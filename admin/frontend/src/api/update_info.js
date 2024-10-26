import { formatJSON } from "../utils/format";


export async function update_table_info({ table, data }) {
    const response = await fetch(`${import.meta.env.REACT_APP_API_URL}/api/${table}/update`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formatJSON(data))
    });

    if (!response.ok) {
        const error = await response.json();
        console.error('Ошибка на сервере:', error);
        throw new Error(`Server error: ${JSON.stringify(error.detail)}`);
    }
    return await response.json();
}
