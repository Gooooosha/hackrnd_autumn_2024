import React, { useState, useEffect } from 'react';
import { CustomTable } from "../../pages/CustomTable";
import { get_table_info } from '../../api/get_info';
import {created_at, updated_at} from '../../utils/time_mixin';


const columnsConfig = [
  { key: 'id', label: 'ID', width: 60, align: 'center', fixed: true },
  { key: 'login', label: 'Логин', width: 300, type: "varchar"},
  { key: 'hashed_password', label: 'Пароль', width: 500, type: "varchar"},
  { key: 'role', label: 'Роль', width: 200, type: "varchar"},
];

columnsConfig.push(created_at);
columnsConfig.push(updated_at);

const Editor = () => {
  const [data, setData] = useState([]);
  const tablename = 'editor';

  useEffect(() => {
    const fetchData = async () => {
      try {
        // const jsonData = await get_table_info({ table: tablename });  
        const jsonData = [
          {
            id: 1,
            login: 'dfsfdnfsfsdf',
            hashed_password: 'fdn12312ndgs67123123412n',
            role: 'admin',
            created_at: '2023-01-01T00:00:00',
            updated_at: '2023-01-01T00:00:00'
          }
        ]      
        setData(jsonData);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);



  return (
    <CustomTable 
      tableName={tablename}
      addFromFile={false}
      columnsConfig={columnsConfig} 
      data={data} 
      setData={setData}
      filtered={true}
    />
  );
};

export default Editor;
