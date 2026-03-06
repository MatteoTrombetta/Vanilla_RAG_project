# REMEMBER
Activate .venv everytime with the following code inside the project folder:
".(backslash).venv\Scripts\Activate.ps1"


## **Project**

Costruire un sistema RAG (Retrieval-Augmented Generation) vanilla, partendo da zero, senza usare framework di alto livello come LangChain o LlamaIndex.


Cosa Servirà:

- Gestore di file in input che leggerà un txt oppure (comincia con questo) un pdf (vedremo se abilitarlo anche per file docx).

- Scrivere un metodo per leggere il file in ingresso

- Scrivere un metodo per cui il programma tokenizzerà il file input. Con questo avremo un metodo di chuncking, in modo da spezzare i file in blocchi definiti (acnhe con un modo per non troncare frasi)

- Gestione e creazione degli emdedding, con tanto di definizione di una similarity metric

- Motore di ricerca del RAG: memorizzare e cercare all'interno dei documenti. Costruire un metodo per fornire i top 3 risultati ecc.

- Generazione e interfaccia.





## Gemini Guidelines

**Settimana 1**: Ingestione e Chunking (Il manipolatore di testi)
Prima di fare AI, devi saper manipolare i dati. L'obiettivo qui è leggere un documento e dividerlo in pezzi più piccoli (chunk), un passaggio critico perché i modelli AI hanno un limite di testo che possono "leggere" in una volta sola.

I tuoi Task:

Crea un file document_processor.py.

Scrivi una classe DocumentProcessor che accetta il percorso di un file di testo (.txt o .md).

Scrivi un metodo per leggere il contenuto del file.

Scrivi un metodo di chunking: deve prendere il testo intero e restituire una lista di stringhe (es. blocchi di 500 caratteri, con una sovrapposizione di 50 caratteri tra un blocco e l'altro per non spezzare le frasi a metà).

Concetti Python da imparare/ripassare: * Programmazione ad oggetti: definire una class e il metodo costruttore __init__.

Gestione sicura dei file (il costrutto with open(...) as file:).

Type Hinting (es. def fai_chunking(self, testo: str) -> list[str]:).



**Settimana 2**: Vettorizzazione (Parlare con i modelli)
Ora devi trasformare i tuoi "chunk" di testo in numeri, o meglio, in vettori (Embeddings). Questo permette al computer di capire il significato semantico delle parole.

I tuoi Task:

Crea un file embedder.py.

Scrivi una classe Embedder. Questa classe dovrà fare una chiamata HTTP a un'API per generare gli embedding (puoi usare l'API di OpenAI o, se vuoi fare tutto gratis sul tuo PC, installare Ollama e usare un modello locale).

Use case
Input	                    Response                Use
"input": "text"	            [vector]	            take [0]
"input": ["t1","t2"]	    [v1, v2]	            keep both
NB: Tip for vector databases (FAISS, Chroma, Qdrant, etc.): Always store the inner vector, not the outer array.

Passa la tua lista di chunk alla classe e ottieni in cambio una lista di vettori (liste di float).

Concetti Python da imparare/ripassare:

Gestire pacchetti esterni (creare un file requirements.txt e un Virtual Environment).

Fare richieste web con la libreria requests.

Nascondere le chiavi segrete (usare la libreria python-dotenv per non mettere mai l'API key nel codice).

Gestione degli errori: usare try... except nel caso in cui l'API non risponda.



**Settimana 3**: Il Motore di Ricerca (La matematica dietro le quinte)
Questo è il cuore del RAG. Quando l'utente fa una domanda, devi trasformare la domanda in un vettore e trovare quali chunk del tuo documento hanno i vettori più "vicini" (simili) matematicamente.

I tuoi Task:

Crea un file vector_store.py.

Scrivi una classe SimpleVectorDB che salvi in memoria i tuoi chunk e i rispettivi vettori (basta un semplice dizionario Python o una lista).

Scrivi una funzione che calcoli la Cosine Similarity tra il vettore della domanda e tutti i vettori salvati.

Ordina i risultati e restituisci i "Top 3" chunk più rilevanti.

Concetti Python da imparare/ripassare:

Usare la libreria numpy per operazioni matematiche su array (molto più veloce del Python standard).

Ordinamento avanzato di liste e dizionari (funzione sorted() con argomenti key personalizzati, magari usando funzioni lambda).



**Settimana 4**: Generazione e Interfaccia (La chiusura del cerchio)
È il momento di unire i pezzi. Prenderai i frammenti di testo trovati, li unirai alla domanda dell'utente e chiederai all'LLM di formulare la risposta finale.

I tuoi Task:

Crea un file main.py. Questo sarà il "direttore d'orchestra" che importa e usa tutte le classi che hai creato finora.

Crea un "Prompt Template": una stringa in cui inietti la domanda e il contesto trovato.

Fai un'ultima chiamata all'LLM (es. GPT-3.5 o Llama 3) per fargli generare la risposta basata sul prompt.

Permetti all'utente di fare la domanda direttamente dal terminale (es. python main.py "Quali sono le conclusioni del documento?").

Concetti Python da imparare/ripassare:

Importare moduli tra file diversi nel tuo progetto.

Le f-strings per formattare testi complessi in modo pulito (es. f"Rispondi a questa domanda: {domanda} usando questo contesto: {contesto}").

Usare argparse o sys.argv per passare argomenti allo script da riga di comando.