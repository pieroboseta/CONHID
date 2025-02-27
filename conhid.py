import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import json

# Configuration
HISTORY_FILE = "conhid.json"
BUTTON_COLOR = "#8c006e"
BG_COLOR = "#420135"
TEXT_COLOR = "white"

class ConhidApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CONHID")
        self.root.geometry("500x230")
        self.root.configure(bg=BG_COLOR)
        
        self.folder_path = ""
        self.history = self.load_history()
        
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg=BG_COLOR, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.select_button = tk.Button(self.frame, text="Select", command=self.select_folder, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.select_button.pack(fill=tk.X, pady=5)
        
        self.rename_button = tk.Button(self.frame, text="Rename", command=self.rename_files, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.rename_button.pack(fill=tk.X, pady=5)
        
        self.restore_button = tk.Button(self.frame, text="Restore", command=self.restore_files, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.restore_button.pack(fill=tk.X, pady=5)
        
        self.list_button = tk.Button(self.frame, text="Full List", command=self.show_full_list, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.list_button.pack(fill=tk.X, pady=5)
        
        self.search_entry = tk.Entry(self.frame)
        self.search_entry.pack(fill=tk.X, pady=5)
        
        self.search_button = tk.Button(self.frame, text="Search", command=self.search_files, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.search_button.pack(fill=tk.X, pady=5)
    
    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            messagebox.showinfo("Selected Folder", f"Folder selected: {self.folder_path}")
    
    def rename_files(self):
        if not self.folder_path:
            messagebox.showerror("Error", "No folder selected.")
            return
        
        files = os.listdir(self.folder_path)
        new_names = {}
        
        for idx, file in enumerate(files, start=1):
            old_path = os.path.join(self.folder_path, file)
            new_name = f"document-{idx}.bin"
            new_path = os.path.join(self.folder_path, new_name)
            
            os.rename(old_path, new_path)
            new_names[new_name] = file
        
        self.history[self.folder_path] = new_names
        self.save_history()
        messagebox.showinfo("Success", "Files renamed successfully.")
    
    def restore_files(self):
        if not self.folder_path or self.folder_path not in self.history:
            messagebox.showerror("Error", "No rename history found for this folder.")
            return
        
        for new_name, old_name in self.history[self.folder_path].items():
            new_path = os.path.join(self.folder_path, new_name)
            old_path = os.path.join(self.folder_path, old_name)
            
            if os.path.exists(new_path):
                os.rename(new_path, old_path)
        
        del self.history[self.folder_path]
        self.save_history()
        messagebox.showinfo("Success", "Files restored successfully.")
    
    def show_full_list(self):
        if not self.folder_path or self.folder_path not in self.history:
            messagebox.showerror("Error", "No rename history available.")
            return
        
        list_window = tk.Toplevel(self.root)
        list_window.title("Full List")
        list_window.geometry("400x300")
        list_window.configure(bg=BG_COLOR)
        
        tree = ttk.Treeview(list_window, columns=("Original Name", "New Name"), show="headings")
        tree.heading("Original Name", text="Original Name")
        tree.heading("New Name", text="New Name")
        tree.pack(fill=tk.BOTH, expand=True)
        
        for new_name, old_name in self.history[self.folder_path].items():
            tree.insert("", "end", values=(old_name, new_name))
    
    def search_files(self):
        search_term = self.search_entry.get().strip().lower()
        if not search_term:
            messagebox.showerror("Error", "Enter a search term.")
            return
        
        if not self.folder_path or self.folder_path not in self.history:
            messagebox.showerror("Error", "No rename history available.")
            return
        
        results = [(old, new) for new, old in self.history[self.folder_path].items() if search_term in old.lower() or search_term in new.lower()]
        
        if not results:
            messagebox.showinfo("Results", "No matching files found.")
            return
        
        result_window = tk.Toplevel(self.root)
        result_window.title("Search Results")
        result_window.geometry("400x300")
        result_window.configure(bg=BG_COLOR)
        
        tree = ttk.Treeview(result_window, columns=("Original Name", "New Name"), show="headings")
        tree.heading("Original Name", text="Original Name")
        tree.heading("New Name", text="New Name")
        tree.pack(fill=tk.BOTH, expand=True)
        
        for old_name, new_name in results:
            tree.insert("", "end", values=(old_name, new_name))
    
    def load_history(self):
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as file:
                return json.load(file)
        return {}
    
    def save_history(self):
        with open(HISTORY_FILE, "w") as file:
            json.dump(self.history, file, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConhidApp(root)
    root.mainloop()
