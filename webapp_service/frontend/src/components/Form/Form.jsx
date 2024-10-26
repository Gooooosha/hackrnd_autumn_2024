import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import './Form.css';
import ModalWindow from "../ModalWIndow/ModalWindow";
import Button from "../Button/Button";
import Input from "../Input/Input";
import CodeVerificationPage from "../../Pages/CodeVerificationPage";


const Form = ({ isSignIn }) => {

   const [fullName, setFullName] = useState('')
   const [phone, setPhone] = useState('')
   const [email, setEmail] = useState('')
   const [address, setAddress] = useState('')
   const [contract, setContract] = useState('')
   const [code, setCode] = useState('')
   const [isContractVerified, setContractVerified] = useState(false)
   const [isModalOpen, setIsModalOpen] = useState(false)

   const navigate = useNavigate();
   const toHome = () => {
      navigate('/')
   }

   const validateForm = async () => {
      if (isSignIn) {
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
      } else {
          if (fullName.length && phone.length && email.length && address.length) {
              const formArray = { fullName, phone, email, address };
              try {
                  const response = await fetch('http://localhost:8000/registration', {
                      method: 'POST',
                      headers: { 'Content-Type': 'application/json' },
                      body: JSON.stringify(formArray)
                  });
  
                  if (response.ok) {
                      console.log('Регистрация успешна:', await response.json());
                      setIsModalOpen(true);
                      setTimeout(() => {
                          toHome();
                      }, 2000);
                  } else {
                      console.error('Error');
                  }
              } catch (error) {
                  console.error('Error:', error);
              }
          }
      }
  }

   return (
      <>
         <div className="form-wrapper">
            <form className="form">
               <button className="form__button" type="button" onClick={toHome}>	&lt;- Назад</button>

               {isSignIn ? (
                  !isContractVerified ? (
                     <>
                        <h1 className="form__title">Форма входа</h1>
                        <Input
                           type="text"
                           placeholder={"Номер договора"}
                           onChange={(e) => setContract(e.target.value)}
                        />
                        <Button onClick={validateForm} type='button'>Дальше</Button>
                     </>
                  ) : (
                     <>
                        <CodeVerificationPage />
                     </>
                  )
               ) : (
                  <>
                     <h1>Форма регистрации</h1>
                     <Input
                        type="text"
                        className="form__input input"
                        placeholder="ФИО"
                        onChange={(e) => setFullName(e.target.value)}
                     />
                     <Input
                        type="tel"
                        className="form__input input"
                        placeholder="Телефон"
                        onChange={(e) => setPhone(e.target.value)}
                     />
                     <Input
                        type="email"
                        className="form__input input"
                        placeholder="Электронная почта"
                        onChange={(e) => setEmail(e.target.value)}
                     />
                     <Input
                        type="text"
                        className="form__input input"
                        placeholder="Адрес для подключения"
                        onChange={(e) => setAddress(e.target.value)}
                     />
                     <Button type={'button'} onClick={validateForm}>Подать заявку</Button>
                  </>
               )}
            </form>
         </div>
         {isModalOpen && <ModalWindow />}
      </>
   )

}

export default Form;