
from nbconvert import NotebookExporter
import nbformat

# Initialize NotebookExporter
exporter = NotebookExporter()

# Read the notebook using nbformat
notebook_content = nbformat.read(notebook_file, as_version=4)

# Export the notebook into a different format
exported_content, resources = exporter.from_notebook_node(notebook_content)

# Write the exported content to a file
with open(f'{direc}/{output_file}', 'wb') as f:
    f.write(exported_content.encode('utf-8'))
