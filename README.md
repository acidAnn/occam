# occam
Remove adjectives from a text to make it more stylistically concise :scissors:

:heart: For keyboardmonkee, redadmiral & schwukas

## setup
```sh
$ python -m venv ./venv
$ python -m spacy download de
$ pip install -r requirements.txt
```

## example
["Sehnsucht" by Joseph von Eichendorff](https://de.wikisource.org/wiki/Sehnsucht_(Eichendorff_II))
```
Sehnsucht.

Es schienen so golden die Sterne,
Am Fenster ich einsam stand
Und hörte aus weiter Ferne
Ein Posthorn im stillen Land.
Das Herz mir im Leib entbrennte,
Da hab’ ich mir heimlich gedacht:
Ach, wer da mitreisen könnte
In der prächtigen Sommernacht!

Zwei junge Gesellen gingen
Vorüber am Bergeshang,
Ich hörte im Wandern sie singen
Die stille Gegend entlang:
Von schwindelnden Felsenschlüften,
Wo die Wälder rauschen so sacht,
Von Quellen, die von den Klüften
Sich stürzen in die Waldesnacht.

Sie sangen von Marmorbildern,
Von Gärten, die über’m Gestein
In dämmernden Lauben verwildern,
Palästen im Mondenschein,
Wo die Mädchen am Fenster lauschen,
Wann der Lauten Klang erwacht,
Und die Brunnen verschlafen rauschen
In der prächtigen Sommernacht. – 
```

ockham version:
```
Sehnsucht.

Es schienen die Sterne,
Am Fenster ich stand
Und hörte aus Ferne
Ein Posthorn im Land.
Das Herz mir im Leib entbrennte,
Da hab ’ ich mir gedacht:
Ach, wer mitreisen könnte
In der Sommernacht!

Zwei Gesellen gingen
Vorüber am Bergeshang,
Ich hörte im Wandern sie 
Die Gegend entlang:
Von Felsenschlüften,
die Wälder rauschen sacht,
Von Quellen, die von den Klüften
Sich stürzen in die Waldesnacht.

Sie sangen von Marmorbildern,
Von Gärten, die über ’m Gestein
In Lauben verwildern,
Palästen im Mondenschein,
die Mädchen am Fenster lauschen,
der Klang erwacht,
Und die Brunnen verschlafen 
In der Sommernacht.–
```
