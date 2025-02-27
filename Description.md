# CONHID: Bulk File Renamer

## Overview
**CONHID** is a powerful, user-friendly bulk file renaming tool designed to simplify the process of organizing large collections of files. With its modern, sleek interface and robust feature set, CONHID allows you to rename files in bulk, restore original names, search through file histories, and even sort files by type. Whether you're managing media libraries, organizing documents, or performing routine file maintenance, CONHID is your go-to solution.

## What It Does
CONHID is built with several key functionalities:
- **Bulk Renaming:** Automatically renames all files in a selected folder using a consistent format (e.g., `document-1.bin`, `document-2.bin`, etc.).
- **Restoration:** Easily restore files to their original names using a saved rename history.
- **Search Functionality:** Quickly search through both renamed and restored files using keywords.
- **Logging System:** Every renaming operation is logged in a JSON file (`conhid.json`), ensuring that changes are tracked and can be reverted if necessary.
- **Modern Aesthetic:** The GUI features a dark-themed interface with uniform buttons for a visually appealing and intuitive experience.

## How It Works
1. **Select a Folder:**
   - Click the **Select** button to open a dialog and choose the folder containing the files you want to manage.
   - Once a folder is selected, CONHID loads all files from that directory.

2. **Rename Files:**
   - Click the **Rename** button to bulk rename all files in the selected folder.
   - Files are renamed following a standard format (e.g., `document-1.bin`, `document-2.bin`, etc.).
   - The original file names are stored in `conhid.json` for later restoration.

3. **Restore Files:**
   - If you need to revert the changes, click the **Restore** button.
   - CONHID reads the rename history from `conhid.json` and renames the files back to their original names.
   - The history for that folder is then cleared from the log.

4. **Full List View:**
   - Click the **Full List** button to open a new window that displays all files from the selected folder.
   
5. **Search:**
   - Enter a search term in the search bar and click the **Search** button.
   - CONHID will filter and display files whose original or new names match the search query.

## Features & Benefits
| Feature               | Description                                                                                      | Use Cases                                                 |
|-----------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| **Bulk Renaming**     | Renames files with a consistent, easy-to-read naming convention.                                 | Organizing media libraries or document archives.          |
| **Restore Function**  | Reverts files to their original names using saved history.                                       | Undo accidental renames or revert changes quickly.        |
| **Full List View**    | Displays a sortable table of files, showing both original and new names.                         | Quickly reviewing all file changes in one place.          |
| **Search Functionality** | Filters files based on keywords present in either original or renamed file names.            | Locating specific files within large directories.         |
| **Logging System**    | Maintains a detailed history of all renaming operations in a JSON file (`conhid.json`).             | Auditing changes and ensuring reversibility of actions.   |
| **Modern UI**         | Features a dark-themed interface with uniform buttons for a sleek user experience.       | Enhances user experience and reduces visual clutter.      |

## How It Can Be Useful
- **Media Organization:** Manage large collections of movies, TV shows, or music files by renaming them into a standard format, making it easier to sort and locate files.
- **Document Management:** Organize documents, reports, and scanned files with consistent naming conventions, especially useful in business or academic settings.
- **Bulk File Maintenance:** Automate repetitive file renaming tasks for IT professionals, archivists, and digital asset managers.
- **Error Correction:** Quickly revert unintended file renames, ensuring that original data is not permanently lost.
- **Custom Workflows:** Easily integrate with other tools or scripts that require standardized file names for further processing.

## Technical Details
- **Language:** Python
- **Libraries:** Tkinter for GUI, JSON for logging, OS for file operations
- **Configuration:**  
  - `HISTORY_FILE`: `conhid.json` stores rename history  
  - `BUTTON_COLOR`: `#8c006e`  
  - `BG_COLOR`: `#420135`  
  - `TEXT_COLOR`: `white`
- **System Requirements:** Python 3.8+ (Tkinter is included by default)

## Installation & Usage
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/pieroboseta/CONHID.git
   cd conhid
   ```

2. **Run the Application:**
   ```bash
   python conhid.py
   ```

3. **Follow the On-Screen Instructions:**
   - Click **Select** to choose a folder.
   - Use **Rename** to bulk rename files.
   - Click **Restore** to revert to original names.
   - View the **Full List** and use **Search** for filtering.

## Conclusion
CONHID is designed to simplify the process of managing large numbers of files, making it an essential tool for anyone who frequently handles bulk file operations. With its modern UI, robust features, and user-friendly design, CONHID streamlines file organization and improves productivity.

---

Feel free to update or expand on this document as needed. Enjoy using CONHID! 🚀
