import { useParams, useNavigate } from "react-router-dom";

const buildingInfo = {
    "1": {
        name: "Innovation Hub",
        address: "Musterstraße 12, 80331 München",
        floors: [
            { id: "eg", label: "Erdgeschoss (EG)", rooms: 4, description: "Eingang, Lobby & Meetingräume" },
            { id: "1", label: "1. Etage", rooms: 4, description: "Büros & Arbeitsplätze" },
            { id: "2", label: "2. Etage", rooms: 4, description: "Konferenzräume & Teamküche" },
        ],
    },
    "2": {
        name: "Tech Campus B",
        address: "Musterallee 5, 80333 München",
        floors: [],
    },
};

function FloorCard({ buildingId, floor }) {
    const navigate = useNavigate();

    function handleMouseEnter(e) {
        e.currentTarget.style.transform = "translateY(-4px)";
        e.currentTarget.style.boxShadow = "0 12px 32px rgba(79,142,247,0.2)";
        e.currentTarget.style.borderColor = "#4f8ef7";
    }

    function handleMouseLeave(e) {
        e.currentTarget.style.transform = "translateY(0)";
        e.currentTarget.style.boxShadow = "0 4px 16px rgba(0,0,0,0.3)";
        e.currentTarget.style.borderColor = "#2e2e4e";
    }

    return (
        <button
            type="button"
            onClick={() => navigate(`/building/${buildingId}/floor/${floor.id}`)}
            onMouseEnter={handleMouseEnter}
            onMouseLeave={handleMouseLeave}
            style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "space-between",
                padding: "20px 24px",
                border: "1px solid #2e2e4e",
                borderRadius: 14,
                cursor: "pointer",
                background: "#16213e",
                boxShadow: "0 4px 16px rgba(0,0,0,0.3)",
                transition: "transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease",
                textAlign: "left",
                width: "100%",
            }}
        >
            <div style={{ display: "flex", alignItems: "center", gap: 20 }}>
                <div style={{
                    width: 52,
                    height: 52,
                    borderRadius: 10,
                    background: "#0f3460",
                    border: "1px solid #2e2e4e",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    fontSize: 22,
                    flexShrink: 0,
                }}>
                    🏢
                </div>
                <div>
                    <div style={{ color: "#e0e0e0", fontWeight: 600, fontSize: 15 }}>
                        {floor.label}
                    </div>
                    <div style={{ color: "#888", fontSize: 13, marginTop: 3 }}>
                        {floor.description}
                    </div>
                    <div style={{ color: "#4f8ef7", fontSize: 12, marginTop: 4 }}>
                        {floor.rooms} Räume verfügbar
                    </div>
                </div>
            </div>
            <span style={{ color: "#4f8ef7", fontSize: 20, lineHeight: 1, flexShrink: 0 }}>→</span>
        </button>
    );
}

export default function FloorsPage() {
    const { buildingId } = useParams();
    const navigate = useNavigate();
    const building = buildingInfo[buildingId];

    return (
        <div style={{
            padding: "40px 24px",
            maxWidth: 1100,
            margin: "0 auto",
            flex: 1,
        }}>
            <button
                type="button"
                onClick={() => navigate("/")}
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
                ← Back to Buildings
            </button>

            <div style={{ marginBottom: 32 }}>
                <h1 style={{ margin: 0, fontSize: 26, color: "#e0e0e0", fontWeight: 700 }}>
                    {building?.name}
                </h1>
                <p style={{ margin: "6px 0 0", fontSize: 14, color: "#888" }}>
                    {building?.address}
                </p>
            </div>

            {building?.floors?.length > 0 ? (
                <div>
                    <h2 style={{ margin: "0 0 20px", fontSize: 18, color: "#c0c0c0", fontWeight: 600 }}>
                        Etage auswählen
                    </h2>
                    <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
                        {building.floors.map((floor) => (
                            <FloorCard key={floor.id} buildingId={buildingId} floor={floor} />
                        ))}
                    </div>
                </div>
            ) : (
                <div style={{
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    justifyContent: "center",
                    padding: "80px 24px",
                    borderRadius: 14,
                    border: "1px solid #2e2e4e",
                    background: "#16213e",
                    boxShadow: "0 4px 16px rgba(0,0,0,0.3)",
                    textAlign: "center",
                }}>
                    <span style={{ fontSize: 48, marginBottom: 16 }}>🚧</span>
                    <h2 style={{ margin: 0, fontSize: 22, color: "#e0e0e0", fontWeight: 700 }}>
                        Coming Soon
                    </h2>
                    <p style={{ margin: "10px 0 0", fontSize: 14, color: "#888", maxWidth: 320 }}>
                        The floor plan and room bookings for this building are not yet available.
                    </p>
                </div>
            )}
        </div>
    );
}
