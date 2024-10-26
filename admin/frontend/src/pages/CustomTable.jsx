import React, { useState } from 'react';
import { Table, TagPicker, Notification, DatePicker, toaster, Button, Pagination, SelectPicker } from 'rsuite';
import DetailModal from '../components/modal/DetailModal';
import EditModal from '../components/modal/EditModal';
import AddModal from '../components/modal/AddModal';
import FileUploadModal from '../components/modal/FileModal';
import { update_table_info } from '../api/update_info';
import { add_table_info } from '../api/add_table_info';
import { delete_table_info } from '../api/delete_table_info';
import { get_table_info, get_filtered_table_info } from '../api/get_info';
import { formatDate } from '../utils/format';
const { Column, HeaderCell, Cell } = Table;

export const CustomTable = ({ tableName, addFromFile, columnsConfig, data, setData, filtered = false }) => {
  const [columnKeys, setColumnKeys] = useState(columnsConfig.map(column => column.key));
  const [loading, setLoading] = useState(false);
  const [detailModalOpen, setDetailModalOpen] = useState(false);
  const [editModalOpen, setEditModalOpen] = useState(false);
  const [addModalOpen, setAddModalOpen] = useState(false);
  const [addFileModalOpen, setAddFileModalOpen] = useState(false);
  const [selectedRow, setSelectedRow] = useState(null);
  const [rowToEdit, setRowToEdit] = useState(null);
  const [filteredData, setFilteredData] = useState(data);

  const [page, setPage] = useState(1);
  const [limit, setLimit] = useState(10);
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const selectedColumns = columnsConfig.filter(column => columnKeys.includes(column.key));
  const isButtonDisabled = !startDate || !endDate;

  const showNotification = (message) => {
    toaster.push(<Notification type="error" duration={2000} header="Ошибка">{message}</Notification>, { placement: 'topEnd' });
  };

  const handleStartDateChange = (date) => {
    if (endDate && date > endDate) {
      showNotification('Начальная дата не может быть больше конечной даты');
      return;
    }
    setStartDate(date);
  };

  const handleEndDateChange = (date) => {
    if (startDate && date < startDate) {
      showNotification('Конечная дата не может быть меньше начальной даты');
      return;
    }
    if (startDate && date.toDateString() === startDate.toDateString()) {
      showNotification('Нельзя выбирать одну и ту же дату');
      return;
    }
    setEndDate(date);
  };

  const handleRowClick = (rowData) => {
    if (editModalOpen) {
      setEditModalOpen(false);
    }
    setSelectedRow(rowData);
    setDetailModalOpen(true);
  };

  const handleEdit = (rowData) => {
    setDetailModalOpen(false);
    setRowToEdit(rowData);
    setEditModalOpen(true);
  };

  const handleSave = async (updatedRow) => {
    try {
      const response = await update_table_info({ table: tableName, data: updatedRow });
      setData(prevData =>
        prevData.map(row => (row.id === response.id ? response : row))
      );
      setEditModalOpen(false);
    } catch (error) {
      console.error('Error updating data:', error);
    }
  };

  const handleDelete = async (rowData) => {
    try {
        const response = await delete_table_info({ table: tableName, id: rowData.id });

        if (response && response.success) {
            setData(prevData => prevData.filter(row => row.id !== rowData.id));
            setDetailModalOpen(false);
        } else {
            throw new Error('Unexpected response format');
        }
    } catch (error) {
        console.error('Error deleting data:', error);
    }
  };

  const handleAdd = async (newRow) => {
    try {
      const response = await add_table_info({ table: tableName, data: newRow });
      setData(prevData => {
        const updatedData = [...prevData, response];
        return updatedData;
      });
  
      setAddModalOpen(false);
    } catch (error) {
      console.error('Error adding data:', error);
    }
  };
  
  const handleFileUpload = async (newData) => {
    try {
      const responses = await Promise.all(
        newData.map(async (row) => {
          const response = await add_table_info({ table: tableName, data: row });
          return response[0];
        })
      );
  
      setData(prevData => [...prevData, ...responses]);
    } catch (error) {
      console.error('Error uploading file data:', error);
    }
  };
  

  const CustomCell = (props) => {
    const { dataKey, rowData, ...rest } = props;

    const renderCellValue = (value) => {
      if (typeof value === 'boolean') {
        return value ? '+' : '-';
      }
      return value;
    };
    
    return <Cell {...rest}>{renderCellValue(rowData[dataKey])}</Cell>;
  };

  const handlePageChange = (newPage) => {
    setPage(newPage);
  };

  const handleLimitChange = (newLimit) => {
    setPage(1);
    setLimit(newLimit);
  };

  let paginatedData = data.slice((page - 1) * limit, page * limit);


  const handleSubmit = async () => {
    const formattedStartDate = formatDate(startDate);
    const formattedEndDate = formatDate(endDate);
    try {
      const jsonData = await get_filtered_stat_table_info({ table: tableName, start_date: formattedStartDate, end_date: formattedEndDate });
      setData(jsonData);
      setFilteredData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const handleResetFilters = async () => {
    setStartDate(null);
    setEndDate(null);
    try {
      const jsonData = await get_table_info({ table: tableName });
      setData(jsonData);
      setFilteredData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <div style={{ display: "flex", gap: "1rem", flexDirection: "row", justifyContent: "space-between", alignItems: "center" }}>
        Поля для отображения:
        <TagPicker
          style={{ marginLeft: "1rem" }}
          data={columnsConfig}
          labelKey="label"
          valueKey="key"
          value={columnKeys}
          onChange={setColumnKeys}
          cleanable={false}
        />
        <div style={{ display: "flex", flexDirection: "column" }}>
          <Button
            appearance="primary"
            onClick={() => setAddModalOpen(true)}
            style={{width: "9rem", marginBottom: "1rem"}}
          >
            Новая запись
          </Button>
          {addFromFile && <Button
            appearance="primary"
            onClick={() => setAddFileModalOpen(true)}
            style={{width: "9rem"}}
          >
            Добавить из файла
          </Button>}
        </div>
      </div>

      <div style={{ display: "flex", gap: "1rem", alignItems: "center", marginTop: "1rem" }}>
        <span>Показывать по:</span>
        <SelectPicker
          data={[
            { label: '10', value: 10 },
            { label: '20', value: 20 },
            { label: '30', value: 30 },
            { label: '50', value: 50 },
          ]}
          value={limit}
          onChange={handleLimitChange}
          cleanable={false}
          style={{ width: 120 }}
        />
        {filtered && <>
        <DatePicker 
          placeholder="Начальная дата"
          value={startDate}
          onChange={handleStartDateChange}
        />
        <DatePicker
          placeholder="Конечная дата"
          value={endDate}
          onChange={handleEndDateChange}
        />

        <Button 
          appearance="primary" 
          onClick={handleSubmit} 
          disabled={isButtonDisabled}
        >
          Отправить
        </Button>

        <Button 
          appearance="default" 
          onClick={handleResetFilters}
        >
          Сбросить фильтры
        </Button>
        </>}
      </div>

      <div>
        <Table
          loading={loading}
          hover
          showHeader
          autoHeight
          data={paginatedData}
          bordered
          cellBordered
          headerHeight={40}
          rowHeight={46}
          style={{ marginTop: "1rem" }}
          onRowClick={handleRowClick}
        >
          {selectedColumns.map(column => {
            const { key, ...otherProps } = column;
            return (
              <Column key={key} {...otherProps}>
                <HeaderCell>{column.label}</HeaderCell>
                <CustomCell dataKey={column.key} />
              </Column>
            );
          })}
        </Table>
      </div>

      <Pagination
        ellipsis
        prev
        next
        first
        last
        style={{ marginTop: '1rem', textAlign: 'right' }}
        total={data.length}
        limit={limit}
        activePage={page}
        onChangePage={handlePageChange}
        onChangeLimit={handleLimitChange}
        limitOptions={[10, 20, 30, 50]}
      />

      {detailModalOpen && selectedRow && (
        <DetailModal
          open={detailModalOpen}
          onClose={() => setDetailModalOpen(false)}
          data={selectedRow}
          onEdit={handleEdit}
          onDelete={handleDelete}
          canChange={true}
          columnsConfig={columnsConfig}
        />
      )}
      {editModalOpen && rowToEdit && (
        <EditModal
          open={editModalOpen}
          onClose={() => setEditModalOpen(false)}
          data={rowToEdit}
          onSave={handleSave}
          columnsConfig={columnsConfig}
        />
      )}
      {addModalOpen && (
        <AddModal
          open={addModalOpen}
          onClose={() => setAddModalOpen(false)}
          onSave={handleAdd}
          columnsConfig={columnsConfig.slice(1, -2)}
        />
      )}
      {addFileModalOpen && (
        <FileUploadModal
          open={addFileModalOpen}
          onClose={() => setAddFileModalOpen(false)}
          onFileUpload={handleFileUpload}
        />
      )}
    </div>
  );
};
