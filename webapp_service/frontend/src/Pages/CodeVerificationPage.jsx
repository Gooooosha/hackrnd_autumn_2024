import React, { useState } from "react";
import Form from "../components/Form/Form";
import Input from "../components/Input/Input";
import Button from "../components/Button/Button";
import "./styles/Code.css";

function CodeVerificationPage() {
  const [code, setCode] = useState("");
  const isValid = /^\d{4}$/.test(code);

  const validateCode = () => {
    if (isValid) {
      alert("Код подтвержден");
    } else {
      alert("Код должен содержать 4 цифры");
    }
  };

  const handleInputChange = (event) => {
    const inputValue = event.target.value;
    if (inputValue.match(/^\d*$/)) {
      setCode(inputValue);
    }
  };

  return (
    <form className="form">
      <h1>Подтверждение входа</h1>
      <div className="form__container">
        <Input
          type="text"
          className="form__input input"
          placeholder="Код подтверждения"
          value={code}
          onChange={handleInputChange} 
        />
        <Button type="button" onClick={validateCode}>
          Подтвердить
        </Button>
      </div>
    </form>
  );
}

export default CodeVerificationPage;

