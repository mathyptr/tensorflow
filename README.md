# Sistema per il riconoscimento di dettagli in opere d’arte


In questo lavoro viene proposta una soluzione per la realizzazione di un’applicazione web che
consenta il riconoscimento di dettagli all’interno di opere d’arte tramite l’ausilio di una webcam e
per lo sviluppo di un intero sistema che permetta l’addestramento di una rete neurale.

Per perseguire questi obiettivi è stata addestrata la rete SSD/MobileNetV2 applicando tecniche di
object detection. In particolare viene effettuato un fine tuning sulla rete in questione al fine di adde-
strarla a riconoscere gli oggetti di interesse.

Sono poi analizzate tutte le fasi del processo di training, per il quale viene utilizzata un’architettura a microservizi implementata tramite l’utilizzo di container Docker.

Successivamente viene esposta una possibile automatizzazione dell’addestramento.

Dopo aver ottenuto il modello personalizzato, è stato realizzato il codice necessario all’implementazione dell’applicativo di cui sono illustrate le sezioni principali e le tecnologie utilizzate.


## Architettura del progetto
Il progetto è volto alla realizzazione di un’applicazione web che consenta il riconoscimento di dettagli all’interno di opere d’arte. Oltre alla sezione accessibile a qualsiasi utente che permette l’utilizzo della propria webcam per inquadrare l’opera di cui si desidera conoscere le informazioni, è presente
anche una sezione privata riservata al personale del museo.
Poiché in quest’ultima è possibile effettuare modifiche importanti alle informazioni delle opere e al contenuto della banca dati, vi si può accedere solo previa autenticazione.
Lo schema nella seguente figura sintetizza l’architettura che è stata sviluppata per effettuare tutte le operazioni implementate.

<img src="img/architettura.png?raw=true" width="720" height="540"> &nbsp;

I container realizzati sono i seguenti:

###  Augmentation
Questo container si occupa della realizzazione del dataset necessario alla creazione del modello applicando tecniche di augmentation a partire dalle immagini originali fornite. Il servizio presente nel container in questione, resterà in attesa di un opportuno comando di avvio da parte del curatore
o di un personale dedicato. A seguito della sua ricezione effettuerà il processo per l’aumento dei dati, al termine del quale provvederà ad attivare il servizio di addestramento presente nel container Tensorflow.

###  Tensorflow
Container che svolge il ruolo centrale di tutta l’architettura contenendo l’ambiente e le risorse necessarie all’addestramento della rete neurale. Il servizio presente al suo interno rimarrà in attesa di essere avviato dal servizio dedicato all’augmentation. Alla ricezione del comando di attivazione si
occuperà di effettuare le varie fasi di addestramento della rete. Dopo aver terminato tali operazioni,avvierà il servizio di conversione presente nel container Tensorflow converter.

###  Tensorflow converter
Tale container si occupa di effettuare la conversione del modello nel formato utilizzato da Tensorflow.js. Il servizio presente si pone in attesa di ricevere un comando di avvio dal microservizio
Tensorflow per eseguire la conversione del modello. Al termine di tale procedura notificherà al microservizo Web-Model la disponibilità del modello.

###  Web Model
Questo container renderà il modello disponibile tramite un servizio REST. Per effettuare tale operazione, è presente un servizio che si occupa di prelevare dal container Tensorflow Converter il modello addestrato e convertito

###  Smartlen-app
All’interno di questo container sono presenti tutte le risorse necessarie alla fruizione della web app.

In ogni container è presente un servizio in ascolto sulla porta 80.
Il container Tensorflow espone anche la porta 81 per interagire con Tensorboard.

Per garantire l'autenticità dei dati prodotti ciascun servizio genera un token JWT, firmandolo e impostando la sua scadenza.
Questo token sarà verificato dal servizio che utilizzerà tali dati (verrà verificata anche la scadenza del token).

