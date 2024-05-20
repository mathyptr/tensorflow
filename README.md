## Contenuto delle cartelle:

_configMathy/config:_
* training.txt: file contenente tutti i comandi necessari per effettuare l'istruzione della rete (da me effettuata su Colab) e per il successivo utilizzo.
* dockerModel.txt: file contenente i comandi utilizzati per configurare la macchina docker relativa al modello dei dati;
* dockerTensorflow.txt: file contenente i comandi utilizzati per configurare la macchina docker a partire da un'immagine tensorflow che andrà poi ad interrogare il container con il modello dei dati;
* dockerConverter.txt: file contenente i comandi utilizzati per configurare la macchina docker utilizzata per la conversione del dataset nel formato atteso da tensorflowjs.

_configMathy/dataset:_
* image_filter_augmentation.py: script python per l'elaborazione delle immagini con filtri e augmentation;
* comandi.txt: file contenente i comandi necessari all'esecuzione dello script python (con i vari parametri per utilizzare filtri o augmentation);
* image: cartella contenente alcuni esempi di immagini generate tramite lo script a partire dall'immagine di un dipinto.

_kangaroodataset:_
* Cartella contente il dataset necessario al riconoscimento dei canguri

_nella cartella principale sono presenti altri file;_
* trainingAndValidate.py: script utilizzato dopo il training della rete come verifica di correttezza 
* labelmap.pbtxt: file utilizzato durante la fase di addestramento 
* Dockerfile: immagine docker per effettuare l'addestramento della rete. Deve poi essere eseguito lo script configTensor.sh (problemi durante il tentativo di installazione dell'ultima versione di python)