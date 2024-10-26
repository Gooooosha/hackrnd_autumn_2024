import React from 'react';
import './Input.css'

function Input({type, onChange, placeholder}) {
  return (
   <input type={type} placeholder={placeholder} onChange={onChange} className='input'/>
  );
}

export default Input;
