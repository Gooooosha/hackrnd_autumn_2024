import React, { useState, useEffect } from 'react';
import { CustomTable } from "../../pages/CustomTable";
import { get_table_info } from '../../api/get_info';
import {created_at, updated_at} from '../../utils/time_mixin';

let columnsConfig = [
  { key: 'id', label: 'Id', width: 60, align: 'center', fixed: true},
  { key: 'contract_number', label: 'Договор', width: 300, type: "varchar"},
  { key: 'name', label: 'Имя', width: 200, type: "varchar"},
  { key: 'surname', label: 'Фамилия', width: 200, type: "varchar"},
  { key: 'middle_name', label: 'Отчество', width: 200, type: "varchar"},
  { key: 'phone_number', label: 'Телефон', width: 400, type: "varchar"},
  { key: 'email', label: 'Почта', width: 300, type: "varchar"},
  { key: 'address', label: 'Адрес', width: 500, type: "varchar"},
  { key: 'tg_id', label: 'TG ID', width: 100, type: "numeric"},
];

columnsConfig.push(created_at);
columnsConfig.push(updated_at);

const Client = () => {
  const [data, setData] = useState([]);
  const tablename = 'client';

  useEffect(() => {
    const fetchData = async () => {
      try {
        // const jsonData = await get_table_info({ table: tablename });
        const jsonData = [
          {
            id: 1,
            contract_number: '516124213148',
            name: 'Владислав',
            surname: 'Березкин',
            middle_name: 'Игоревич',
            phone_number: '89131234567',
            email: 'dfsjm@mail.ru',
            address: 'Ростовская обл., г. Ростов-на-Дону, ул. Красноармейская, д. 1',
            tg_id: '1241414',
            created_at: '2023-01-01T00:00:00',
            updated_at: '2023-01-01T00:00:00'
          }
        ];
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
      addFromFile={true}
      columnsConfig={columnsConfig}
      data={data}
      setData={setData}
      filtered={true}
    />
  );
};

export default Client;
