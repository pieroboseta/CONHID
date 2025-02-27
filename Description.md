# CONHID: Bulk File Renamer

## Overview
**CONHID** is an advanced and user-friendly bulk file renaming tool designed to simplify and customize the process of organizing large collections of files. With a modern, sleek interface and enhanced features, CONHID now offers the flexibility to set custom naming formats and load a list of custom names, in addition to its core functionalities like bulk renaming and restoration. Whether you're managing media libraries, organizing documents, or performing routine file maintenance, CONHID adapts to your workflow with ease.

## What It Does
CONHID is built with several key functionalities:
- **Bulk Renaming:** Automatically renames all files in a selected folder using either a custom list of names (loaded from a JSON file) or a default sequential format (e.g., `document-1.bin`, `document-2.bin`, etc.) with a user-defined prefix and extension.
- **Custom Naming Options:** Set your own file name prefix and file extension through the new **Prefix** feature.
- **Load Custom Name List:** Optionally load a JSON file containing a list of custom file names to be used for renaming, providing greater control over the process.
- **Restoration:** Easily restore files to their original names using a saved rename history.
- **Search Functionality:** Quickly search through both renamed and restored files using keywords.
- **Logging System:** Every renaming operation is logged in a JSON file (`conhid.json`), ensuring that changes are tracked and can be reverted if necessary.
- **Modern Aesthetic:** The GUI features a dark-themed interface with uniform buttons for a visually appealing and intuitive experience.

## How It Works
1. **Select a Folder:**
   - Click the **Select** button to open a dialog and choose the folder containing the files you want to manage.
2. **Set Custom Prefix & Extension:**
   - Click the **Prefix** button to set your desired file name prefix and file extension.
3. **Load Custom Name List (Optional):**
   - Click the **Add List** button to load a JSON file containing custom file names. If loaded, CONHID uses these names for renaming; otherwise, it falls back to the default naming format.
4. **Rename Files:**
   - Click the **Rename** button to bulk rename files using either the loaded list or the specified prefix with sequential numbering.
5. **Restore Files:**
   - If you need to revert the changes, click the **Restore** button. CONHID reads the rename history from `conhid.json` and renames the files back to their original names.
6. **View & Search:**
   - Click **Full List** to view all file renaming operations.
   - Use the **Search** function to quickly locate files by name.

## Features & Benefits
| Feature                   | Description                                                                                                      | Use Cases                                                 |
|---------------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| **Bulk Renaming**         | Renames files with a customizable naming format using either a list of names or a default sequential pattern.      | Organizing media libraries or document archives.          |
| **Custom Naming Options** | Set a custom prefix and file extension to match your naming conventions.                                          | Personalizing file names to suit specific projects.       |
| **Load Custom Name List** | Import a JSON file containing custom file names to apply specific naming orders.                                  | Tailoring file names for detailed organizational needs.   |
| **Restore Function**      | Reverts files to their original names using saved history.                                                       | Undo accidental renames quickly and efficiently.          |
| **Full List View**        | Displays a sortable table of files, showing both original and new names.                                          | Reviewing all file changes in one place.                  |
| **Search Functionality**  | Filters files based on keywords in original or renamed file names.                                                | Quickly locating specific files among many.               |
| **Logging System**        | Tracks every renaming operation in a JSON log (`conhid.json`) for auditability and reversibility.                   | Ensuring data integrity and change traceability.          |
| **Modern UI**             | Features a dark-themed, intuitive interface that enhances usability and reduces visual clutter.                     | Improving user experience across various workflows.       |

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
   - Click **Prefix** to set your custom file name prefix and extension.
   - (Optional) Click **Add List** to load a JSON file with custom names.
   - Click **Rename** to apply the new file names.
   - Click **Restore** to revert changes if needed.
   - Use **Full List** and **Search** to review and locate files.

## Conclusion
CONHID streamlines bulk file management with added customization options, making it an essential tool for anyone who frequently handles file renaming tasks. Enjoy a more personalized and flexible approach to organizing your files with CONHID! 🚀
