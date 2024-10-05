# MusicDownloader

MusicDownloader es una aplicación de escritorio en Python que permite buscar y descargar música de YouTube.

## Características

- Búsqueda por URL o título de la canción en YouTube.
- Descarga de canciones en formato MP3.
- Interfaz amigable desarrollada con Tkinter.
- Indicador de progreso durante la descarga.
- Descarga en segundo plano (usando threading) para mantener la aplicación receptiva.
- Ruta de descarga configurable.
- Botón de descarga que se desactiva y muestra "Descargando..." durante el proceso.

## Requisitos

- Python 3.11
- Módulos de Python:
    - pytube
    - yt-dlp
    - tkinter

## Instalación

### Clona este repositorio:

git clone https://github.com/tu-usuario/MusicDownloader.git

### Instala las dependencias:

pip install pytube yt-dlp

Asegúrate de tener ffmpeg instalado y en la ruta indicada en el código. Si no lo tienes, descárgalo aquí y ajusta la ubicación en el archivo controller.py:

'ffmpeg_location': 'path/to/ffmpeg',
'ffprobe_location': 'path/to/ffprobe'

## Uso:
Clona o descarga el repositorio.

Ejecuta la aplicación con:

python controller.py

Ingresa un título de canción o una URL.

Selecciona la carpeta de descarga.

Haz clic en "Buscar".

Selecciona una de las opciones del recuadro y da click en "Descargar"

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto
Para preguntas, contacta a Mathias.Romero@codigocreativo.pe.
