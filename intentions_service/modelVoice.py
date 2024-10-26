import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import load_model
from pymorphy3 import MorphAnalyzer
import joblib
import spacy
import numpy as np
# from pydub import AudioSegment
import wave
import vosk
import json



class IntentRecognizer:
    def __init__(self, model_path='model.keras', vectorizer_path='vectorizer.pkl',
                 label_encoder_path='label_encoder.pkl'):
        self.model_path = model_path
        self.vectorizer_path = vectorizer_path
        self.label_encoder_path = label_encoder_path
        self.nlp = spacy.load("ru_core_news_sm")
        self.morph = MorphAnalyzer()

        if os.path.exists(self.vectorizer_path):
            self.vectorizer = joblib.load(self.vectorizer_path)
        else:
            self.vectorizer = TfidfVectorizer()

        if os.path.exists(self.label_encoder_path):
            self.label_encoder = joblib.load(self.label_encoder_path)
        else:
            self.label_encoder = LabelEncoder()  # Initialize a new label encoder

        if os.path.exists(self.model_path):
            self.model = load_model(self.model_path)
            print("Загружена обученная модель.")
        else:
            print("Обученная модель не найдена. Начинаю обучение.")
            self.data_samples = self._get_data_samples()
            self.X, self.y = self._prepare_data()
            self.model = self._train_model()

    def retrain_model(self):
        for file_path in [self.model_path, self.vectorizer_path, self.label_encoder_path]:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"{file_path} удален для перетренировки.")

        self.data_samples = self._get_data_samples()
        self.X, self.y = self._prepare_data()
        
        self.model = self._train_model()
        print("Модель обучена и сохранена.")

    def _get_data_samples(self):
        return [
            {"text": "не работает", "intent": "problem"},
            {"text": "не грузит", "intent": "problem"},
            {"text": "не загружается", "intent": "problem"},
            {"text": "есть проблема", "intent": "problem"},
            {"text": "проблема", "intent": "problem"},
            {"text": "зависание", "intent": "problem"},
            {"text": "сеть недоступна", "intent": "problem"},
            {"text": "нестабильное соединение", "intent": "problem"},
            {"text": "ошибка подключения", "intent": "problem"},
            {"text": "не удается подключиться", "intent": "problem"},
            {"text": "изменить тариф на максимальный", "intent": "editTariff"},
            {"text": "изменить тариф на мощный", "intent": "editTariff"},
            {"text": "изменить тариф на честный", "intent": "editTariff"},
            {"text": "перейти на тариф максимальный", "intent": "editTariff"},
            {"text": "перейти на тариф мощный", "intent": "editTariff"},
            {"text": "перейти на тариф честный", "intent": "editTariff"},
            {"text": "поменять тариф на максимальный", "intent": "editTariff"},
            {"text": "поменять тариф на мощный", "intent": "editTariff"},
            {"text": "поменять тариф на честный", "intent": "editTariff"},
            {"text": "добавить услугу антивирус касперский", "intent": "addService"},
            {"text": "добавить услугу выделенный ip", "intent": "addService"},
            {"text": "добавить услугу персональный менеджер", "intent": "addService"},
            {"text": "добавить услугу фирменный роутер", "intent": "addService"},
            {"text": "подключить услугу антивирус касперский", "intent": "addService"},
            {"text": "подключить услугу выделенный ip", "intent": "addService"},
            {"text": "подключить услугу персональный менеджер", "intent": "addService"},
            {"text": "подключить услугу фирменный роутер", "intent": "addService"},
            {"text": "заключить новый договор", "intent": "contract"},
            {"text": "заключить договор", "intent": "contract"},
        ]

    def _preprocess_text(self, text):
        doc = self.nlp(text.lower())
        lemmas = [self.morph.parse(token.text)[0].normal_form for token in doc if not token.is_stop]
        return " ".join(lemmas)

    def _prepare_data(self):
        for sample in self.data_samples:
            sample["text"] = self._preprocess_text(sample["text"])

        texts = [sample["text"] for sample in self.data_samples]
        intents = [sample["intent"] for sample in self.data_samples]

        # Create feature vectors using TF-IDF
        X = self.vectorizer.fit_transform(texts).toarray()
        joblib.dump(self.vectorizer, self.vectorizer_path)  # Save the vectorizer

        y = self.label_encoder.fit_transform(intents)
        joblib.dump(self.label_encoder, self.label_encoder_path)  # Save the label encoder

        return X, y

    def _train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)

        model = Sequential([
            Dense(128, input_shape=(self.X.shape[1],), activation='relu'),
            Dropout(0.5),
            Dense(64, activation='relu'),
            Dropout(0.5),
            Dense(len(set(self.y)), activation='softmax')
        ])

        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        model.fit(X_train, y_train, epochs=100, batch_size=1, validation_data=(X_test, y_test))

        model.save(self.model_path)  # Save the trained model
        return model

    def predict_intent(self, text):
        processed_text = self._preprocess_text(text)
        text_vector = self.vectorizer.transform([processed_text]).toarray()
        prediction = self.model.predict(text_vector)
        predicted_intent = np.argmax(prediction)
        return self.label_encoder.inverse_transform([predicted_intent])[0]

    def extract_parameters(self, text, intent):
        lemmas = self._preprocess_text(text).split()
        parameter = ''

        if intent == "editTariff":
            tariffs = ["максимальный", "мощный", "честный"]
            for tariff in tariffs:
                if tariff in lemmas:
                    parameter = tariff

        elif intent == "addService":
            services = ["антивирус касперский", "выделенный ip", "персональный менеджер", "фирменный роутер"]
            for service in services:
                service_tokens = service.split()
                if all(token in lemmas for token in service_tokens):
                    parameter = service

        elif intent == "contract":
            if "договор" in lemmas:
                parameter = 'договор'

        return parameter

    def recognize_intent_with_params(self, text, threshold=0.6, unknown_word_ratio=0.6):
        intent = self.predict_intent(text)
        processed_text = self._preprocess_text(text)
        text_vector = self.vectorizer.transform([processed_text]).toarray()

        prediction = self.model.predict(text_vector)
        predicted_probability = np.max(prediction)

        unknown_ratio = 1
        lemmas = processed_text.split()
        known_words = [lemma for lemma in lemmas if lemma in self.vectorizer.get_feature_names_out()]
        if len(lemmas) > 1:
            unknown_ratio -= (len(known_words) / len(lemmas))

        if predicted_probability < threshold or unknown_ratio > unknown_word_ratio:
            return "error", None

        parameters = self.extract_parameters(text, intent)

        if intent in ["editTariff", "addService"] and not parameters:
            return "error", None

        return intent, parameters

    def recognize_speech_from_audio(self, wav_path):
        vosk.SetLogLevel(True)
        model = vosk.Model("intentions_service/model_vosk")

        wf = wave.open(wav_path, "rb")

        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
            raise ValueError("Аудиофайл должен быть в формате WAV с моно, 16 битами и частотой дискретизации 16000 Гц")

        rec = vosk.KaldiRecognizer(model, wf.getframerate())

        result_text = ""
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result_text = json.loads(rec.Result())["text"]
                print(f"Фраза целиком: {result_text}")

        result_text = json.loads(rec.FinalResult())["text"]
        print("\nРаспознанный текст:", result_text)
        return result_text

recognizer = IntentRecognizer()

def get_intent_by_voice(file_name: str):
    recognized_text = recognizer.recognize_speech_from_audio(f"intentions_service/voices/{file_name}.wav")
    intent, params = recognizer.recognize_intent_with_params(recognized_text)
    return intent


def get_intent_by_text(text: str):
    intent, params = recognizer.recognize_intent_with_params(text)
    return intent
