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
            padding: "12px 24px",
            background: "#16213e",
            borderBottom: "1px solid #2e2e4e",
        }}>
            <span style={{ color: "#e0e0e0", fontWeight: 600, fontSize: 16 }}>
                Bürobuchungssystem
            </span>
            <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
                <span style={{ color: "#aaa", fontSize: 14 }}>
                    {user?.name}
                </span>
                <button
                    onClick={handleLogout}
                    style={{
                        padding: "6px 14px",
                        borderRadius: 6,
                        border: "1px solid #4f8ef7",
                        background: "transparent",
                        color: "#4f8ef7",
                        fontSize: 14,
                        cursor: "pointer",
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
