---
layout: post
title:  Advent of Datascience 2018
date:   2018-11-29 13:32:20 +0300
description: # Add post description (optional)
img: 2018-11-30_advent.jpg # Add image post (optional)
tags: [Blog, Data]
author: Franz Krekeler
---
Automatisiertes Buchungssystem in Google Sheets

In diesem Case habe ich meinen Rechnungsprozess automatisiert.
Die Funktionen von der Google App Script Engine in JavaScript machten es möglich.
Folgende Funktionen habe ich implemntiert:
- Rechnungen nach Erstellung in einem neuen Sheet speichern.
- Uebersicht von allen gestellten Rechnungen.
- Alte Rechnungen laden.
- Umwandlung als PDF. Speichern im Google Drive Ordner.
- Automatischer Versand per Mail.
- Timerfunktion, wenn die Mail erst am nächsten Tag verschickt werden soll.
- Massenversand von allen fertigen Rechnungen.


Buchungsystem in Aktion:

Der Mail-Dialog. An diese Mail wird dann eine Rechnung als PDF verschickt.
![Buchungsystem in Aktion: Hier kommt der Mail-Dialog. An diese Mail wird dann eine Rechnung als PDF verschickt.]({{site.baseurl}}/assets/img/post/buchungssystem1.jpg)

Die Datenbank von gestellten Rechnungen
![Buchungsystem in Aktion: Hier sieht man die Datenbank von gestellten Rechnungen]({{site.baseurl}}/assets/img/post/buchungssystem3.jpg)
Der Code per Google App Script
![Buchungsystem in Aktion: Der Code per Google App Script]({{site.baseurl}}/assets/img/post/buchungssystem4.jpg)
Folgende Möglichkeiten bietet das System.
![Buchungsystem in Aktion: Folgende Möglichkeiten bietet das System.]({{site.baseurl}}/assets/img/post/buchungssystem2.jpg)
So sieht die Mail dann aus, wenn sie verschickt wird
![Buchungsystem in Aktion: So sieht die Rechnung dann aus, wenn sie verschickt wird.]({{site.baseurl}}/assets/img/post/buchungssystem5.jpg)


