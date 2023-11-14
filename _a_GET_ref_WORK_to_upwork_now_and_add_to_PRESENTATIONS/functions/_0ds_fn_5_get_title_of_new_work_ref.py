
import json

def get_first_markdown_title(notebook_path):
    with open(notebook_path, 'r') as f:
        notebook_data = json.load(f)

    for cell in notebook_data['cells']:
        if cell['cell_type'] == 'markdown':
            source = cell['source']
            for line in source:
                if line.startswith('#'):
                    return line.strip()[2:].strip()
