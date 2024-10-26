import React, { useState } from "react";
import Form from "./Form/Form";
import Input from "./Input/Input";
import Button from "./Button/Button";
import { useNavigate } from "react-router-dom";

const SignInForm = () => {
  const [contract, setContract] = useState('');
  const [isContractVerified, setContractVerified] = useState(false)
  const navigate = useNavigate();

  const handleSignIn = async () => {
    if (contract.length) {
        try {
            const response = await fetch('http://localhost:8000/registration', {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' }
            });

            const data = await response.json();
            const isContractValid = data.some(item => item.contract === contract);
            
            if (isContractValid) {
                setContractVerified(true);
               navigate('/signin/code')
            } else {
                alert('Контракт не найден!');
            }
        } catch (error) {
            console.error('Error fetching contracts:', error);
        }
    }
  };

  return (
    <Form title="Вход в личный кабинет" onSubmit={(e) => e.preventDefault()}>
      <Input
        type="text"
        placeholder="Номер договора"
        value={contract}
        onChange={(e) => setContract(e.target.value)}
      />
      <Button onClick={handleSignIn} type="button">
        Дальше
      </Button>
    </Form>
  );
};

export default SignInForm;