Esempio di token JWT
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjc5MzgwNjQuODU5NDY0LCJpYXQiOjE3Mjc4NTE2NjQuODU5NDYsImlzcyI6ImF1Z21lbnRvciIsImNtZCI6InN0YXJ0IiwiYXVkIjoiaHR0cHM6Ly8xNzIuMTAuMC4zL2NnaS1iaW4vc3RhcnRjbWQucHkifQ.BTLBHFmZa1jtqkmK1GAvfIX626xjLdBkkOHboxM6KHY

{'exp': 1727938064.859464, 'iat': 1727851664.85946, 'iss': 'augmentor', 'cmd': 'start', 'aud': 'https://172.10.0.3/cgi-bin/startcmd.py'}


## Contenuto delle cartelle:

_configMathy/config:_
* training.txt: file contenente tutti i comandi necessari per effettuare l'istruzione della rete e per il successivo utilizzo;
* dockerModel.txt: file contenente i comandi utilizzati per configurare la macchina docker che contiene il modello dei dati;
* dockerTensorflow.txt: file contenente i comandi utilizzati per configurare la macchina docker a partire da un'immagine tensorflow che andrà poi ad interrogare il container con il modello dei dati;
* dockerConverter.txt: file contenente i comandi utilizzati per configurare la macchina docker utilizzata per la conversione del dataset nel formato atteso da tensorflowjs.  

_configMathy/dataset:_
* image_filter_augmentation.py: script python per l'elaborazione delle immagini con filtri e augmentation;
* comandi.txt: file contenente i comandi necessari all'esecuzione dello script python (con i vari parametri per utilizzare filtri o augmentation);
* image: cartella contenente alcuni esempi di immagini generate tramite lo script a partire dall'immagine di un dipinto.  



_docker:_ 

Cartella contente i docker file dei container utilizzati (Augmentation,Tensorflow,Tensorflow converter,Web-model,Smartlen-app)

_models:_

Cartella contenente i repository dei modelli TensorFlow

_script:_

Cartella contente i vari script utilizzati dai container Augmentation,Tensorflow,Tensorflow converter,Web-model.
Occore configurare ciascun servizio modificando il file config.py in modo che possa comunicare con il servizio che lo precede e con quello che lo segue.

In particolare:

### Container Augmentation:

 il servizio presente in questo container scaricherà le immagini e il file coco dal servizio Smartlen-app e per far questo dovrà essere configurato il parametro "smartlens_srv" (smartlens_srv='http://Smartlen-IP-ADDRESS/'). Al termine dell'elaborazione lo stesso servizio dovrà informare il container Tensorflow e per far questo dovrà essere configurato il parametro "tensorflow_srv" (tensorflow_srv='http://TENSORFLOW_SRV-IP-ADDRESS/')

### Container Tensorflow:

 il servizio presente in questo container scaricherà le immagini e i file di training e test dal servizio Augmentation e per far questo dovrà essere configurato il parametro "Augmentation_srv" (augmentation_srv='http://AUGMENTATION_SRV-IP-ADDRESS/'). Al termine dell'esportazione questo servizio dovrà informare il container Converter e per far questo dovrà essere configurato il parametro "converter_srv" (converter_srv='http://CONVERTER_SRV-IP-ADDRESS/')

### Container Converter:

 il servizio presente in questo container scaricherà il modello dal servizio Tensorflow e per far questo dovrà essere configurato il parametro "tensorflow_srv" (tensorflow_srv='http://TENSORFLOW_SRV-IP-ADDRESS/' ). Al termine della conversione dovrà informare il container WebModel e per far questo dovrà essere configurato il parametro "webmodel_srv" (webmodel_srv='http://WEBMODEL_SRV-IP-ADDRESS/')

### Container WebModel:

 il servizio presente in questo container scaricherà il modello dal servizio Converter e per far questo dovrà essere configurato il parametro "converter_srv" (converter_srv='http://TENSORFLOW_SRV-IP-ADDRESS/).

Sempre nel file config.py di ciscun container dovrà essere inserita la chiave privata (mysecret) utilizzata per firmare il token JWT.

