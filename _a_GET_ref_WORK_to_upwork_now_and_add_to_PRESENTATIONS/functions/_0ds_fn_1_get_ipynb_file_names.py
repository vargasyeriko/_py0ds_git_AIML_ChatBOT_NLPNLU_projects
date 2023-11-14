import os

def list_all_ipynb_files(folder_path):
    try:
        all_files = os.listdir(folder_path)
    except FileNotFoundError:
        return "Folder not found."
    
    ipynb_files = [f for f in all_files if f.endswith('.ipynb')]
    
    return ipynb_files
