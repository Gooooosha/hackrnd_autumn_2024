import { useEffect } from 'react';
import './App.css';
import HomePage from './Pages/HomePage';
import { BrowserRouter, Routes, Route, useNavigate } from 'react-router-dom';
import RegistrationPage from './Pages/RegistrationPage';
import {RoutesPath} from './Router/index'


const tg = window.Telegram.WebApp;

function App() {
  useEffect(() => {
    tg.ready();
  }, [])
  const onClose = () => {
    tg.close()
  }

  return (
    <BrowserRouter>
    <Routes>
    {RoutesPath.map((route, index) => {
      return (
      <Route 
      key={index}
      path={route.path}
      element={<route.component />}
      exact = {route.exact}
      />)
    })}
    </Routes>
    </BrowserRouter>
  
  );
}
export default App;
