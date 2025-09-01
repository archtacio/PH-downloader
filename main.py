import os
import sys
import time
from datetime import datetime
import argparse
import yt_dlp

def download_video(url, output_path=None, quality="best"):
    """
    Descarga un video desde una URL utilizando yt-dlp
    
    Args:
        url (str): URL del video a descargar
        output_path (str, optional): Ruta donde guardar el video
        quality (str, optional): Calidad del video (default: "best")
    """
    # Crear carpeta de salida si no existe
    if output_path:
        os.makedirs(output_path, exist_ok=True)
    else:
        output_path = os.path.join(os.getcwd(), "descargas")
        os.makedirs(output_path, exist_ok=True)
    
    # Configurar opciones de descarga
    ydl_opts = {
        'format': quality,
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'progress_hooks': [progress_hook],
    }
    
    print(f"Iniciando descarga desde: {url}")
    print(f"Guardando en: {output_path}")
    print(f"Calidad seleccionada: {quality}")
    
    try:
        # Iniciar descarga
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_title = info.get('title', 'Video')
            print(f"\nDescarga completada: {video_title}")
            print(f"Archivo guardado en: {output_path}")
    except Exception as e:
        print(f"Error durante la descarga: {str(e)}")
        return False
    
    return True

def progress_hook(d):
    """Muestra el progreso de la descarga"""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\rProgreso: {percent} | Velocidad: {speed} | ETA: {eta}", end='')
    elif d['status'] == 'finished':
        print("\nProcesando archivo descargado...")

def main():
    parser = argparse.ArgumentParser(description='Descargador de videos para fines educativos')
    parser.add_argument('url', type=str, help='URL del video a descargar')
    parser.add_argument('-o', '--output', type=str, help='Carpeta donde guardar el video')
    parser.add_argument('-q', '--quality', type=str, default='best', 
                        help='Calidad del video (best, worst, 1080p, 720p, etc.)')
    
    # si se proporcionaron argumentos
    if len(sys.argv) == 1:
        # si no hay argumentos
        print("=== Descargador de Videos para Estudio ===")
        url = input("Ingrese la URL del video: ")
        output = input("Carpeta de destino (dejar en blanco para usar './descargas'): ")
        quality = input("Calidad deseada (dejar en blanco para usar 'best'): ")
        
        # valores predeterminados si están vacíos
        if not output:
            output = None
        if not quality:
            quality = "best"
        
        download_video(url, output, quality)
    else:
        # Modo línea de comandos
        args = parser.parse_args()
        download_video(args.url, args.output, args.quality)

if __name__ == "__main__":
    main()