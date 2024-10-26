import React from 'react';
import './Input.css'

function Input({type, onChange, placeholder, value}) {
  return (
   <input type={type} placeholder={placeholder} onChange={onChange} className='input' value={value}/>
  );
}

export default Input;
