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

## 4. Schutzbedarfsbewertung der Schutzobjekte

### 4.1 Informationen

#### 4.1.1 Benutzerkonten  
*(Name, E-Mail-Adresse, Login-Daten)*

- **Vertraulichkeit:  Hoch**  
  Benutzerkonten enthalten personenbezogene Daten sowie Zugangsinformationen. Ein unbefugter Zugriff kann zu Missbrauch einzelner Nutzerkonten und unberechtigten Buchungen führen.

- **Integrität: Hoch**  
  Veränderungen an Benutzerkonten (z. B. Rollen oder Zuordnungen) können die ordnungsgemäße Nutzung des Systems beeinträchtigen.

- **Verfügbarkeit: Normal**  
  Der temporäre Ausfall einzelner Benutzerkonten ist organisatorisch handhabbar.

---

#### 4.1.2 Buchungsdaten  
*(Datum, Arbeitsplatz, Benutzerzuordnung)*

- **Vertraulichkeit: Normal**  
  Buchungsdaten ermöglichen Rückschlüsse auf Anwesenheitszeiten von Mitarbeitenden, gelten jedoch nicht als hochsensible Daten.

- **Integrität: Hoch**  
  Fehlerhafte oder manipulierte Buchungsdaten können zu Fehlbelegungen und organisatorischen Problemen führen.

- **Verfügbarkeit: Hoch**  
  Ohne verfügbare Buchungsdaten ist eine Arbeitsplatzplanung erschwert.

---

#### 4.1.3 Administrationsdaten

- **Vertraulichkeit: Sehr hoch**  
  Administrationsdaten ermöglichen Änderungen an Systemkonfigurationen und Nutzerrechten.

- **Integrität: Sehr hoch**  
  Unbefugte Änderungen können die korrekte Funktionsweise des Systems beeinträchtigen.

- **Verfügbarkeit: Normal**  
  Kurzfristige Einschränkungen sind organisatorisch überbrückbar.

---

### 4.2 Anwendungen

#### 4.2.1 Webanwendung 

- **Vertraulichkeit: Normal**  
  Das Frontend stellt personenbezogene Daten dar und verarbeitet Benutzereingaben.

- **Integrität: Hoch**  
  Manipulationen können zu fehlerhaften Buchungen oder Sicherheitslücken führen.

- **Verfügbarkeit: Hoch**  
  Bei Ausfall der Webanwendung ist keine Nutzung des Systems möglich.

---

#### 4.2.2 Serveranwendung 

- **Vertraulichkeit: Hoch**  
  Das Backend verarbeitet zentrale Anwendungslogik und Zugriff auf gespeicherte Daten.

- **Integrität: Sehr hoch**  
  Fehler oder Manipulationen wirken sich direkt auf Buchungen und Systemverhalten aus.

- **Verfügbarkeit: Hoch**  
  Ein Ausfall führt zu einer temporären Nichtnutzbarkeit des Systems.

---

### 4.3 IT-Systeme

#### 4.3.1 Webserver

- **Vertraulichkeit: Normal**  
  Der Webserver enthält Konfigurationsdaten und Logdateien.

- **Integrität: Hoch**  
  Manipulationen können Schadcode einschleusen oder den Server kompromittieren.

- **Verfügbarkeit: Hoch**  
  Der Webserver ist für den Betrieb der Anwendung zwingend erforderlich.

---

#### 4.3.2 Datenbankserver

- **Vertraulichkeit: Hoch**  
  Speicherung personenbezogener und organisatorischer Daten.

- **Integrität: Sehr hoch**  
  Datenverluste oder inkonsistente Daten beeinträchtigen die Zuverlässigkeit des Systems erheblich.

- **Verfügbarkeit: Hoch**  
  Ohne Datenbank ist der Betrieb eingeschränkt möglich.

---

### 4.4 Kommunikationsverbindungen

#### 4.4.1 Datenübertragung zwischen Client und Server 

- **Vertraulichkeit: Hoch**  
Während der Übertragung werden Anmelde- und Buchungsdaten verarbeitet.

- **Integrität: Hoch**  
  Manipulationen könnten zu fehlerhaften Buchungen führen.

- **Verfügbarkeit: Normal**  
 Kurzfristige Störungen sind tolerierbar.

---


## 5. Zusammenfassende Schutzbedarfsübersicht

| Schutzobjekt            | Vertraulichkeit | Integrität | Verfügbarkeit |
|-------------------------|-----------------|------------|---------------|
| Benutzerkonten          | Hoch            | Hoch       | Normal        |
| Buchungsdaten           | Normal          | Hoch       | Hoch          |
| Administrationsdaten    | Sehr hoch       | Sehr hoch  | Normal        |
| Webanwendung (Frontend) | Normal          | Hoch       | Hoch          |
| Serveranwendung (Backend)| Hoch           | Hoch       | Hoch          |
| Webserver               | Normal          | Hoch       | Hoch          |
| Datenbankserver         | Hoch            | Sehr hoch  | Hoch          |
| Kommunikation (HTTPS)   | Hoch            | Hoch       | Normal        |


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


