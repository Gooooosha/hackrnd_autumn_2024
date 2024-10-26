import React, { useState, useEffect } from 'react';
import { Modal, Form, Button, Input, InputNumber, DatePicker, Checkbox } from 'rsuite';

const AddModal = ({ open, onClose, onSave, columnsConfig }) => {
  const [newRow, setNewRow] = useState({});

  useEffect(() => {
    const initialValues = {};
    columnsConfig.forEach(column => {
      if (column.type === 'boolean') {
        initialValues[column.key] = false;
      }
    });
    setNewRow(initialValues);
  }, [columnsConfig]);

  const handleChange = (value, key) => {
    setNewRow(prev => ({ ...prev, [key]: value }));
  };

  const handleSave = () => {
    const formattedRow = {
      ...newRow,
      planned_delivery_date: newRow.planned_delivery_date
        ? newRow.planned_delivery_date.toISOString().split('T')[0]
        : null,
    };
    onSave(formattedRow);
    setNewRow({});
  };

  const renderInput = (type, key, value) => {
    switch (type) {
      case 'numeric':
        return (
          <InputNumber 
            value={value || ''} 
            onChange={val => handleChange(val, key)} 
            style={{ width: '100%' }}
          />
        );
      case 'boolean':
        return (
          <Checkbox 
            checked={value || false} 
            onChange={(_, checked) => handleChange(checked, key)}
          >
            Да
          </Checkbox>
        );
        case 'date':
          return (
            <DatePicker
              value={value || null}
              onChange={val => handleChange(new Date(val), key)}
            />
          );

      default:
        return (
          <Input 
            value={value || ''} 
            onChange={val => handleChange(val, key)} 
          />
        );
    }
  };

  return (
    <Modal open={open} onClose={onClose}>
      <Modal.Header>
        <Modal.Title>Добавить запись</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form fluid>
          {columnsConfig.map(column => {
            const { key, label, type } = column;
            return (
              <Form.Group controlId={`formBasic${key}`} key={key}>
                <Form.ControlLabel>{label}</Form.ControlLabel>
                {renderInput(type, key, newRow[key])}
              </Form.Group>
            );
          })}
        </Form>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={handleSave} appearance="primary">
          Сохранить
        </Button>
        <Button onClick={onClose} appearance="default">
          Отмена
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default AddModal;
