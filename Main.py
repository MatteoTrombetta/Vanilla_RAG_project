'''
Main.

The project here is to write a RAG system from 
scratch without the use of Llamaindex or LangChain.
I will do it by hand without using AI.

WHAT TO INSERT AS A TYPICAL STRUCTURE FILE:
- File header: with Shebangline, encoding declaration, Docstring
- Imports
- Global Constants
-

'''

from src.DocumentProcessor import DocumentProcessor
from pathlib import Path

TYPE = "Document"

# OTHER FUNCTIONS TO BE USED

# MAIN FUNCTION
def main():
    print("This this is a program that simulates a simple RAG system." \
    "\nPlease enter decide whether you want to append a new document with the command " \
    "\'A\' or you want to retrieve some information with the command \'R\': ")
    
    processor = DocumentProcessor(100, 20)
    p = Path('src/docs/file_prova2.txt')
    document = processor.load_document(p)
    chunks_ex = processor.chunks_text(document)

    print("\n")

    for i in range(len(chunks_ex)):
        print(f"** Chunk number: {i} Value = ", chunks_ex[i])
        print("\n|" \
              "\n|" \
              "\n|" \
              "\n|")

    return
    
if __name__ == "__main__":
    main()