import React, { useState, useEffect } from 'react';
import { Modal, Button, Panel } from 'rsuite';
import 'rsuite/dist/rsuite.min.css';

const DetailModal = ({ open, onClose, data, onEdit, onDelete, canChange, columnsConfig }) => {
  const [confirmModalOpen, setConfirmModalOpen] = useState(false);

  useEffect(() => {

  }, []);

  if (!data) return null;

  const handleDeleteClick = () => {
    setConfirmModalOpen(true);
  };

  const handleConfirmDelete = () => {
    onDelete(data);
    setConfirmModalOpen(false);
  };

  const handleCancelDelete = () => {
    setConfirmModalOpen(false);
  };


  console.log(data);
  
  return (
    <>
      <Modal
        open={open}
        onClose={onClose}
        size="lg"
      >
        <Modal.Header>
          <Modal.Title>Подробная информация</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Panel bordered>
          {Object.keys(data).map((key) => {
            const columnConfig = columnsConfig.find((config) => config.key === key);
            if (columnConfig && key !== 'actions') {
              return (
                <React.Fragment key={key}>
                  <div style={{ display: 'flex', gap: '10px', marginBottom: '10px' }}>
                    <strong>{columnConfig.label}: </strong>
                    <span>
                      {typeof data[key] === 'boolean' ? (data[key] ? 'Да' : 'Нет') : data[key]}
                    </span>
                  </div>
                </React.Fragment>
              );
            }
            return null;
          })}
          </Panel>
        </Modal.Body>
        <Modal.Footer>

        {canChange ? (
            <>
              <Button appearance="primary" onClick={() => onEdit(data)} style={{ marginLeft: '10px' }}>Редактировать</Button>
              <Button appearance="default" onClick={handleDeleteClick} style={{ marginLeft: '10px' }}>Удалить</Button>
            </>
          ) : (
            <>
              <Button appearance="primary" onClick={onClose} style={{ marginLeft: '10px' }}>Закрыть</Button>
            </>
          )}
        </Modal.Footer>

      </Modal>

      <Modal
        open={confirmModalOpen}
        onClose={() => setConfirmModalOpen(false)}
        size="xs"
      >
        <Modal.Header>
          <Modal.Title>Подтверждение удаления</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <p>Вы уверены, что хотите удалить этот элемент?</p>
        </Modal.Body>
        <Modal.Footer>
          <Button onClick={handleConfirmDelete} appearance="primary">Удалить</Button>
          <Button onClick={handleCancelDelete} appearance="default">Отмена</Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default DetailModal;
