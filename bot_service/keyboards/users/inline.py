from aiogram.utils.formatting import as_line, Bold

from bot_service.keyboards.keyboard_constructor import InlineConstructor


def inline_kb_client_menu():
    text = as_line(
        Bold("Вы вошли в главное меню чат-бота для логистики"),
        "\n\nВыберите одно из следующих действий:"
    )
    text_and_data = [["Создание накладной", "creating_invoice"],
                     ["Расчет накладной", 'https://google.com'],
                     ["Отслеживание посылки", "tracking_package"],
                     ["Претензии", "claims"],
                     ["Чат с менеджером", "chat_client"],
                     ["Мои договоры", "contracts"]]
    button_type = ["callback_data", "web_app", "callback_data",
                   "callback_data", "callback_data", "callback_data"]

    reply_markup = InlineConstructor.create_kb(text_and_data=text_and_data,
                                               button_type=button_type)
    return text.as_html(), reply_markup
