# Schutzbedarfsanalyse nach BSI-Grundschutz

## 1. Einordnung und Ziel der Schutzbedarfsanalyse

Diese Schutzbedarfsanalyse wird für das Projekt **„Arbeitsplatzbuchungstool“** durchgeführt. Ziel ist es, den Schutzbedarf der im System verarbeiteten Informationen und IT-Komponenten gemäß den Grundwerten des **BSI IT-Grundschutzes** zu bestimmen:

* **Vertraulichkeit**
* **Integrität**
* **Verfügbarkeit**

Die Analyse dient als Grundlage für die spätere Auswahl geeigneter Sicherheitsmaßnahmen.

---

## 2. Beschreibung des betrachteten Systems

Das Arbeitsplatzbuchungstool ist eine webbasierte Anwendung zur Reservierung von Arbeitsplätzen innerhalb einer Organisation.

### Zentrale Funktionen

* Benutzerregistrierung und Authentifizierung
* Anzeige verfügbarer Arbeitsplätze
* Buchung und Stornierung von Arbeitsplätzen
* Administrationsfunktionen zur Verwaltung von Arbeitsplätzen

Das System wird über einen Webbrowser genutzt und greift auf eine zentrale Datenbank zu.

---

## 3. Schutzobjekte

Im Rahmen der Schutzbedarfsanalyse werden folgende Schutzobjekte betrachtet:

### 3.1 Informationen

* Benutzerkonten (Name, E-Mail-Adresse, Login-Daten)
* Buchungsdaten (Datum, Arbeitsplatz, Benutzerzuordnung)
* Administrationsdaten

### 3.2 Anwendungen

* Webanwendung (Frontend)
* Serveranwendung (Backend)

### 3.3 IT-Systeme

* Webserver
* Datenbankserver

### 3.4 Kommunikationsverbindungen

* Datenübertragung zwischen Client und Server (HTTPS)

---

## 4. Schutzbedarfsfeststellung

Die Schutzbedarfsfeststellung erfolgt getrennt nach den Grundwerten Vertraulichkeit, Integrität und Verfügbarkeit.

### 4.1 Vertraulichkeit

**Schutzbedarf: Mittel**

#### Begründung:

* Verarbeitung personenbezogener Daten (Name, E-Mail-Adresse)
* Rückschlüsse auf Anwesenheitszeiten von Mitarbeitenden möglich
* Missbrauch könnte zu Datenschutzverstößen führen

Ein sehr hoher Schutzbedarf liegt nicht vor, da keine besonders sensiblen Daten (z. B. Gesundheits- oder Finanzdaten) verarbeitet werden.

---

### 4.2 Integrität

**Schutzbedarf: Hoch**

#### Begründung:

* Manipulation von Buchungsdaten kann zu Doppelbuchungen führen
* Falsche oder manipulierte Daten beeinträchtigen den Betriebsablauf
* Vertrauensverlust der Nutzer bei fehlerhaften Buchungen

Die Korrektheit der Daten ist essenziell für die Funktionsfähigkeit des Systems.

---

### 4.3 Verfügbarkeit

**Schutzbedarf: Hoch**

#### Begründung:

* Ausfall des Systems verhindert Arbeitsplatzbuchungen
* Kurzfristige Planungen sind ohne System nicht möglich
* Manuelle Ersatzprozesse sind nur eingeschränkt praktikabel

Ein längerer Ausfall würde den Arbeitsbetrieb deutlich beeinträchtigen.

---

## 5. Zusammenfassende Schutzbedarfsübersicht

| Schutzobjekt  | Vertraulichkeit | Integrität | Verfügbarkeit |
| ------------- | --------------- | ---------- | ------------- |
| Benutzerdaten | Mittel          | Hoch       | Mittel        |
| Buchungsdaten | Mittel          | Hoch       | Hoch          |
| Webanwendung  | Mittel          | Hoch       | Hoch          |
| Datenbank     | Mittel          | Hoch       | Hoch          |
| Gesamtsystem  | **Mittel**      | **Hoch**   | **Hoch**      |

Der Gesamtschutzbedarf des Systems ergibt sich aus dem jeweils höchsten Schutzbedarf der betrachteten Schutzobjekte.

---

## 6. Schadensszenarien

### 6.1 Verletzung der Vertraulichkeit

* Unbefugter Zugriff auf Benutzerdaten
* Offenlegung von Anwesenheitsinformationen

**Mögliche Schäden:**

* Datenschutzverstöße
* Vertrauensverlust der Nutzer

### 6.2 Verletzung der Integrität

* Manipulation oder Löschung von Buchungen
* Erzeugung von Doppelbuchungen

**Mögliche Schäden:**

* Störungen im Arbeitsablauf
* Erhöhter administrativer Aufwand

### 6.3 Verletzung der Verfügbarkeit

* Systemausfall durch technische Fehler
* Überlastung oder Fehlkonfiguration

**Mögliche Schäden:**

* Arbeitsplätze können nicht geplant werden
* Produktivitätsverlust

---

## 7. Abgrenzung und Annahmen

* Das System wird nur innerhalb einer Organisation genutzt
* Kein produktiver Echtbetrieb mit externen Kunden
* Die Analyse dient Ausbildungs- und Lernzwecken

---

## 8. Fazit

Das Arbeitsplatzbuchungstool weist insgesamt einen **mittleren Schutzbedarf hinsichtlich Vertraulichkeit** sowie einen **hohen Schutzbedarf hinsichtlich Integrität und Verfügbarkeit** auf.

Auf Basis dieser Schutzbedarfsanalyse können im nächsten Schritt geeignete technische und organisatorische Maßnahmen nach dem BSI IT-Grundschutz abgeleitet werden.
