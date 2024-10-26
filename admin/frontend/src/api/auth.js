export async function login({login, password}) {
    const response = await fetch(`${import.meta.env.REACT_APP_API_URL}/auth/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            login: login,
            password: password,

        })
    });
    return await response.json();
    
}


export async function get_role_by_token({role}) {
    const response = await fetch(`${import.meta.env.REACT_APP_API_URL}/auth/role`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            role: role,
        })
    });
    return await response.json();
}
