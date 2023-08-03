# 🚗 Gebrauchtwagen-Preisvorhersage: Revving into the Future 🏁

## Beschreibung

Dieses Repository enthält ein Machine Learning (ML) Projekt, das sich auf die Preisvorhersage von Gebrauchtwagen konzentriert. Das Ziel des Projekts ist es, anhand verschiedener Merkmale und Eigenschaften von Gebrauchtwagen, wie Marke, Modell, Alter, Kilometerstand, Kraftstofftyp, Motorleistung und weiteren, den Verkaufspreis des Fahrzeugs vorherzusagen.

## Datensatz

Das ML-Projekt verwendet den folgenden Datensatz:

[Used Car Dataset](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes)

Der Datensatz enthält umfangreiche Informationen über Gebrauchtwagen von Ford, Mercedes, etc.. Er umfasst verschiedene Merkmale und Eigenschaften der Fahrzeuge sowie die dazugehörigen Verkaufspreise. Die Daten werden für das Training und die Bewertung der ML-Modelle verwendet.

## Projektstruktur

Die Projektstruktur umfasst die folgenden Dateien und Verzeichnisse:

- `daten/`: In diesem Verzeichnis sind die Datensätze gespeichert, die für das Training und die Bewertung der ML-Modelle verwendet werden.

- `notebooks/`: Hier befinden sich Jupyter Notebooks, die die Datenanalyse, das Feature-Engineering, das Modelltraining und die Bewertung der Modelle enthalten.

- `modelle/`: In diesem Ordner werden die trainierten ML-Modelle gespeichert, die für die Preisvorhersage genutzt werden.

- `requirements.txt`: Eine Datei, die alle notwendigen Python-Bibliotheken und -Versionen enthält, die für das Projekt benötigt werden.

## Vorgehen

Das ML-Projekt zur Preisvorhersage von Gebrauchtwagen umfasst folgende Schritte:

1. Datenerfassung: Sammeln von Gebrauchtwagendaten aus [Used Car Dataset](https://www.kaggle.com/datasets/adityadesai13/used-car-dataset-ford-and-mercedes).

2. Datenbereinigung: Bereinigung der Daten, Entfernen von Duplikaten und Anpassen von fehlenden oder ungültigen Werten.

3. Datenanalyse: Untersuchung der Daten, um Muster, Korrelationen und wichtige Merkmale zu erkennen.

4. Feature-Engineering: Auswahl und Extrahierung relevanter Merkmale für das ML-Modell.

5. Modellauswahl: Auswahl eines geeigneten ML-Algorithmus oder einer Kombination verschiedener Modelle.

6. Modelltraining: Training des ausgewählten Modells mit den bereinigten und vorverarbeiteten Daten.

7. Modellbewertung: Evaluierung der Modellleistung anhand geeigneter Metriken und Tests.

8. Modelloptimierung: Feinabstimmung des Modells, um die Vorhersagegenauigkeit zu verbessern.

9. Preisvorhersage: Verwendung des trainierten Modells, um den Preis für neue Gebrauchtwagen vorherzusagen.

## Streamlit-Anwendung

Dieses Projekt enthält auch eine Streamlit-Anwendung, mit der Sie die Gebrauchtwagen-Preisvorhersage in einer interaktiven Benutzeroberfläche erkunden können. 

Um die Streamlit-Anwendung lokal auszuführen, folgen Sie diesen Schritten:

1. Stellen Sie sicher, dass Sie alle Anforderungen aus der `requirements.txt` installiert haben.
2. Navigieren Sie zum Projektverzeichnis und führen Sie den folgenden Befehl aus:

   ```bash
   streamlit run ml_model.py
   ![Vorschau](.streamlit/auszug.png)

