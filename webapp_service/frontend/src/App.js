import { useEffect } from 'react';
import './App.css';
import { BrowserRouter, Routes, Route} from 'react-router-dom';
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
