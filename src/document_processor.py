
# Let's start by creating a class that handles the preprocessing part from a PDF file


class FileTokenizer:

    type = "Document"

    def __init__(self, docName, docType, docLength):
        self.docName = docName
        self.docType = docType
        self.docLength = docLength
    pass


