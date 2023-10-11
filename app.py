import io
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from urllib.request import urlopen
from PIL import Image, ImageTk

# Define the file types and the folders to sort them into
file_types = {
    ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a": "audio",
    ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".3gp": "videos",
    ".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd": "images",
    ".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx": "documents",
    ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2": "archives",
    ".txt", ".md", ".log", ".json", ".yaml", ".csv": "plain-text",
    ".exe", ".msi": "exe",
    ".pdf": "pdf",
    ".py": "python",
    ".xml", ".xsd", ".dtd", ".xslt": "xml",
    ".sh", ".bash", ".zsh": "shell",
}

class FileOrganizer:
    def __init__(self, master):
        self.master = master
        master.title("Neuronexus File Organiser")
        master.geometry("320x165")

        # Fetch the Neuronexus logo from the URL and create a PhotoImage object from it
        logo_url = "https://www.neuronexus.xyz/media/images/neuronexuslogo.png"
        self.logo_data = urlopen(logo_url).read()
        self.logo_image = ImageTk.PhotoImage(Image.open(io.BytesIO(self.logo_data)))

        # Add the Neuronexus logo to the GUI
        self.logo_label = tk.Label(master, image=self.logo_image)
        self.logo_label.pack()

        # Create the user interface
        self.folder_path = tk.StringVar()
        self.folder_label = tk.Label(master, text="Select a folder to organise:")
        self.folder_label.pack()
        self.folder_entry = tk.Entry(master, textvariable=self.folder_path)
        self.folder_entry.pack()
        self.folder_button = tk.Button(master, text="Browse...", command=self.browse_folder)
        self.folder_button.pack()
        self.organize_button = tk.Button(master, text="Organise Files", command=self.organize_files)
        self.organize_button.pack()

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_path.set(folder_path)

    def organize_files(self):
        folder_path = self.folder_path.get()
        if not folder_path:
            messagebox.showerror("Error", "Please select a folder to organise.")
            return

        # Organise the files
        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                file_ext = os.path.splitext(filename)[1].lower()
                if file_ext in file_types:
                    folder_name = file_types[file_ext]
                    folder_path_new = os.path.join(folder_path, folder_name)
                    if not os.path.exists(folder_path_new):
                        os.mkdir(folder_path_new)
                    shutil.move(os.path.join(folder_path, filename), os.path.join(folder_path_new, filename))

        messagebox.showinfo("Success", "Files have been organised.")

# Create the GUI window
root = tk.Tk()
file_organizer = FileOrganizer(root)
root.mainloop()
