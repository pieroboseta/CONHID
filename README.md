# 🌟 CONHID - Bulk File Renamer

Conhid is a **powerful, simple, and modern** bulk file renaming tool that now offers enhanced customization features. Easily rename files using a default sequence with a custom prefix and extension, or load a custom list of names from a JSON file. Conhid simplifies file organization with an intuitive interface and robust functionality.

---

## ✨ Features

| Feature                      | Description |
|------------------------------|-------------|
| 📂 **Select Folder**         | Choose a folder containing the files you want to rename. |
| 📝 **Set Prefix**            | Define a custom prefix and file extension for your file names. |
| 🗒 **Add List**              | Load a JSON file with a list of custom file names to be used for renaming. |
| 🔄 **Rename Files**          | Renames files using the custom list if available, or defaults to a sequential format (e.g., `document-1.bin`). |
| 🔙 **Restore Names**         | Revert files to their original names using saved rename history. |
| 📋 **Full List View**        | Displays a table of original and new file names for review. |
| 🔍 **Search**                | Search through both renamed and restored file names using keywords. |
| 📖 **Logging System**        | Tracks all renaming operations in `conhid.json` for auditability and easy restoration. |
| 🎨 **Modern UI**             | Features a sleek, dark-themed interface for an enhanced user experience. |
| 🚀 **Optimized for Windows** | Ensures smooth performance on Windows devices. |

---

## 📦 Requirements

- **Python 3.8+**
- **Tkinter (built-in with Python)**
- **JSON (built-in with Python)**

---

## 🛠 Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/pieroboseta/CONHID.git
   cd conhid
   ```

2. **Run the Script:**
   ```bash
   python conhid.py
   ```

---

## 🚀 Usage Guide

1. **Open Conhid** by running the Python script.
2. Click **"Select"** to choose the folder with files you want to rename.
3. Click **"Set Prefix"** to define your custom file name prefix and extension.
4. (Optional) Click **"Add List"** to load a JSON file containing custom file names.
5. Click **"Rename"** to rename the files using the custom list if available, or the default sequential format.
6. Click **"Restore"** to revert the files to their original names if necessary.
7. Use **"Full List"** to view all renaming operations and **"Search"** to locate specific files.

---

## ⚡ Preview

![Screenshot](https://github.com/user-attachments/assets/921d32e6-9a1f-4348-98aa-2249c30d2c39)


---

## 📝 Notes
- **Renaming Format:** Files are renamed using a custom list (if loaded via **Add List**) or a default format `<prefix>-<number>.<extension>` (e.g., `document-1.bin`).
- **Custom Naming Options:** Easily personalize your file names by setting a custom prefix and file extension.
- **Future Updates:** Features like "Undo Last Action" are coming soon.

---

## 📌 License
This project is licensed under the **MIT License**.

---

## 💡 Contributing
Want to improve Conhid? Feel free to fork the repo and submit a PR!

---

## 📞 Contact
For any issues or suggestions, open an issue on GitHub. 🚀
