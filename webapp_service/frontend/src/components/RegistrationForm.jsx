import React, { useState } from "react";
import Form from "./Form/Form";
import Input from "./Input/Input";
import Button from "./Button/Button";

const RegistrationForm = ({setModal }) => {
  const [fullName, setFullName] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');
  const [address, setAddress] = useState('');

  const handleInputChange = (event) => {
    const inputValue = event.target.value;
    if (inputValue.match(/^\d*$/)) {
    setPhone(inputValue);
    }
  };


  const handleRegistration = async () => {
    if (fullName.length && phone.length && email.length && address.length) {
        const formArray = { fullName, phone, email, address };
        try {
            const response = await fetch('http://localhost:8000/registration', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formArray)
            });

            if (response.ok) {
                console.log('Регистрация успешна:', await response.json());
                setModal(true);
                
                setFullName('')
                setPhone('')
                setEmail('')
                setAddress('')

            } else {
                console.error('Error');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    }
  };

  return (
    <>
    
    <Form title="Форма заявления" onSubmit={(e) => e.preventDefault()}>
    
      <Input
        type="text"
        placeholder="ФИО"
        value={fullName}
        onChange={(e) => setFullName(e.target.value)}
      />
      <Input
        type="tel"
        placeholder="Телефон"
        value={phone}
        onChange={handleInputChange}
      />
      <Input
        type="email"
        placeholder="Электронная почта"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <Input
        type="text"
        placeholder="Адрес для подключения"
        value={address}
        onChange={(e) => setAddress(e.target.value)}
      />
      <Button onClick={handleRegistration} type="button">
        Подать заявку
      </Button>
    </Form>
    </>
  );
};

export default RegistrationForm;