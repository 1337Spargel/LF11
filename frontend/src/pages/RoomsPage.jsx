import { useParams, useNavigate } from "react-router-dom";
import officeImg from "../assets/office.png";

const buildingInfo = {
    "1": { name: "Innovation Hub" },
    "2": { name: "Tech Campus B" },
};

const floorInfo = {
    "eg": { label: "Erdgeschoss (EG)" },
    "1":  { label: "1. Etage" },
    "2":  { label: "2. Etage" },
};

export default function RoomsPage() {
    const { buildingId, floorId } = useParams();
    const navigate = useNavigate();

    const building = buildingInfo[buildingId];
    const floor = floorInfo[floorId];

    return (
        <div style={{
            padding: "40px 24px",
            maxWidth: 1100,
            margin: "0 auto",
            flex: 1,
        }}>
            <button
                type="button"
                onClick={() => navigate(`/building/${buildingId}`)}
                style={{
                    display: "inline-flex",
                    alignItems: "center",
                    gap: 6,
                    marginBottom: 32,
                    background: "transparent",
                    border: "none",
                    color: "#4f8ef7",
                    fontSize: 14,
                    cursor: "pointer",
                    padding: 0,
                }}
            >
                ← Back to Floors
            </button>

            <div style={{ marginBottom: 32 }}>
                <h1 style={{ margin: 0, fontSize: 26, color: "#e0e0e0", fontWeight: 700 }}>
                    {building?.name} – {floor?.label}
                </h1>
                <p style={{ margin: "6px 0 0", fontSize: 14, color: "#888" }}>
                    Verfügbare Räume auf dieser Etage
                </p>
            </div>

            <div>
                <h2 style={{ margin: "0 0 20px", fontSize: 18, color: "#c0c0c0", fontWeight: 600 }}>
                    Raumübersicht
                </h2>
                <div style={{
                    borderRadius: 14,
                    overflow: "hidden",
                    border: "1px solid #2e2e4e",
                    boxShadow: "0 4px 16px rgba(0,0,0,0.3)",
                    background: "#16213e",
                }}>
                    <img
                        src={officeImg}
                        alt={`Raumübersicht – ${building?.name} ${floor?.label}`}
                        style={{
                            width: "100%",
                            display: "block",
                            objectFit: "contain",
                        }}
                    />
                </div>
            </div>
        </div>
    );
}
