# BigDataAssignment-2022

Big Data analitics course assignment

## Tasks

BKK3 (egyelőre magyarul, TODO: lefordítani)

### Téma

Az I épületből este 10-kor, tömegközlekedéssel elérhető "kocsmák" (i.e., Google Maps találat erre a keresésre) elemzése

### Adatbeszerzés

https://openmobilitydata.org/p/bkk/42 és pl. Google Places API

### Adatelőkészítés és szűkítés

A Google Places API (a free változat elég kell, hogy legyen) talán a fő kihívás, egyenértékes megoldást elfogadok

### Leskálázás méretben "small" datára

Valószínűleg nem szükséges

### EDA fókusz

Az I épület 10 perces sétatávolságában megállóval rendelkező éjszakai járatok alapvető jellemzői (javasolt:
pandas_profiling vagy BambooLib)

### Big Data vizualizáció

Datashader alapú (lehet HoloViz-be integrálva) interaktív, Budapest-térkép alapú heatmap, mely az I épületből este 10-es
indulással, átszállás nélkül való utazási időben vett távolságát mutatja a "celláknak" (cellán belül átlagolással, ha
több opció is van). Természetesen vannak a városnak olyan részei, ahova átszállás nélkül nem lehet eljutni az
egyetemről!

### Elemzési feladat

Algoritmus azon megállók megtalálására, ahova 45 perc alatt, max k átszállással el lehet jutni az I épületből este 10-es
indulással. (Demonstráció elég k=1 vagy 2-re.)

## Doc

* [GTFS](doc/gtfs.md)