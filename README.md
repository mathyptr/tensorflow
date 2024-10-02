## Contenuto delle cartelle:



_configMathy/config:_
* training.txt: file contenente tutti i comandi necessari per effettuare l'istruzione della rete (da me effettuata su Colab) e per il successivo utilizzo;
* dockerModel.txt: file contenente i comandi utilizzati per configurare la macchina docker che contiene il modello dei dati;
* dockerTensorflow.txt: file contenente i comandi utilizzati per configurare la macchina docker a partire da un'immagine tensorflow che andrà poi ad interrogare il container con il modello dei dati;
* dockerConverter.txt: file contenente i comandi utilizzati per configurare la macchina docker utilizzata per la conversione del dataset nel formato atteso da tensorflowjs.  



_configMathy/dataset:_
* image_filter_augmentation.py: script python per l'elaborazione delle immagini con filtri e augmentation;
* comandi.txt: file contenente i comandi necessari all'esecuzione dello script python (con i vari parametri per utilizzare filtri o augmentation);
* image: cartella contenente alcuni esempi di immagini generate tramite lo script a partire dall'immagine di un dipinto.  



_docker:_ 

Cartella contente i docker file dei container utilizzati (Augmentation,Tensorflow,Tensorflow converter,Web-model,Smartlen-app)


<img src="img/architettura.png?raw=true" width="720" height="540"> &nbsp;



* Augmentation
Questo container si occupa della realizzazione del dataset necessario alla creazione del modello ap-
plicando tecniche di augmentation a partire dalle immagini originali fornite. Il servizio presente
nel container in questione, resterà in attesa di un opportuno comando di avvio da parte del curatore
o di un personale dedicato. A seguito della sua ricezione effettuerà il processo per l’aumento dei
dati, al termine del quale provvederà ad attivare il servizio di addestramento presente nel container
Tensorflow.

* Tensorflow
Container che svolge il ruolo centrale di tutta l’architettura contenendo l’ambiente e le risorse ne-
cessarie all’addestramento della rete neurale. Il servizio presente al suo interno rimarrà in attesa di
essere avviato dal servizio dedicato all’augmentation. Alla ricezione del comando di attivazione si
occuperà di effettuare le varie fasi di addestramento della rete. Dopo aver terminato tali operazioni,
avvierà il servizio di conversione presente nel container Tensorflow converter.

* Tensorflow converter
Tale container si occupa di effettuare la conversione del modello nel formato utilizzato da Tensor-
flow.js. Il servizio presente si pone in attesa di ricevere un comando di avvio dal microservizio
Tensorflow per eseguire la conversione del modello. Al termine di tale procedura notificherà al mi-
croservizo Web-Model la disponibilità del modello.
Web Model
Questo container renderà il modello disponibile tramite un servizio REST. Per effettuare tale opera-
zione, è presente un servizio che si occupa di prelevare dal container Tensorflow Converter il modello
addestrato e convertito

* Smartlen-app
All’interno di questo container sono presenti tutte le risorse necessarie alla fruizione della web app.

Per garantire l'autenticità dei dati prodotti ciascun servizio genera un token JWT, firmandolo e impostando la sua scadenza.
Questo token sarà verificato dal servizio che utilizzerà tali dati (verrà verificata anche la scadenza del token)

_models:_

Cartella contenente i repository dei modelli TensorFlow

_script:_

Cartella contente i vari script utilizzati dai container Augmentation,Tensorflow,Tensorflow converter,Web-model.
Occore configurare ciascun servizio modificando il file config.py in modo che possa comunicare con il servizio
che lo precede e con quello che lo segue.

Ad esempio il servizio presente nel container Tensorflow scaricherà le immagini e il file coco dal servizio
Augmentation e per far questo deve essere configurato il parametro:
augmentation_srv='http://AUGMENTATION_SRV-IP-ADDRESS/'

Il container Tensorflow al termine del training dovrà informare di ciò il container Converter e per far questo deve
essere configurato il parametro:
converter_srv='http://CONVERTER_SRV-IP-ADDRESS/'

Sempre nel file config.py dovrà essere inserita la chiave privata utilizzata per firmare il token JWT.

