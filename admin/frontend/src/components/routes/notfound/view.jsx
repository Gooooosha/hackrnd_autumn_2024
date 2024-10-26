import React from 'react';
import { Panel, Button, Grid, Row, Col } from 'rsuite';
import { useNavigate } from 'react-router-dom';
import WarningRoundIcon from '@rsuite/icons/WarningRound';

const NotFound = () => {
  const navigate = useNavigate();

  return (
      <div style={{ 
            padding: '50px', 
            backgroundColor: '#f8f8f8', 
            display: 'flex', 
            justifyContent: 'center', 
            alignItems: 'center' 
          }}>
          <Panel shaded bordered style={{ padding: '40px', textAlign: 'center' }}>
            <WarningRoundIcon style={{ fontSize: '72px', color: '#d9534f' }} />
            <h1 style={{ fontSize: '72px', margin: '20px 0' }}>404</h1>
            <h3>Страница не найдена</h3>
            <p style={{ color: '#666' }}>Извините, но такой страницы не существует.</p>
            <Button onClick={() => navigate('/auth')} appearance="primary" style={{ marginTop: '20px' }}>
              Вернуться на главную
            </Button>
          </Panel>
        </div>
  );
};

export default NotFound;
