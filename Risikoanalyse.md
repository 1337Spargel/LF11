## 1. Einordnung und Methodik

Auf Basis der Schutzbedarfsanalyse weisen insbesondere die Administrationsdaten und die Datenbankintegrität einen hohen bis sehr hohen Schutzbedarf auf. Um diesen Anforderungen gerecht zu werden, wird im Folgenden eine vereinfachte Risikoanalyse gemäß BSI-Standard 200-3 durchgeführt.

### Vorgehensweise

Die Bewertung der Risiken erfolgt qualitativ anhand der Faktoren Eintrittswahrscheinlichkeit und Schadensausmaß.

* **Eintrittswahrscheinlichkeit:** Wie plausibel ist das Eintreten des Szenarios im täglichen Betrieb?
* **Schadensausmaß:** Welche Auswirkungen hätte das Ereignis auf die Organisation (finanziell, rechtlich, operativ)?

---

## 2. Analyse der identifizierten Risiken

### 2.1 Risiko 1: Manipulation und Angriff von Benutzerkonten

| Merkmal | Beschreibung |
| --- | --- |
| **Gefährdung** | Unbefugter Zugriff durch schwache Passwörter oder Credential Stuffing. |
| **Schutzobjekt** | Benutzerkonten, Buchungsdaten. |
| **Eintrittswahrscheinlichkeit** | Mittel |
| **Schadensausmaß** | Mittel bis Hoch (Verstoß gegen DSGVO-Vorgaben). |
| **Risikoeinschätzung** | **Mittleres Risiko** |
| **Risikobehandlung** | Umsetzung von Passwort-Mindestanforderungen, Kontosperrung bei Fehlversuchen und Sensibilisierung der Nutzenden. |

### 2.2 Risiko 2: Manipulation von Buchungs- und Datenbankinhalten

| Merkmal | Beschreibung |
| --- | --- |
| **Gefährdung** | Fehlerhafte Software-Logik oder gezielte Manipulation von Datenbankeinträgen. |
| **Schutzobjekt** | Datenbank, Buchungslogik. |
| **Eintrittswahrscheinlichkeit** | Niedrig bis Mittel |
| **Schadensausmaß** | Hoch (Prozessstörungen, Vertrauensverlust in das Tool). |
| **Risikoeinschätzung** | **Mittleres bis hohes Risiko** |
| **Risikobehandlung** | Validierung aller Eingaben (Server-side), Einsatz von Datenbank-Integritätsprüfung und regelmäßige Daten-Backups. |

### 2.3 Risiko 3: Missbrauch administrativer Privilegien

| Merkmal | Beschreibung |
| --- | --- |
| **Gefährdung** | Übernahme eines Administrator-Accounts oder Fehlbedienung mit weitreichenden Folgen. |
| **Schutzobjekt** | Gesamtsystem, Konfigurationsdaten. |
| **Eintrittswahrscheinlichkeit** | Niedrig |
| **Schadensausmaß** | Sehr Hoch (Vollständige Kompromittierung des Systems). |
| **Risikoeinschätzung** | **Hohes Risiko** |
| **Risikobehandlung** | Strenge Limitierung der Admin-Zahl, Trennung von Benutzer- und Admin-Accounts, Protokollierung administrativer Änderungen (Audit Log). |

### 2.4 Risiko 4: Ungeplanter Systemausfall (Verfügbarkeit)

| Merkmal | Beschreibung |
| --- | --- |
| **Gefährdung** | Technische Defekte am Webserver oder Datenbankfehler. |
| **Schutzobjekt** | Webserver, Datenbankserver. |
| **Eintrittswahrscheinlichkeit** | Mittel |
| **Schadensausmaß** | Mittel (Einschränkung der Arbeitsplatzplanung). |
| **Risikoeinschätzung** | **Mittleres Risiko** |
| **Risikobehandlung** | Monitoring der Dienste, definierter Wiederherstellungsplan (Disaster Recovery) und regelmäßige Wartungsfenster. |

### 2.5 Risiko 5: Mitlesen/Manipulation der Datenübertragung

| Merkmal | Beschreibung |
| --- | --- |
| **Gefährdung** | Man-in-the-Middle-Angriffe in (unverschlüsselten) Netzwerkumgebungen. |
| **Schutzobjekt** | Kommunikation (HTTPS), Session-Daten. |
| **Eintrittswahrscheinlichkeit** | Niedrig |
| **Schadensausmaß** | Hoch (Abgriff von aktiven Sessions oder Passwörtern). |
| **Risikoeinschätzung** | **Mittleres Risiko** |
| **Risikobehandlung** | Erzwungene TLS-Verschlüsselung (HSTS) und Einsatz aktueller Verschlüsselungs-Suites. |

---

## 3. Gesamteinschätzung und Restrisikobewertung

Die Risikoanalyse zeigt, dass die Mehrheit der potenziellen Gefährdungen durch die konsequente Umsetzung der BSI-Grundschutz-Standardmaßnahmen (Bausteine APP, INF, SYS) auf ein akzeptables Maß reduziert werden kann.

Besonderes Augenmerk liegt auf dem Administrationsbereich. Durch die Kombination aus technischer Protokollierung und organisatorischer Trennung der Rollen wird das verbleibende Restrisiko als vertretbar eingestuft. Da das System intern genutzt wird und keine geschäftskritischen Transaktionen (z. B. Zahlungsverkehr) abwickelt, sind keine darüber hinausgehenden Hochsicherheitsmaßnahmen erforderlich.

## 4. Fazit

Das Arbeitsplatzbuchungstool weist ein ausgewogenes Risikoprofil auf. Die identifizierten Risiken sind mit gängigen IT-Sicherheitspraktiken beherrschbar. Unter der Voraussetzung, dass die empfohlenen Behandlungsmaßnahmen (insb. Backup, Verschlüsselung und Rollenkonzept) umgesetzt werden, bestehen keine Einwände gegen den produktiven Betrieb des Systems.

---
