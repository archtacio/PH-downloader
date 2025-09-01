# Video Downloader

Un descargador de videos sencillo y flexible escrito en Python, utilizando [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Características
- Descarga videos individuales desde una URL.
- Soporte para calidad personalizada (`best`, `worst`, `1080p`, etc.).
- Guarda automáticamente en carpeta `descargas/` si no se especifica destino.
- Interfaz por línea de comandos y modo interactivo.

## Requisitos
- Python 3.8+
- yt-dlp

## Instalación
```bash
git clone https://github.com/tuusuario/video-downloader.git
cd video-downloader
pip install -r requirements.txt
