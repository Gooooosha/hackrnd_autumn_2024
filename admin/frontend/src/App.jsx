import './App.css';
import 'rsuite/dist/rsuite.min.css';
import './index.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Auth from './components/routes/auth/view';
import MainLayout from './components/routes/database/view';
import { RoleProvider } from './components/routes/RoleContext';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <RoleProvider>
          <Routes>
            <Route path="/auth" element={<Auth />} />
            <Route path="/database" element={<MainLayout/>} />
          </Routes>
        </RoleProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
