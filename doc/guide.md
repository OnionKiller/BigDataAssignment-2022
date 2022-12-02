# Útmutató a feladatok megoldásához

## Beadás
Az utolsó előadáson rövid (5 perces) előadás, főszabály szerint minden csapattag jelen kell, hogy legyen. Az utolsó hét végéig kérem a megoldás"beadásra" letisztázását. Pótlási héten pótbemutatásra természetesen van lehetőség, de én nagyon boldog szoktam lenni, amikor erre nincs szükség.

## Beadandó
**Alaposan** megkommentelt-dokumentált, önhordó Jupyter notebook, lehetőleg anaconda-project-ként, egy lent megadott Git repoban fejlesztve/"beadva". Mindenképp erősen javasolt a conda használata (pl. anaconda-val telepítve). Természetesen lehet Windows-on is dolgozni, de a sokéves tapasztalat szerint a Linux/OS X sokkal alkalmasabb. Elégtelen lokális erőforrások esetén (főszabály szerint a HF-ek Big Data _jellegűek_, de "beleférnek" helyi erőforrásokba): valamennyi Azure kredit jár minden BME hallgatónak (-> azureforeducation.microsoft.com) és ott a BME Cloud is. A Google Colab csomagtámogatása sokszor kissé esetleges.

## Részfeladatok és technológiai kényszerek

### Adatbeszerzés és előkészítés 
Javasolt a bemeneti adatokat Parquet formátumba átalakítani (amennyiben nem abban van) és azon dolgozni.

### Adatelőkészítés és szűkítés 
A cél mindenhol az, hogy "mikroadatokon" dolgozzunk, így ha adatszűkítésre van szükség, akkor javasolt nem mintavételezni, hanem szisztematikusan részadatkészletet választani. Az előkészítés része egy adatszótár létrehozása is ([Jó gyakorlat](https://help.osf.io/article/217-how-to-make-a-data-dictionary)). Cél: dokumentáljuk és értsük az adatkészlet változóit.

### Adatkezelés 
Mind a dask használatát, mind a beágyazott Spark-ot értékelem, de végső esetben a pandas is OK, a lényeg, hogy mikroadatokon dolgozzatok. Javasolt a Python kernel, de nem kötelező. Javaslom az összeszedett-letisztított adatok hatékonyan betölthető formában (pl. Parquet) kezelését is, a saját érdeketekben is. A dask előnye, hogy (elvileg) jól játszik együtt a datashader-rel és pl. a [dataprep](https://github.com/sfu-db/dataprep)-prel.

### EDA
Az EDA-t tárgyaltuk "sima plotos" és klasszikus (desktop) interaktív megközelítésben is. A minimumkövetelmény egy értelmes "felderítő" logika mentén végiggenerált és in-notebook dokumentált áttekintő plot-sorozat (a peremeloszlásokra és két/kevés változós kereszthatásokra fókuszálva), konstruktív kimenete pedig 1-2 olyan hipotézis, melyre a "modellépítés" részfeladatban reflektáltok is. "Sima" pandas alapon is lehet dolgozni, de javasolt vagy a pandas-profiling, vagy a bamboolib, vagy a dataprep.eda használata. A pandas-profiling csak "kis adatra" megy (in-memory pandas dataframe), a bamboolib elvileg összeköthető Spark-kal, a dataprep pedig működik dask fölött. Ezekről be fogok illeszteni még egy előadást, de simán el lehet indulni in-memory adatok fölött.

### Big Data vizualizáció
Big Data jellegű vizualizáció (i.e., heatmap különböző változatai mikroadatokon). Erősen javasolt: Datashader, illetve HoloVizbe csomagolt Datashader, a pandas lehetőleg fallback legyen. Erről volt előadás, aktívan karbantartott, conda csomagként létező eszközök és az online dokumentáció jó.

### Modellépítés
Optimális esetben Dask ML vagy Spark ML, de ha ezek nem jönnek össze, lehetőség (szűkített) adatkészleten "klasszikus" megoldásokhoz, mint pl. a scikit-learn is nyúlni. Az eredmények interpretálása és minőség-értékelése (amennyiben ennek van értelme) követelmény.