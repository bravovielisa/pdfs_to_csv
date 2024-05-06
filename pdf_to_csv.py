import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1
import csv

# Directorios de entrada y salida
input_folder = r'C:\Users\usuario\pdf_input'
output_folder = r'C:\Users\usuario\csv_input'

# Nos aseguramos de que la carpeta de salida existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lista con los nombres de los archivos PDF en la carpeta de entrada
pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

# Iteramos a través de los archivos PDF y los convertimos en CSV
for file in pdf_files:
    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.csv')  # Cambiamos el nombre del archivo a CSV

    with open(output_path, 'w', newline='', encoding='latin1') as csv_file:
        csv_writer = csv.writer(csv_file, escapechar='\\')

        # Encabezados de las columnas
        csv_writer.writerow(['Variable', 'Valor'])

        # Abre el archivo PDF
        with open(input_path, 'rb') as pdf_file:
            parser = PDFParser(pdf_file)
            doc = PDFDocument(parser)
            fields = resolve1(doc.catalog['AcroForm'])['Fields']

            # Itera a través de los campos de formulario
            for i in fields:
                field = resolve1(i)
                name = field.get('T', b'').decode('latin1', errors='replace')
                value_obj = field.get('V', b'')

                if isinstance(value_obj, bytes):
                    value = value_obj.decode('latin1', errors='replace')
                else:
                    value = str(value_obj)

                csv_writer.writerow([name, value])

# Mostrar mensaje al final del proceso
print(f"Se han convertido {len(pdf_files)} archivos PDF a CSV en la carpeta de salida: {output_folder}")