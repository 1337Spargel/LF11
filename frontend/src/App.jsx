import { Routes, Route, Navigate, useNavigate } from "react-router-dom";
import { useAuth } from "./context/AuthContext";
import BuildingsPage from "./pages/BuildingsPage.jsx";
import LoginPage from "./pages/LoginPage.jsx";
import RegisterPage from "./pages/RegisterPage.jsx";

function ProtectedRoute({ children }) {
    const { isAuthenticated } = useAuth();
    return isAuthenticated ? children : <Navigate to="/login" replace />;
}

function Header() {
    const { user, logout } = useAuth();
    const navigate = useNavigate();

    function handleLogout() {
        logout();
        navigate("/login");
    }

    return (
        <div style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            padding: "14px 32px",
            background: "#16213e",
            borderBottom: "1px solid #2e2e4e",
            boxShadow: "0 2px 12px rgba(0,0,0,0.3)",
        }}>
            <span style={{ color: "#e0e0e0", fontWeight: 700, fontSize: 17, letterSpacing: "0.01em" }}>
                🏢 Bürobuchungssystem
            </span>
            <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
                <span style={{ color: "#aaa", fontSize: 14 }}>
                    Hallo, <strong style={{ color: "#c0c0c0" }}>{user?.name}</strong>
                </span>
                <button
                    onClick={handleLogout}
                    style={{
                        padding: "7px 16px",
                        borderRadius: 7,
                        border: "1px solid #4f8ef7",
                        background: "transparent",
                        color: "#4f8ef7",
                        fontSize: 14,
                        cursor: "pointer",
                        transition: "background 0.18s, color 0.18s",
                    }}
                    onMouseEnter={e => {
                        e.currentTarget.style.background = "#4f8ef7";
                        e.currentTarget.style.color = "#fff";
                    }}
                    onMouseLeave={e => {
                        e.currentTarget.style.background = "transparent";
                        e.currentTarget.style.color = "#4f8ef7";
                    }}
                >
                    Abmelden
                </button>
            </div>
        </div>
    );
}

export default function App() {
    const { isAuthenticated } = useAuth();

    return (
        <>
            {isAuthenticated && <Header />}
            <Routes>
                <Route path="/login" element={<LoginPage />} />
                <Route path="/register" element={<RegisterPage />} />
                <Route path="/" element={
                    <ProtectedRoute>
                        <BuildingsPage />
                    </ProtectedRoute>
                } />
            </Routes>
        </>
    );
}
