
import os
import shutil

# Define the directory you want to organize
directory = os.path.expanduser('~/Downloads')

# Define extensions and their corresponding folder names
extensions = {
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".md",".epub"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".iso"},
    "Code": {".py", ".c", ".cpp", ".h", ".java", ".js", ".ts", ".html", ".css", ".json", ".sql", ".bat", ".ps1"}, 
    "Installers": {".exe", ".msi"},
}

# Count successfully relocated files
total_moved = 0

# Loop through every file using os.scandir()
with os.scandir(directory) as entries:
    for entry in entries:

        # Ensure it's a file, not a directory
        if entry.is_file():
            filename = entry.name
            file_path = os.path.join(directory, filename)

            # Extract the file extension and make it lowercase
            file_extension = os.path.splitext(filename)[1].lower()

            # Check if the extension is in our dictionary
            for folder_name, file_extensions in extensions.items():
                if file_extension in file_extensions:

                    folder_path = os.path.join(directory, folder_name)

                    # Create the folder if it doesn't already exist
                    os.makedirs(folder_path, exist_ok=True)

                    # Move the file into the designated folder
                    try:
                        destination = os.path.join(folder_path, filename)
                        shutil.move(file_path, destination)

                        # Increase count after successful move
                        total_moved += 1
                        print(f"Moved: {filename} -> {folder_name}")

                    except FileExistsError:
                        print(f"File already exists: {filename}")

                    except PermissionError:
                        print(f"Permission denied: {filename}")

                    except OSError as error:
                        print(f"Could not move {filename}: {error}")

                    break

# Print formatted execution summary
print("\n" + "=" * 35)
print("       FILE ORGANIZER SUMMARY")
print("=" * 35)
print(f"Directory organized : {directory}")
print(f"Total files moved   : {total_moved}")
print("=" * 35)
print("Organization complete!")
