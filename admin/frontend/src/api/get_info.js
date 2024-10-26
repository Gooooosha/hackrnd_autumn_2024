export async function get_table_info({table}) {
    const response = await fetch(`${import.meta.env.REACT_APP_API_URL}/api/${table}/get_all`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    });
    return await response.json();
    
}

export async function get_filtered_table_info({ table, start_date, end_date }) {
    const response = await fetch(`${import.meta.env.REACT_APP_API_URL}/api/${table}/get_filtered?start_date=${encodeURIComponent(start_date)}&end_date=${encodeURIComponent(end_date)}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    });
    return await response.json();
}
