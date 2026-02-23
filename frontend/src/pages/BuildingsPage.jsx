import buildingImg from "../assets/building.png";

const buildings = [
    { id: "b1", name: "Gebäude A", img: buildingImg },
    { id: "b2", name: "Gebäude B", img: buildingImg },
];

export default function BuildingsPage() {
    return (
        <div style={{
            padding: "40px 24px",
            maxWidth: 1100,
            margin: "0 auto",
            flex: 1,
        }}>
            <div style={{ textAlign: "center", marginBottom: 40 }}>
                <h1 style={{
                    margin: 0,
                    fontSize: 28,
                    color: "#e0e0e0",
                    fontWeight: 700,
                }}>
                    Gebäude auswählen
                </h1>
                <p style={{ color: "#888", marginTop: 8, fontSize: 14, marginBottom: 0 }}>
                    Wähle ein Gebäude, um die verfügbaren Räume zu sehen
                </p>
            </div>

            <div style={{
                display: "grid",
                gap: 24,
                gridTemplateColumns: "repeat(auto-fit, minmax(280px, 1fr))",
            }}>
                {buildings.map((b) => (
                    <BuildingCard key={b.id} building={b} />
                ))}
            </div>
        </div>
    );
}

function BuildingCard({ building: b }) {
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
            onClick={() => console.log("Geklickt:", b.id)}
            onMouseEnter={handleMouseEnter}
            onMouseLeave={handleMouseLeave}
            style={{
                padding: 0,
                border: "1px solid #2e2e4e",
                borderRadius: 14,
                overflow: "hidden",
                cursor: "pointer",
                background: "#16213e",
                boxShadow: "0 4px 16px rgba(0,0,0,0.3)",
                transition: "transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease",
                textAlign: "left",
            }}
        >
            <img
                src={b.img}
                alt={b.name}
                style={{
                    width: "100%",
                    height: 180,
                    objectFit: "cover",
                    display: "block",
                }}
            />
            <div style={{ padding: "16px 20px", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
                <div>
                    <h3 style={{ margin: 0, color: "#e0e0e0", fontSize: 16, fontWeight: 600 }}>
                        {b.name}
                    </h3>
                    <div style={{ fontSize: 13, color: "#888", marginTop: 4 }}>
                        Etagen & Räume anzeigen
                    </div>
                </div>
                <span style={{ color: "#4f8ef7", fontSize: 20, lineHeight: 1 }}>→</span>
            </div>
        </button>
    );
}
