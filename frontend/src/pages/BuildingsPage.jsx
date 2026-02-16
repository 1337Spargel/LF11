import buildingImg from "../assets/building.png";

const buildings = [
    { id: "b1", name: "Gebäude A", img: buildingImg },
    { id: "b2", name: "Gebäude B", img: buildingImg },
];

export default function BuildingsPage() {
    return (
        <div style={{ padding: 16, maxWidth: 1100, margin: "0 auto" }}>
            <h1 style={{ marginBottom: 16 }}>Gebäude auswählen</h1>

            <div
                style={{
                    display: "grid",
                    gap: 16,
                    gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))",
                }}
            >
                {buildings.map((b) => (
                    <button
                        key={b.id}
                        type="button"
                        onClick={() => console.log("Geklickt:", b.id)}
                        style={{
                            textAlign: "left",
                            padding: 0,
                            border: "1px solid #ddd",
                            borderRadius: 14,
                            overflow: "hidden",
                            cursor: "pointer",
                            background: "white",
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
                        <div style={{ padding: 12 }}>
                            <h3 style={{ margin: 0 }}>{b.name}</h3>
                            <div style={{ fontSize: 14, opacity: 0.8 }}>
                                (Klick testet nur in der Konsole)
                            </div>
                        </div>
                    </button>
                ))}
            </div>
        </div>
    );
}
