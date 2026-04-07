# -*- coding: utf-8 -*-
"""
This script updates the slide type of all cells in a Jupyter notebook.
It can be used to set the slide type for all cells to a specific type, 
such as "slide", "subslide", "fragment", "skip", or "notes". 


Created on Wed Apr  9 15:01:37 2025

@author: fabian.woebbeking@iwh-halle.de
"""

  
import sys
import json
import os

def update_slide_type(filename, slide_type):
    # Define the valid slide types.
    valid_slide_types = ["slide", "subslide", "fragment", "skip", "notes"]
    
    # Check if the provided slide_type is valid.
    if slide_type not in valid_slide_types:
        print(f"Error: '{slide_type}' is not a valid slide type. Valid slide types are: {', '.join(valid_slide_types)}.")
        sys.exit(1)
    
    # Check if the file exists.
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    # Read the notebook file.
    try:
        with open(filename, "r", encoding="utf-8") as f:
            notebook = json.load(f)
    except Exception as e:
        print(f"Error reading '{filename}': {e}")
        sys.exit(1)
    
    # Ensure the notebook has cells.
    if "cells" not in notebook:
        print("Error: This notebook does not contain any cells.")
        sys.exit(1)
    
    # Update each cell's metadata.
    for cell in notebook["cells"]:
        # Ensure the 'metadata' field exists.
        if "metadata" not in cell:
            cell["metadata"] = {}
        # Ensure the 'slideshow' field exists.
        if "slideshow" not in cell["metadata"]:
            cell["metadata"]["slideshow"] = {}
        # Set the slide type.
        cell["metadata"]["slideshow"]["slide_type"] = slide_type
    
    # Write the updated notebook back to file.
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(notebook, f, indent=1)
    except Exception as e:
        print(f"Error writing to '{filename}': {e}")
        sys.exit(1)
    
    print(f"Notebook '{filename}' updated: all cells set to slide_type '{slide_type}'.")



def append_conversion_cell(filename):
    """
    Check if a conversion cell exists in the notebook. If not, prompt the user to add a
    conversion cell (which includes code that converts the notebook to html slides). The
    conversion cell will have the slide type 'skip'.
    """
    conversion_keyword = "jupyter nbconvert"
    
    # Read the notebook.
    try:
        with open(filename, "r", encoding="utf-8") as f:
            notebook = json.load(f)
    except Exception as e:
        print(f"Error reading '{filename}': {e}")
        sys.exit(1)
    
    if "cells" not in notebook:
        print("Error: This notebook does not contain any cells.")
        sys.exit(1)
    
    # Check if a conversion cell already exists.
    conversion_exists = False
    for cell in notebook["cells"]:
        if cell.get("cell_type", "") == "code":
            source = cell.get("source", "")
            # source may be a list or a string
            source_str = "".join(source) if isinstance(source, list) else source
            if conversion_keyword in source_str:
                conversion_exists = True
                break

    if conversion_exists:
        print("A conversion cell already exists. No additional cell was added.")
    else:
        # Prompt the user whether to add the conversion cell.
        answer = input("No conversion cell found. Do you want to add a conversion cell to the notebook? (Y/n): ")
        if answer.strip().lower() in ('y', 'yes', ''):
            # Create the conversion cell.
            conversion_cell_source = [
                "# This converts the notebook to html slides\n",
                "import os\n",
                "local_dir = %pwd\n",
                "os.system(f'jupyter nbconvert {local_dir}/" + filename + " --to slides --output-dir=html --SlidesExporter.reveal_scroll=True')\n"
            ]
            conversion_cell = {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {
                    "slideshow": {
                        "slide_type": "skip"
                    }
                },
                "outputs": [],
                "source": conversion_cell_source
            }
            # Append the conversion cell to the list of cells.
            notebook["cells"].append(conversion_cell)
            print("Conversion cell added.")
        else:
            print("Conversion cell was not added.")

    # Write the updated notebook back to file.
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(notebook, f, indent=1)
    except Exception as e:
        print(f"Error writing to '{filename}': {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Check for the required filename argument.
    if len(sys.argv) < 2:
        print("Usage: python slidetype.py filename.ipynb [slide_type]")
        sys.exit(1)
    
    filename = sys.argv[1]
    # Default to "subslide" if no slide_type is provided.
    slide_type = sys.argv[2] if len(sys.argv) > 2 else "subslide"
    
    update_slide_type(filename, slide_type)
    append_conversion_cell(filename)

    