# File Organizer

A simple Python script that tidies up a folder by sorting loose files into subfolders based on their file type.

## What It Does

The script scans a target directory and moves each file into a category folder that matches its extension. Category folders are created automatically the first time they are needed.

| Folder | Extensions |
|--------|------------|
| **Documents** | `.pdf` `.doc` `.docx` `.txt` `.rtf` `.odt` `.xls` `.xlsx` `.ppt` `.pptx` `.csv` `.md` `.epub` |
| **Images** | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg` `.webp` `.tiff` `.ico` |
| **Videos** | `.mp4` `.mkv` `.avi` `.mov` `.wmv` `.flv` `.webm` |
| **Archives** | `.zip` `.rar` `.7z` `.tar` `.gz` `.iso` |
| **Code** | `.py` `.c` `.cpp` `.h` `.java` `.js` `.ts` `.html` `.css` `.json` `.sql` `.bat` `.ps1` |
| **Installers** | `.exe` `.msi` |

When it finishes, it prints a summary showing the organized directory and the total number of files moved.

## Requirements

- Python 3.6 or newer
- No third-party packages (uses only `os` and `shutil` from the standard library)

## Usage

1. Open `organizer.py` and set the folder you want to organize:

   ```python
   directory = os.path.expanduser('~/Documents')
   ```

   `~` expands to your user folder (for example `C:\Users\YourName`). Other common choices:

   ```python
   directory = os.path.expanduser('~/Downloads')
   directory = os.path.expanduser('~/Desktop')
   ```

2. Run the script:

   ```bash
   python organizer.py
   ```

3. Check the output. Each moved file is logged like this:

   ```
   Moved: report.pdf -> Documents
   Moved: photo.jpg -> Images
   ```

## Example Output

```
Moved: resume.pdf -> Documents
Moved: vacation.png -> Images
Moved: setup.exe -> Installers

===================================
       FILE ORGANIZER SUMMARY
===================================
Directory organized : C:\Users\YourName/Downloads
Total files moved   : 3
===================================
Organization complete!
```

## Customization

To add or change categories, edit the `extensions` dictionary:

```python
extensions = {
    "Audio": {".mp3", ".wav", ".flac"},   # new category
    "Images": {".jpg", ".png", ".heic"},  # add an extension
}
```

Extensions must be lowercase and include the leading dot.

## How It Works

1. Lists the contents of the target directory using `os.scandir()`.
2. Skips anything that is not a file, so existing folders are left alone.
3. Lowercases the file extension so `PHOTO.JPG` and `photo.jpg` are treated the same.
4. Looks up the extension in the `extensions` dictionary.
5. Creates the destination folder if needed, then moves the file with `shutil.move()`.
6. Handles `PermissionError`, `FileExistsError`, and other `OSError` cases by printing a message and continuing with the next file.

## Notes and Limitations

- **Only top-level files are moved.** Files already inside subfolders are not touched.
- **Unknown extensions are left in place.** Files with no matching category stay where they are.
- **Duplicate names:** if a file with the same name already exists in the destination, behavior depends on your operating system. On Windows the move may fail with an error rather than overwrite. Consider renaming duplicates (for example `report_1.pdf`) if this matters for your files.
- **Moves are not automatically undoable.** Test on a copy of your folder first, especially when pointing the script at an important directory.
- **The script moves itself** if it is located inside the target directory, since `.py` files belong to the Code category. Run it from a different folder, or add a check to skip it.

## Troubleshooting

**`FileNotFoundError: The system cannot find the path specified`**
The `directory` path does not exist. Check the spelling (for example `Documents`, not `Doccument`) and confirm the folder is actually there.

**`PermissionError`**
The file may be open in another program, or you may not have access to the folder. Close the file and try again.

## License

Free to use and modify for personal or educational purposes.