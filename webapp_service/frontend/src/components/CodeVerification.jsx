import Form from "./Form/Form";
import React, { useState } from "react";

import Input from "../components/Input/Input";
import Button from "../components/Button/Button";

function CodeVerification() {
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
        <Form title="Подтверждение входа" onSubmit={(e) => e.preventDefault()}>
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
      </Form>
    )
}
export default CodeVerification;