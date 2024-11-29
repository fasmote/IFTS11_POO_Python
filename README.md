
# Trabajo Práctico - Programación Orientada a Objetos (POO)

Este proyecto fue desarrollado como parte del trabajo práctico de Programación Orientada a Objetos (POO). Su objetivo es integrar tres clases fundamentales: `Str2Dic`, `Collection` y `Document`, y usarlas para manipular datos provenientes de un archivo CSV.

## **Objetivo del Proyecto**
El trabajo busca aplicar conceptos básicos de POO como clases, métodos y encapsulamiento. El programa lee un archivo CSV con datos personales, convierte las líneas en documentos usando un esquema, y almacena estos documentos en una colección. 

Finalmente, podemos realizar operaciones como buscar documentos, listar la colección completa o importar datos desde un archivo.

---

## **Descripción de las Clases**

### **1. Clase `Document`**
- Representa un documento individual.
- Tiene un identificador único (`id`) y un diccionario con los datos del documento.

### **2. Clase `Collection`**
- Gestiona una colección de documentos.
- Usa un diccionario donde las claves son los IDs de los documentos.
- Permite agregar, buscar, eliminar y listar documentos.

### **3. Clase `Str2Dic`**
- Convierte una línea de texto separada por comas (como en un CSV) en un diccionario.
- Se basa en un esquema proporcionado (los nombres de las columnas).

---

## **Estructura del Proyecto**

```
TP_POO/
├── main.py                 # Archivo principal para ejecutar el programa
├── clases/                 # Carpeta que contiene las clases
│   ├── collection.py       # Clase Collection
│   ├── document.py         # Clase Document
│   ├── str2doc.py          # Clase Str2Dic
├── archivos/               # Carpeta para almacenar los archivos CSV
│   ├── basededatos.csv     # Archivo CSV de ejemplo
│   ├── ejemplo30.csv       # Otro archivo CSV con más datos
```

---

## **Funciones Principales**

### **1. Crear una Colección**
- Selecciona la opción 1 del menú para crear una nueva colección.

### **2. Importar un Archivo CSV**
- Selecciona la opción 2 para importar datos desde un archivo CSV.
- Puedes especificar un nombre para la colección.

### **3. Buscar un Documento**
- Selecciona la opción 3 y proporciona el ID del documento que deseas buscar.

### **4. Eliminar un Documento**
- Selecciona la opción 4 y proporciona el ID del documento que deseas eliminar.

### **5. Listar Documentos**
- Selecciona la opción 5 para listar todos los documentos de una colección.

---
