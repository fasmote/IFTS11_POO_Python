class Document:
   
    def __init__(self, doc_id, contenido):
        self.id = doc_id
        self.contenido = contenido 

    def __repr__(self):
        
        return f"Document(ID={self.id}, Data={self.contenido})"
