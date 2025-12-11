# Conversor de HTML a Markdown

Este script convierte automáticamente todos los archivos **HTML** ubicados en una carpeta específica a archivos **Markdown (.md)**, utilizando la librería `markdownify`.  
Además, evita sobrescribir archivos ya convertidos, omitiéndolos si la versión `.md` ya existe.


## 🚀 Características

- Convierte archivos `.html` a `.md` de forma automática.
- Omite la conversión si el archivo Markdown ya existe.
- Elimina etiquetas innecesarias como `<script>` y `<style>`.
- Mantiene la estructura de carpetas definida por el usuario.
- Compatible con grandes cantidades de archivos (aumenta el límite de recursión).


## 📁 Estructura de carpetas usada

```
lescorts/
│── html/
│ └── 2025/
│ └── va/
│ ├── archivo1.html
│ ├── archivo2.html
│ └── ...
│
└── md/
└── 2025/
└── va/
```

## 🧩 Requisitos

Instala la librería necesaria:

```
pip install markdownify
```

## 🛠️ Uso

Simplemente ejecuta el script:

```
python html_to_markdown.py
```

Asegúrate de actualizar las rutas si deseas trabajar con otros directorios:

```
input_folder = "lescorts/html/2025/va"
output_folder = "lescorts/md/2025/va"
```

## 💰 Financiación

Este recurso está financiado por el Ministerio para la Transformación Digital y de la Función Pública — Financiado por la UE – NextGenerationEU, en el marco del proyecto Desarrollo de Modelos ALIA.

## 🙏 Agradecimientos

Expresamos nuestro agradecimiento a todas las personas e instituciones que han contribuido al desarrollo de este recurso.

Agradecimientos especiales a:

[Proveedores de datos]

[Proveedores de soporte tecnológico]

Asimismo, reconocemos las contribuciones financieras, científicas y técnicas del Ministerio para la Transformación Digital y de la Función Pública – Financiado por la UE – NextGenerationEU dentro del marco del proyecto Desarrollo de Modelos ALIA.

## 📚 Referencia

Por favor, cita este conjunto de datos usando la siguiente entrada BibTeX:

```
@misc{conversor_alia_lescorts_2025,
  author       = {Espinosa Zaragoza, Sergio and Sep{\'u}lveda Torres, Robiert and Mu{\~n}oz Guillena, Rafael and Consuegra-Ayala, Juan Pablo},
  title        = {ALIA_lescorts Conversor}, 
  year         = {2025},
  institution  = {Language and Information Systems Group (GPLSI) and Centro de Inteligencia Digital (CENID), University of Alicante (UA)},
  howpublished = {\url{https://github.com/gplsi/scraper-alia-uv}}
}
```

## ⚠️ Aviso Legal

Este recurso puede contener sesgos o artefactos no intencionados.
Cualquier tercero que utilice o implemente sistemas basados en este recurso es el único responsable de garantizar un uso conforme, seguro y ético, incluyendo el cumplimiento de las normativas relevantes en materia de IA y protección de datos.

La Universidad de Alicante, como creadora y propietaria del recurso, no asume ninguna responsabilidad por los resultados derivados del uso por parte de terceros.

## 📜 Licencia

Licencia Apache, Versión 2.0
