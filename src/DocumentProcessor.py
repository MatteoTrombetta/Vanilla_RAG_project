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

# Let's start by creating a class that handles the preprocessing part from a PDF file


from pathlib import Path
import os
import Document

class DocumentProcessor:

    def __init__(self, chunck_size=1000, chunck_overlap=200):
        self.chunck_size = chunck_size
        self.chunck_overlap = chunck_overlap

    def load_document(self, file_path):
        # file_path = Path.cwd() # current working directory
        # __file__ gives the path of the current script file
        file_path = Path(__file__).parent.resolve() #.parent gets the containing folder, .resolve() returns an absolute path
        print('File Path: ', file_path)
        # Remeber that here the path is on '/docs' check whether you need to change that
        try:
            with (file_path / 'docs/file_prova2.txt', 'r') as file:
                content = file.read()
                print(content) # can be removed
        except FileNotFoundError:
            print("Error: file does not exists")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        return content




