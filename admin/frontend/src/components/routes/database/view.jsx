import React, { useState } from 'react';
import { Tabs } from 'rsuite';
import Client from '../../tables/Client';
import Editor from '../../tables/Editor';
import Purpose from '../../tables/Purpose';
import Reply from '../../tables/Reply';
import Intention from '../../tables/Intention';
import { useRole } from '../RoleContext';
import NotFound from '../notfound/view';

function MainLayout() {
  const [adminActiveTab, setAdminActiveTab] = useState('client');
  const [editorActiveTab, setEditorActiveTab] = useState('purpose');
  const { role } = useRole();

  if (!role) {
    return <NotFound />;
  }

  const adminTabs = [
    { key: 'client', title: 'Клиенты', component: <Client /> },
    { key: 'editor', title: 'Редакторы', component: <Editor /> },
  ];

  const editorTabs = [
    { key: 'intention', title: 'Обращения', component: <Intention /> },
    { key: 'purpose', title: 'Намерения', component: <Purpose /> },
    { key: 'reply', title: 'Ответы', component: <Reply /> },
  ];

  const tabs = role === 'admin' ? adminTabs : editorTabs;
  const activeTab = role === 'admin' ? adminActiveTab : editorActiveTab;
  const setActiveTab = role === 'admin' ? setAdminActiveTab : setEditorActiveTab;

  return (
    <div>
      <Tabs activeKey={activeTab} onSelect={setActiveTab} appearance="pills">
        {tabs.map(({ key, title, component }) => (
          <Tabs.Tab key={key} eventKey={key} title={title}>
            <div style={{ padding: 20 }}>
            {component}
            </div>
          </Tabs.Tab>
        ))}
      </Tabs>
    </div>
  );
}

export default MainLayout;
