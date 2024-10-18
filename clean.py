import os

def rename_folders(directory):
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        # Check if it's a directory and contains "велико" or "Велико"
        if os.path.isdir(folder_path) and ("велико" in folder_name or "Велико" in folder_name):
            # Create the new folder name by removing "велико" or "Велико"
            new_folder_name = folder_name.replace("велико", "").replace("Велико", "").strip()
            new_folder_path = os.path.join(directory, new_folder_name)

            try:
                # Rename the folder
                os.rename(folder_path, new_folder_path)
                print(f"Renamed: '{folder_name}' -> '{new_folder_name}'")
            except Exception as e:
                print(f"Error renaming '{folder_name}': {e}")

if __name__ == "__main__":
    # Replace with the path to the directory you want to scan
    target_directory = "./"  
    rename_folders(target_directory)

