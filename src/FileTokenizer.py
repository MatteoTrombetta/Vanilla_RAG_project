'''
The project here is to write a RAG system from 
scratch without the use of Llamaindex or LangChain.
I will do it by hand without using AI.

Cosa devi fare:

1. Scrivi una classe Python che legge un file PDF o TXT e lo divide in blocchi (chunking) usando logica pura (es. contando i token o i caratteri).

2. Usa le API (es. OpenAI o un modello locale con Ollama) per trasformare questi blocchi in vettori numerici (Embeddings). 
Non usare un Vector DB già pronto, ma salva i vettori in un array Numpy.

3. Scrivi tu la funzione matematica in Python per calcolare la Cosine Similarity tra la domanda dell'utente e i tuoi documenti.

4. Passa il contesto trovato all'LLM per fargli generare la risposta.

'''


# Let's start by creating the skeleton for this system

# Let's start by creating a class that handles the preprocessing part from a PDF file


class FileTokenizer:

    type = "Document"

    def __init__(self, docName, docType, docLength):
        self.docName = docName
        self.docType = docType
        self.docLength = docLength
    pass


