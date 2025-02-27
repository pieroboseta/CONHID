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
        self.root.title("CONHID - Bulk File Renamer")
        self.root.geometry("320x160")
        self.root.configure(bg=BG_COLOR)
        
        self.folder_path = ""
        self.prefix = "document"
        self.extension = "bin"
        self.history = self.load_history()
        self.rename_list = []
        
        self.create_widgets()
    
    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg=BG_COLOR, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Row 0: Select and Prefix buttons
        self.select_button = tk.Button(self.frame, text="Select", command=self.select_folder, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.select_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        self.prefix_button = tk.Button(self.frame, text="Prefix", command=self.set_prefix, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.prefix_button.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        # Row 1: Rename and Add List buttons
        self.rename_button = tk.Button(self.frame, text="Rename", command=self.rename_files, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.rename_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        
        self.add_list_button = tk.Button(self.frame, text="Add List", command=self.load_list, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.add_list_button.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        
        # Row 2: Restore and Full List buttons
        self.restore_button = tk.Button(self.frame, text="Restore", command=self.restore_files, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.restore_button.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        
        self.list_button = tk.Button(self.frame, text="Full List", command=self.show_full_list, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.list_button.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        
        # Row 3: Search input and Search button
        self.search_entry = tk.Entry(self.frame)
        self.search_entry.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
        
        # Changed the search button color to white and text to black
        self.search_button = tk.Button(self.frame, text="Search", command=self.search_files, bg="white", fg="black")
        self.search_button.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        
        # Ensure both columns expand equally
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
    
    def set_prefix(self):
        prefix_window = tk.Toplevel(self.root)
        prefix_window.title("Set Prefix & Extension")
        prefix_window.geometry("300x150")
        prefix_window.configure(bg=BG_COLOR)
        
        tk.Label(prefix_window, text="Prefix:", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
        prefix_entry = tk.Entry(prefix_window)
        prefix_entry.pack(pady=5)
        
        tk.Label(prefix_window, text="File Extension:", bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
        extension_entry = tk.Entry(prefix_window)
        extension_entry.pack(pady=5)
        
        def save_prefix():
            self.prefix = prefix_entry.get() or "document"
            self.extension = extension_entry.get() or "bin"
            messagebox.showinfo("Success", f"Prefix set to: {self.prefix}\nExtension set to: {self.extension}")
            prefix_window.destroy()
        
        tk.Button(prefix_window, text="Save", command=save_prefix, bg=BUTTON_COLOR, fg=TEXT_COLOR).pack(pady=5)
    
    def load_list(self):
        if not self.folder_path:
            messagebox.showerror("Error", "Please select a folder first.")
            return
        
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    loaded_data = json.load(file)
                # Case 1: JSON file is a list
                if isinstance(loaded_data, list):
                    self.rename_list = loaded_data
                    messagebox.showinfo("Success", "List loaded successfully.")
                # Case 2: JSON file is a dictionary (e.g., history file)
                elif isinstance(loaded_data, dict):
                    if self.folder_path in loaded_data:
                        inner_data = loaded_data[self.folder_path]
                        if isinstance(inner_data, dict):
                            self.rename_list = list(inner_data.values())
                            messagebox.showinfo("Success", "List loaded successfully from history file.")
                        else:
                            messagebox.showerror("Error", "Expected a dictionary for the folder data in the JSON file.")
                    else:
                        messagebox.showerror("Error", "The JSON file does not contain data for the selected folder.")
                else:
                    messagebox.showerror("Error", "JSON file must contain a list of names or valid history data.")
            except Exception as e:
                messagebox.showerror("Error", f"Error loading JSON: {e}")
    
    def rename_files(self):
        if not self.folder_path:
            messagebox.showerror("Error", "No folder selected.")
            return
        
        files = os.listdir(self.folder_path)
        new_names = {}
        
        for idx, file in enumerate(files):
            old_path = os.path.join(self.folder_path, file)
            if idx < len(self.rename_list):
                new_name = f"{self.rename_list[idx]}.{self.extension}"
            else:
                new_name = f"{self.prefix}-{idx+1}.{self.extension}"
            new_path = os.path.join(self.folder_path, new_name)
            
            os.rename(old_path, new_path)
            new_names[new_name] = file
        
        self.history[self.folder_path] = new_names
        self.save_history()
        messagebox.showinfo("Success", "Files renamed successfully.")
    
    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            messagebox.showinfo("Selected Folder", f"Folder selected: {self.folder_path}")
    
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
            try:
                with open(HISTORY_FILE, "r") as file:
                    return json.load(file)
            except Exception as e:
                messagebox.showwarning("Warning", f"Failed to load history: {e}\nStarting with empty history.")
                return {}
        return {}
    
    def save_history(self):
        with open(HISTORY_FILE, "w") as file:
            json.dump(self.history, file, indent=4)

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = ConhidApp(root)
        root.mainloop()
    except Exception as e:
        print("An error occurred:", e)
        input("Press Enter to exit...")
