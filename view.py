import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, filedialog

class MusicDownloaderUI:
    def __init__(self, root, controller, save_path):
        self.root = root
        self.controller = controller
        self.save_path = save_path
        self.song_options = []

        # Configurar la ventana principal
        self.root.title("Music Downloader")
        self.root.geometry("400x400")

        # Crear los widgets
        self.label = tk.Label(root, text="Ingrese URL o Título de la canción:")
        self.label.pack(pady=10)

        self.frame1 = tk.Frame(root, padx=50, pady=0)
        self.frame1.pack(pady=10, fill=tk.BOTH)

        self.input_entry = tk.Entry(self.frame1, width=40)
        self.input_entry.pack(side=tk.LEFT)

        self.search_button = tk.Button(self.frame1, text="Buscar", command=self.search_action)
        self.search_button.pack(side=tk.RIGHT)

        self.frame2 = tk.Frame(root, padx=10, pady=0)
        self.frame2.pack(pady=10, fill=tk.BOTH)

        self.select_folder_button = tk.Button(self.frame2, text="Seleccionar carpeta", command=self.select_folder)
        self.select_folder_button.pack(side=tk.LEFT)

        self.folder_label = tk.Label(self.frame2, text=f"Carpeta: ...{self.save_path.split('/')[-2]}/{self.save_path.split('/')[-1]}" if self.save_path else "Seleccione una carpeta")
        self.folder_label.pack(side=tk.LEFT)

        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.song_listbox = Listbox(root, selectmode=tk.SINGLE, yscrollcommand=self.scrollbar.set, height=8)
        self.song_listbox.pack(pady=10, padx=10, fill=tk.BOTH)
        self.scrollbar.config(command=self.song_listbox.yview)

        self.download_button = tk.Button(root, text="Descargar", command=self.download_action)
        self.download_button.pack(pady=10)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.save_path = folder
            self.controller.set_path(folder)
            self.folder_label.config(text=f"Carpeta: ...{self.save_path.split('/')[-2]}/{self.save_path.split('/')[-1]}")

    def search_action(self):
        query = self.input_entry.get().strip()
        if not self.save_path:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una carpeta para guardar las descargas.")
            return
        if query:
            self.song_options = self.controller.buscar(query)
            self.show_song_options(self.song_options)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una URL o un título válido.")

    def show_song_options(self, options):
        self.song_listbox.pack(pady=10, padx=10, fill=tk.BOTH)
        self.song_listbox.delete(0, tk.END)  # Limpiar la lista anterior
        for option in options:
            self.song_listbox.insert(tk.END, option.title)

    def download_action(self):
        if not self.song_listbox.curselection():
            return
        selected_index = self.song_listbox.curselection()[0]
        selected_song = self.song_options[selected_index]
        self.controller.descargar_action(selected_song, self.save_path)
