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

## 💰 Funding

This resource is funded by the *Ministerio para la Transformación Digital y de la Función Pública* — Funded by **EU – NextGenerationEU**, within the framework of the project *Desarrollo de Modelos ALIA*.

## 🙏 Acknowledgments

We extend our gratitude to all individuals and institutions that contributed to the development of this resource.

Special thanks to:

- [Data providers]  
- [Technological support providers]

We also acknowledge the financial, scientific, and technical contributions of the *Ministerio para la Transformación Digital y de la Función Pública – Funded by EU – NextGenerationEU* within the framework of the *Desarrollo de Modelos ALIA* project.

## 📚 Reference

Please cite this dataset using the following BibTeX entry:

```bibtex
@misc{uji_parallel_va_en_2025,
  author       = {Espinosa Zaragoza, Sergio and Sep{\'u}lveda Torres, Robiert and Mu{\~n}oz Guillena, Rafael and Consuegra-Ayala, Juan Pablo}, <-- ACTUALIZAR
  title        = {ALIA_lescorts Converter}, 
  year         = {2025},
  institution  = {Language and Information Systems Group (GPLSI) and Centro de Inteligencia Digital (CENID), University of Alicante (UA)},
  howpublished = {\url{https://huggingface.co/datasets/gplsi/uji_parallel_va_es}} <-- ACTUALIZAR
}
```

## ⚠️ Disclaimer

This resource may contain biases or unintended artifacts.
Any third party using or deploying systems based on this resource is solely responsible for ensuring compliant, safe, and ethical use, including adherence to relevant AI and data protection regulations.

The University of Alicante, as creator and owner of the resource, assumes no liability for outcomes resulting from third-party use.

## 📜 License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
