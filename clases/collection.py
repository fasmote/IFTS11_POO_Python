from clases.document import Document
from clases.str2doc import Str2Dic

class Collection:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}

    def agregar_documento(self, doc_id, data):
        """
        Crea un objeto Document y lo agrega a la colección.
        :param doc_id: ID único del documento.
        :param data: Diccionario con los datos del documento.
        """
        documento = Document(doc_id, data)
        self.documentos[doc_id] = documento

    def get_document(self, doc_id):
       
        return self.documentos.get(doc_id, None)

    def delete_document(self, doc_id):
       
        if doc_id in self.documentos:
            del self.documentos[doc_id]

    def list_documents(self):
        
        return self.documentos

    def import_csv(self, ruta_csv):
        """
        Importa datos desde un archivo CSV.
        :param ruta_csv: Ruta al archivo CSV.
        """
        with open(ruta_csv, 'r', encoding='utf-8') as file:
            schema = file.readline().strip()
            str2dic = Str2Dic(schema)
            linea = file.readline().strip()
            doc_id = 1
            while linea != "":
                data = str2dic.convert(linea)
                self.agregar_documento(doc_id, data)
                linea = file.readline().strip()
                doc_id += 1
