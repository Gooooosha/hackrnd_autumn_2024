import React from 'react';
import './Button.css'

function Button({children, onClick, type}) {
  return (
    <button className='button' onClick={onClick} type={type}>
      {children}
    </button>
  );
}

export default Button;
