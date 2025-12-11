import os
from markdownify import markdownify as md
import sys
sys.setrecursionlimit(10000)

if __name__ == '__main__':
    # Carpeta con los archivos HTML
    input_folder = "lescorts/html/2025/va"
    output_folder = "lescorts/md/2025/va"

    # Asegurar que la carpeta de salida existe
    os.makedirs(output_folder, exist_ok=True)

    # Procesar cada archivo HTML
    for filename in os.listdir(input_folder):
        if filename.endswith(".html"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace(".html", ".md"))

            # Verificar si el archivo Markdown ya existe
            if os.path.exists(output_path):
                print(f"El archivo {output_path} ya existe, se omite la conversión.")
                continue  # Omite la conversión para este archivo

            # Leer el HTML
            with open(input_path, "r", encoding="utf-8") as f:
                html_content = f.read()

            # Convertir a Markdown
            markdown_content = md(html_content, strip=["script", "style"])

            # Guardar el archivo Markdown
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown_content)

            print(f"Convertido: {filename} -> {output_path}")

    print("Conversión completa.")

