class Str2Dic():
	def__init__(self, schema: str, separator=','):
		if (len(schema))== 0:
			raise SchemaError("El schema esta vacio")
        self.schema = schema.split(separator)
        self.separator = separator
     def convert(self, row: str) -> dict:
        linea = row.split(self.separator)
        if len(linea) == len(self.schema):
            i=0
            d={}
            while i < len(linea):
                d[self.schema[i]] = linea[i]
                i = i + 1
            return d
        else:
            raise ValueError("Los campos de la fila no concuerdan con el schema")
        
  