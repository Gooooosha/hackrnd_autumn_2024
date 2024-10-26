import React, { useState, useEffect } from 'react';
import { Modal, Button, Form, Input, InputNumber, DatePicker, Checkbox } from 'rsuite';

const EditModal = ({ open, onClose, data, onSave, columnsConfig }) => {
  const [formData, setFormData] = useState(data);

  useEffect(() => {
    const initialValues = { ...data };
    columnsConfig.forEach(column => {
      if (column.type === 'boolean' && formData[column.key] === undefined) {
        initialValues[column.key] = false;
      }
    });
    setFormData(initialValues);
  }, [data, columnsConfig]);

  const handleChange = (value, key) => {
    setFormData(prevData => ({ ...prevData, [key]: value }));
  };

  const handleSave = () => {
    const formattedRow = {
      ...formData,
      planned_delivery_date: formData.planned_delivery_date
        ? formData.planned_delivery_date.toISOString().split('T')[0]
        : null,
    };
    onSave(formattedRow);
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
      case 'varchar':
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
        <Modal.Title>Редактирование записи</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form fluid>
          {columnsConfig.map(column => {
            const { key, label, type } = column;
            return (
              key !== 'id' && (
                <Form.Group key={key}>
                  <Form.ControlLabel>{label}</Form.ControlLabel>
                  {renderInput(type, key, formData[key])}
                </Form.Group>
              )
            );
          })}
        </Form>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={handleSave} appearance="primary">
          Сохранить
        </Button>
        <Button onClick={onClose} appearance="default">
          Закрыть
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default EditModal;
