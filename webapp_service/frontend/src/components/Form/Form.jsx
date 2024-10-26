import React from "react";
import './Form.css';

const Form = ({ title, children, onSubmit }) => (
  <div className="form-wrapper">
    <form className="form" onSubmit={onSubmit}>
      <h1 className="form__title">{title}</h1>
      <div className="form__container">{children}</div>
    </form>
  </div>
);

export default Form;