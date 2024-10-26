import React from "react";
import './Form.css';
import logo from '../../assets/logo.png';

const Form = ({ title, children, onSubmit }) => (
  <div className="form-wrapper">
    <form className="form" onSubmit={onSubmit}>
      <div className="form__logo-wrapper">
      <img src={logo} alt="ТТК-лого" className="form__logo"/>
      </div>
      <h1 className="form__title">{title}</h1>
      <div className="form__container">{children}</div>
    </form>
  </div>
);

export default Form;