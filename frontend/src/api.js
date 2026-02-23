const BASE_URL = "http://localhost:8001/api";

export async function authFetch(endpoint, options = {}) {
    const token = localStorage.getItem("token");
    const headers = {
        "Content-Type": "application/json",
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
        ...options.headers,
    };
    const response = await fetch(`${BASE_URL}${endpoint}`, { ...options, headers });
    return response;
}

export async function apiPost(endpoint, body) {
    return authFetch(endpoint, {
        method: "POST",
        body: JSON.stringify(body),
    });
}
