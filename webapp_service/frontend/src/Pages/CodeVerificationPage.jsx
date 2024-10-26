import React from 'react';
import Form from '../components/Form/Form';
import Input from '../components/Input/Input';
import Button from '../components/Button/Button';
import { useNavigate } from 'react-router-dom';
import './styles/Code.css'

function CodeVerificationPage() {
  const navigate = useNavigate();
  const toHome = () => {
    navigate('/')
 }
  return (
   <form className='form'>
     <button className="form__button" type="button" onClick={toHome}>	&lt;- Назад</button>
    <h1>Подтверждение договора</h1>
                        <Input
                           type="text"
                           className="form__input input"
                           placeholder="Код подтверждения"
                           onChange={(e) => setCode(e.target.value)}
                        />
                        <Button type="button" onClick={() => alert("Код подтвержден!")}>Подтвердить</Button>
   </form>
  );
}

export default CodeVerificationPage;
