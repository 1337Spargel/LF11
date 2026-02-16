import { Routes, Route } from "react-router-dom";
import BuildingsPage from "./pages/BuildingsPage.jsx";

export default function App() {
    return (
        <Routes>
            <Route path="/" element={<BuildingsPage />} />
        </Routes>
    );
}
