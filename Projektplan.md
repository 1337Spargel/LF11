# PROJEKTBESCHREIBUNG – BÜROBUCHUNGSSYSTEM

Das System besteht aus **Frontend**, **Backend**, **API-Schnittstelle** und **Datenpersistenz**.  
Frontend und Backend werden parallel entwickelt, die API dient als verbindender Vertrag, und SQLite sorgt für die dauerhafte Speicherung aller Daten.

---

## Frontend – React und Tailwind CSS

Das Frontend wird mit **React** umgesetzt und verwendet **Tailwind CSS** für Layout und Gestaltung.  
Die Benutzeroberfläche folgt dem **Atomic-Design-Prinzip**, bei dem UI-Elemente von kleinsten Bausteinen über kombinierte Strukturen bis hin zu vollständigen Seiten aufgebaut werden.

### Navigation
Die hierarchische Navigation ermöglicht dem Nutzer:
- von der Gebäudeübersicht
- über die Etagenübersicht
- bis in einzelne Räume

Zunächst wird mit **statischen Beispieldaten** gearbeitet, um:
- Navigation
- Darstellung von Raumplänen
- Anzeige von Sitzplatzstatus

zu testen.

Erst nach Fertigstellung der Grundstruktur werden die Daten durch **API-Aufrufe** ersetzt. Dadurch kann das Frontend unabhängig vom Backend parallel entwickelt und getestet werden.

### Architekturprinzip

Die UI-Komponenten sind bewusst **logikfrei**.

Geschäftslogik wie:
- Prüfen von Sitzplatzverfügbarkeit
- Buchen von Plätzen

wird über **Services und Hooks** implementiert.

Vorteile:
- Hohe Wiederverwendbarkeit
- Gute Testbarkeit
- Klare Trennung von Darstellung und Logik

---

## Backend – Python

Das Backend wird in **Python** umgesetzt und folgt einer klaren **Schichtenarchitektur**:

- **API-Schicht** → Kommunikation mit dem Frontend
- **Service-Layer** → Geschäftslogik
- **Repository-Layer** → Datenzugriff auf SQLite

### Geschäftslogik

Umfasst:
- Prüfung der Verfügbarkeit von Arbeitsplätzen
- Regeln für Buchungen und Stornierungen
- Kontrolle der Benutzerberechtigungen **(rollenbasiert mittels RBAC)**

### Repository-Layer

- Zugriff auf SQLite **über ORM bzw. parametrisierte Queries**
- Verwaltung von Relationen
- Verwendung von Constraints

Beispiel:
- Verhindern von Doppelbuchungen am selben Tag

Die Logik wird zunächst mit **Test- oder Dummy-Daten** entwickelt, sodass Backend und Frontend unabhängig voneinander funktionsfähig sind.

---

## API-Schnittstelle

Die API definiert alle Endpunkte zur Verbindung von Frontend und Backend.

### Zentrale Funktionen

- Laden von Gebäuden
- Laden von Etagen
- Laden von Räumen
- Abfrage des Belegungsstatus
- Erstellen von Buchungen
- Löschen von Buchungen

Die Kommunikation erfolgt über **JSON** **und wird mittels Swagger/OpenAPI dokumentiert**.

### Vorteil

Die API ermöglicht eine **parallele Entwicklung**, da:
- das Frontend definierte Endpunkte nutzen kann
- ohne auf die vollständige Backend-Implementierung warten zu müssen

Später erfolgt die gemeinsame Integration und Schnittstellentestung.

---

## Datenpersistenz – SQLite

SQLite dient als zentrale Datenbank.

Gespeicherte Daten:
- Gebäude
- Etagen
- Räume
- Sitzplätze
- Buchungen
- Nutzer

### Sicherstellung fachlicher Regeln

- Relationen
- Constraints
- Verhinderung von Doppelbuchungen

**Zur Gewährleistung von Integrität und Verfügbarkeit werden regelmäßige automatisierte Backups der SQLite-Datenbank durchgeführt und Wiederherstellungstests eingeplant.**

Der Repository-Layer kapselt den Datenzugriff, sodass Änderungen an der Datenbankstruktur keine Auswirkungen auf Geschäftslogik oder API haben.

---

## Entwicklungs- und Teststrategie

Frontend und Backend werden zunächst **parallel entwickelt und unabhängig getestet**.

### Frontend

- Test der Navigation
- UI-Validierung
- Interaktionen mit Mock-Daten

### Backend

- Validierung des Service-Layers
- Tests des Repository-Layers
- Isolierte Prüfung der Geschäftslogik
- **Überprüfung der Authentifizierungs- und Autorisierungslogik (JWT/RBAC)**
- **Test der Audit-Logging-Funktionen**

### Integration

Nach erfolgreicher Testphase:

- Ersetzen der Mock-Daten durch echte API-Aufrufe
- Aktivierung der Authentifizierung **(JWT mit kurzer Token-Laufzeit und sicherem Passwort-Hashing)**
- Persistente Speicherung in SQLite
- **Ausschließliche Nutzung von HTTPS sowie HSTS zur Absicherung der Transportverbindung**

### Ziel

- Schrittweise stabile Entwicklung
- Frühe Fehlererkennung
- Nahtlose Zusammenarbeit von Frontend und Backend  