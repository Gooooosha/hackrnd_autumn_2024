export async function delete_table_info({ table, id }) {
    try {
        const response = await fetch(`${import.meta.env.REACT_APP_API_URL}/api/${table}/delete`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id })
        });

        if (!response.ok) {
            const error = await response.json();
            console.error('Ошибка на сервере:', error);
            throw new Error(`Server error: ${JSON.stringify(error.detail || 'Unknown error')}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Ошибка при запросе:', error);
        throw error;
    }
}
