import React, { useState, useEffect } from 'react';
import { CustomTable } from "../../pages/CustomTable";
import { get_table_info } from '../../api/get_info';
import {created_at, updated_at} from '../../utils/time_mixin';


const columnsConfig = [
  { key: 'id', label: 'Id', width: 60, align: 'center', fixed: true },
  { key: 'mail', label: 'Почта', width: 200, type: "varchar"},
];

columnsConfig.push(created_at);
columnsConfig.push(updated_at);

const Mail = () => {
  const [data, setData] = useState([]);
  const tablename = 'mail';
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        // const jsonData = await get_table_info({ table: tablename });     
        const jsonData = [
          {
            id: 1,
            mail: 'fdsfkm@mail.ru',
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
      columnsConfig={columnsConfig} 
      data={data} 
      setData={setData}
      addFromFile={false}
      filtered={true}
    />
  );
};

export default Mail;
