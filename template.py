import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "Chest_Disease"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/constant/training_pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/entity/artifact_entity.py",
    f"src/{project_name}/ml/__init__.py",
    f"src/{project_name}/ml/model/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/cloud_storage/__init__.py",
    "main.py",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "bento.yaml",
]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory; {filedir} for the file:  {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
            
    else:
         logging.info(f"{filename} already exists ")       
