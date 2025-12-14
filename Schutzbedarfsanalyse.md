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

## 3. Schutzbedarfsbewertung der Schutzobjekte

### 3.1 Informationen

#### 3.1.1 Benutzerkonten  
*(Name, E-Mail-Adresse, Login-Daten)*

- **Vertraulichkeit: Sehr hoch**  
  Benutzerkonten enthalten Authentifizierungsdaten. Ein unbefugter Zugriff ermöglicht Identitätsmissbrauch und potenziell den vollständigen Zugriff auf das System.

- **Integrität: Hoch**  
  Manipulationen an Benutzerkonten (z. B. Rollenänderungen) können unbefugte Administrationsrechte ermöglichen.

- **Verfügbarkeit: Mittel**  
  Kurzfristige Ausfälle einzelner Benutzerkonten sind tolerierbar, beeinträchtigen jedoch die Nutzbarkeit.

---

#### 3.1.2 Buchungsdaten  
*(Datum, Arbeitsplatz, Benutzerzuordnung)*

- **Vertraulichkeit: Mittel**  
  Buchungsdaten ermöglichen Rückschlüsse auf Anwesenheitszeiten von Mitarbeitenden, gelten jedoch nicht als hochsensible Daten.

- **Integrität: Sehr hoch**  
  Die Korrektheit der Buchungsdaten ist geschäftskritisch. Manipulationen führen zu Doppelbuchungen, Fehlbelegungen und organisatorischem Chaos.

- **Verfügbarkeit: Hoch**  
  Ohne verfügbare Buchungsdaten ist eine Arbeitsplatzplanung nicht möglich.

---

#### 3.1.3 Administrationsdaten

- **Vertraulichkeit: Sehr hoch**  
  Administrationsdaten ermöglichen vollständige Kontrolle über das System. Ein Abfluss hätte gravierende sicherheitsrelevante Folgen.

- **Integrität: Sehr hoch**  
  Veränderungen an Administrationsdaten können das System vollständig kompromittieren.

- **Verfügbarkeit: Mittel**  
  Kurzfristige Nichtverfügbarkeit ist tolerierbar, längere Ausfälle erschweren jedoch den Betrieb erheblich.

---

### 3.2 Anwendungen

#### 3.2.1 Webanwendung (Frontend)

- **Vertraulichkeit: Mittel**  
  Das Frontend stellt personenbezogene Daten dar und verarbeitet Benutzereingaben.

- **Integrität: Hoch**  
  Manipulationen können zu fehlerhaften Buchungen oder Sicherheitslücken führen.

- **Verfügbarkeit: Hoch**  
  Bei Ausfall der Webanwendung ist keine Nutzung des Systems möglich.

---

#### 3.2.2 Serveranwendung (Backend)

- **Vertraulichkeit: Sehr hoch**  
  Das Backend verarbeitet sämtliche sensiblen Daten und Geschäftslogik. Ein Zugriff bedeutet vollständige Kompromittierung.

- **Integrität: Sehr hoch**  
  Manipulationen an der Backend-Logik führen zu falschen Buchungen, Sicherheitslücken oder Datenverlust.

- **Verfügbarkeit: Sehr hoch**  
  Ein Ausfall des Backends legt das gesamte System vollständig lahm.

---

### 3.3 IT-Systeme

#### 3.3.1 Webserver

- **Vertraulichkeit: Mittel**  
  Der Webserver enthält Konfigurationsdaten und Logdateien.

- **Integrität: Hoch**  
  Manipulationen können Schadcode einschleusen oder den Server kompromittieren.

- **Verfügbarkeit: Hoch**  
  Der Webserver ist für den Betrieb der Anwendung zwingend erforderlich.

---

#### 3.3.2 Datenbankserver

- **Vertraulichkeit: Sehr hoch**  
  Die Datenbank enthält sämtliche personenbezogenen und organisatorischen Daten.

- **Integrität: Sehr hoch**  
  Datenmanipulation oder -verlust gefährdet die Zuverlässigkeit und Korrektheit des Systems massiv.

- **Verfügbarkeit: Sehr hoch**  
  Ohne Datenbank ist das System nicht funktionsfähig.

---

### 3.4 Kommunikationsverbindungen

#### 3.4.1 Datenübertragung zwischen Client und Server (HTTPS)

- **Vertraulichkeit: Sehr hoch**  
  Während der Übertragung werden Login- und Buchungsdaten übertragen, deren Abhören zu schweren Datenschutzverletzungen führt.

- **Integrität: Sehr hoch**  
  Manipulierte Übertragungen können zu unbefugten Aktionen oder falschen Buchungen führen.

- **Verfügbarkeit: Mittel**  
  Kurzfristige Verbindungsstörungen sind tolerierbar, längere Ausfälle verhindern die Nutzung des Systems.

---


## 5. Zusammenfassende Schutzbedarfsübersicht

| Schutzobjekt            | Vertraulichkeit | Integrität | Verfügbarkeit |
|-------------------------|-----------------|------------|---------------|
| Benutzerkonten          | Sehr hoch       | Hoch       | Mittel        |
| Buchungsdaten           | Mittel          | Sehr hoch  | Hoch          |
| Administrationsdaten    | Sehr hoch       | Sehr hoch  | Mittel        |
| Webanwendung (Frontend) | Mittel          | Hoch       | Hoch          |
| Serveranwendung (Backend)| Sehr hoch      | Sehr hoch  | Sehr hoch     |
| Webserver               | Mittel          | Hoch       | Hoch          |
| Datenbankserver         | Sehr hoch       | Sehr hoch  | Sehr hoch     |
| Kommunikation (HTTPS)   | Sehr hoch       | Sehr hoch  | Mittel        |


Der Gesamtschutzbedarf des Systems ergibt sich aus dem jeweils höchsten Schutzbedarf der betrachteten Schutzobjekte.


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


