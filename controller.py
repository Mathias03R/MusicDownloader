from tkinter import messagebox
from pytube import YouTube, Search
from pytube.exceptions import VideoUnavailable
from view import MusicDownloaderUI
import tkinter as tk
import yt_dlp
import os
import threading

class MusicController:
    def __init__(self):
        self.root = tk.Tk()
        self.song_list = []
        self.s = None
        self.ui = MusicDownloaderUI(self.root, self, self.obtener_path())
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        self.ruta_absoluta = ruta_actual.replace("\\", "/")
        

    def run(self):
        self.root.mainloop()

    def on_complete(self, stream, filepath):
        messagebox.showinfo("Descarga completa", "La descarga ha finalizado correctamente.")

    def buscar(self, url):
        self.s = None
        self.song_list = []
        
        if not url:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una URL o un título válido.")
            return
        
        if url.startswith("http://") or url.startswith("https://"):
            try: 
                yt = YouTube(url=url, on_complete_callback=self.on_complete)
                return [yt]
            except VideoUnavailable:
                messagebox.showerror("Error", "Video no disponible.")
        else:
            s = Search(url)
            return s.results

        
    def descargar(self, song, destino):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': destino + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': self.ruta_absoluta + '/utils/bin/ffmpeg.exe',
            'ffprobe_location': self.ruta_absoluta + '/utils/bin/ffprobe.exe'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                print(song.watch_url)
                info = ydl.extract_info(song.watch_url, download=True)
                title = info['title']
                self.root.after(0, lambda: messagebox.showinfo("Descarga Exitosa", f"La canción {title} se ha descargado exitosamente."))
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Error", "No se pudo descargar el video seleccionado."))
                print (e)
            finally:
                self.root.after(0, lambda: self.ui.download_button.config(state=tk.NORMAL, text="Descargar"))

    def descargar_action(self, song, destino):
        self.ui.download_button.config(state=tk.DISABLED, text="Descargando...")

        if song and destino:
            thread = threading.Thread(target=self.descargar, args=(song, destino))
            thread.start()
        else:
            messagebox.showerror("Error de entrada", "Debe ingresar una URL")

    def obtener_path(self):
        try:
            with open("path.txt", "r") as f:
                path = f.read()
                return path
        except FileNotFoundError:
            return None
        except Exception as e:
            print(e)
            return None
        
    def set_path(self, path):
        try:
            with open("path.txt", "w") as f:
                f.write(path)
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "No se pudo guardar la ruta. Intente de nuevo.")

if __name__ == "__main__":
    controller = MusicController()
    controller.run()
