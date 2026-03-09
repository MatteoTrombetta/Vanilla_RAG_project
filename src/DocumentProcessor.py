from pathlib import Path

class DocumentProcessor:
    """Class to handle the processing and the split of the document into chunks"""
    def __init__(self, chunk_size: int=500, chunk_overlap: int=100) -> None:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def load_document(self, file_path: Path) -> str:
        return file_path.read_text(encoding='utf-8')      
    
    def chunks_text(self, doc: str) -> list[str]:
        """Method used to split the document into chunks
        mimics a sliding window to allow overlapping between chunks"""
        # POSSIBLE FUTURE IMPROVEMENT:
        # We could use regex or 'nltk' library to allow dynamic splits at the end of phrases or paragraphs.
        chunks: list[str] = []
        # range(start, stop, step)
        for i in range(0, len(doc), self.chunk_size-self.chunk_overlap):
            block: str = doc[i:i+self.chunk_size]
            chunks.append(block)
        return chunks

"""             if i-self.chunk_overlap <= 0:
                block: str = doc[0:self.chunk_size + self.chunk_overlap]
            elif i+self.chunk_overlap > len(doc):
                block: str = doc[i:]
            else:
                block: str = doc[i:self.chunk_size + self.chunk_overlap]
            chunks.append(block) 
            return chunks
"""



