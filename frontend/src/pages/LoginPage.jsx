import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { apiPost } from "../api";

export default function LoginPage() {
    const { login } = useAuth();
    const navigate = useNavigate();
    const [form, setForm] = useState({ email: "", password: "" });
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    function handleChange(e) {
        setForm({ ...form, [e.target.name]: e.target.value });
    }

    async function handleSubmit(e) {
        e.preventDefault();
        setError("");
        setLoading(true);
        try {
            const res = await apiPost("/auth/login", {
                email: form.email,
                password: form.password,
            });
            if (!res.ok) {
                const data = await res.json();
                setError(data.detail || "Anmeldung fehlgeschlagen");
                return;
            }
            const data = await res.json();
            login(data.access_token, {
                id: data.user_id,
                name: data.user_name,
                email: data.user_email,
            });
            navigate("/");
        } catch {
            setError("Server nicht erreichbar");
        } finally {
            setLoading(false);
        }
    }

    return (
        <div style={{
            minHeight: "100vh",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            background: "#1a1a2e",
        }}>
            <div style={{
                background: "#16213e",
                borderRadius: 12,
                padding: "40px 48px",
                width: "100%",
                maxWidth: 400,
                boxShadow: "0 8px 32px rgba(0,0,0,0.4)",
            }}>
                <h1 style={{ marginBottom: 8, fontSize: 28, color: "#e0e0e0" }}>
                    Anmelden
                </h1>
                <p style={{ color: "#888", marginBottom: 28, fontSize: 14 }}>
                    Bürobuchungssystem
                </p>

                {error && (
                    <div style={{
                        background: "#3d1515",
                        color: "#ff6b6b",
                        padding: "10px 14px",
                        borderRadius: 8,
                        marginBottom: 20,
                        fontSize: 14,
                    }}>
                        {error}
                    </div>
                )}

                <form onSubmit={handleSubmit}>
                    <label style={labelStyle}>E-Mail</label>
                    <input
                        type="email"
                        name="email"
                        value={form.email}
                        onChange={handleChange}
                        required
                        style={inputStyle}
                        placeholder="name@beispiel.de"
                    />

                    <label style={labelStyle}>Passwort</label>
                    <input
                        type="password"
                        name="password"
                        value={form.password}
                        onChange={handleChange}
                        required
                        style={inputStyle}
                        placeholder="••••••••"
                    />

                    <button type="submit" disabled={loading} style={buttonStyle}>
                        {loading ? "Wird angemeldet…" : "Anmelden"}
                    </button>
                </form>

                <p style={{ textAlign: "center", marginTop: 24, color: "#888", fontSize: 14 }}>
                    Noch kein Konto?{" "}
                    <Link to="/register" style={{ color: "#4f8ef7", textDecoration: "none" }}>
                        Registrieren
                    </Link>
                </p>
            </div>
        </div>
    );
}

const labelStyle = {
    display: "block",
    marginBottom: 6,
    color: "#aaa",
    fontSize: 13,
    fontWeight: 500,
};

const inputStyle = {
    width: "100%",
    padding: "10px 12px",
    borderRadius: 8,
    border: "1px solid #2e2e4e",
    background: "#0f3460",
    color: "#e0e0e0",
    fontSize: 15,
    marginBottom: 18,
    boxSizing: "border-box",
    outline: "none",
};

const buttonStyle = {
    width: "100%",
    padding: "12px",
    borderRadius: 8,
    border: "none",
    background: "#4f8ef7",
    color: "#fff",
    fontSize: 16,
    fontWeight: 600,
    cursor: "pointer",
    marginTop: 4,
};
