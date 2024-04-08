import os


def remove_files_except_pdf(folder_path):
    try:
        # Iterate through all files and directories in the folder
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                file_path = os.path.join(root, filename)

                # Check if the file is not a PDF
                if not filename.endswith('.pdf'):
                    try:
                        # Try to remove the file
                        os.remove(file_path)
                        print(f"Removed: {file_path}")
                    except Exception as e:
                        print(f"Failed to remove {file_path}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
folder_path = "C:/Users/User/Desktop/test"
remove_files_except_pdf(folder_path)