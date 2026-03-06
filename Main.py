'''
Main.

The project here is to write a RAG system from 
scratch without the use of Llamaindex or LangChain.
I will do it by hand without using AI.

WHAT TO INSERT AS A TYPICAL STRUCTURE FILE:
- File header: with Shebangline, encoding declaration, Docstring
- Imports
- Global Constants

'''

from src.DocumentProcessor import DocumentProcessor
from src.OllamaEmbedder import OllamaEmbedder
from src.VanillaEmbedder import VanillaEmbedder
from pathlib import Path

TYPE = "Document"

# OTHER FUNCTIONS TO BE USED

# MAIN FUNCTION
def main():
    print("> This this is a program that simulates a simple RAG system." \
    "\nPlease enter decide whether you want to append a new document with the following commands: \n" \
    ">\'1\': Chunk a document.\n"
    ">\'2\': Obtain the embdedding of string input using OllamaEmbdder class.\n"
    ">\'3\': Obtain the embdedding of string input using VanillaEmbedder class.\n"
    ">\'4\': Simulate the ingestion of the documents int the \'\docs\' directory.\n"
    )
    x :str = input()

    processor = DocumentProcessor(100, 20)
    p = Path('src/docs/file_prova2.txt')
    document = processor.load_document(p)
    chunks_ex = processor.chunks_text(document)

    print("\n")

    match x:
        case "1":
            #Checks for the correct use of class DocumentProcessor   
            for i in range(len(chunks_ex)):
                print(f"** Chunk number: {i} Value = ", chunks_ex[i])
                print("\n|" \
                    "\n|" \
                    "\n|")
        case "2":
            #Checks for correct use class OllamaEmbedder
            print('\n> Choose the input string you want to embedd :')
            embedder = OllamaEmbedder()
            input_string: str = input()
            new_embedding = embedder.get_embed(input_string)

        case "3":
            #Checks for correct use class VanillaEmbedder
            print('\n> Choose the input string you want to embedd :')
            embedder = VanillaEmbedder()
            input_string: str = input()
            new_embedding = embedder.get_embed(input_string)
        case "4":
            #Checking ingestion of documents
            processor = DocumentProcessor(100, 20)
            embedder = VanillaEmbedder()
            knowledge_base = []
            docs_path = Path('src/docs')
            for child in docs_path.iterdir(): 
                doc: str = processor.load_document(child)
                doc_chunks = processor.chunks_text(doc)
                for chunk in doc_chunks:
                    emb_chunk = embedder.get_embed(chunk)
                    new_info = {
                        "source": child.name,
                        "text": chunk,
                        "embedding": emb_chunk
                    }
                    knowledge_base.append(new_info)
            print('Database successfully created.')
            print(f'Total number of elaborated chunks: {len(knowledge_base)}')
            print(f'Shape of the first chunk: {len(knowledge_base[0]["embedding"])}')
        case _: 
            print('Closing...')
    return
    


if __name__ == "__main__":
    main()