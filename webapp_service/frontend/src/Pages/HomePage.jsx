import React from 'react';
import { useNavigate } from 'react-router-dom';
import Button from '../components/Button/Button';
import './styles/HomePage.css'


function HomePage() {

const navigate = useNavigate();
const toRegistration = () => {
  navigate('/registration')
}
const toSignIn = () => {
  navigate('/signin')
}

  return (
    <div className='container'>
      <div className="container__buttons-wrapper">
     <Button onClick={toRegistration}>Заключить договор</Button>
     <Button onClick={toSignIn}>Войти как клиент ТТК</Button>
    </div>
    </div>
  );
}

export default HomePage;
