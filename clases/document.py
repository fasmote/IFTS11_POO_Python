class Document:
   
    def __init__(self, doc_id, data):
        self.id = doc_id  # ID único del documento
        self.data = data  # Diccionario con los datos del documento

    def __repr__(self):
        
        return f"Document(ID={self.id}, Data={self.data})"
