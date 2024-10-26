import React, { useState } from 'react';
import { Modal, Button, Uploader, Notification } from 'rsuite';

const FileUploadModal = ({ open, onClose, onFileUpload }) => {
  const [fileList, setFileList] = useState([]);

  const handleUpload = async () => {
    if (fileList.length === 0) {
      Notification.error({ title: 'Ошибка', description: 'Пожалуйста, выберите файл для загрузки' });
      return;
    }

    const formData = new FormData();
    formData.append('file', fileList[0].blobFile);

    try {
      const response = await fetch(`${process.env.REACT_APP_API_URL}/api/client/uploadfile`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Ошибка загрузки файла');
      }

      const data = await response.json();
      console.log('Загруженные данные:', data);

      onFileUpload(data);

      onClose();
    } catch (error) {
      Notification.error({ title: 'Ошибка', description: 'Не удалось загрузить файл' });
      console.error('Ошибка загрузки файла:', error);
    }
  };

  return (
    <Modal open={open} onClose={onClose}>
      <Modal.Header>
        <Modal.Title>Добавление записи с файла</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Uploader
          fileList={fileList}
          onChange={setFileList}
          action=""
          draggable
          listType="text"
          autoUpload={false}
        >
          <div style={{ lineHeight: '200px', textAlign: 'center' }}>
            <span>Нажмите или перетащите файл в область</span>
          </div>
        </Uploader>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={onClose} appearance="subtle">
          Отмена
        </Button>
        <Button onClick={handleUpload} appearance="primary">
          Загрузить
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default FileUploadModal;
