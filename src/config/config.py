''' configuration settings including path to data files
    OUTPUT: 
        parent directory of project
        path to data files
'''

from pathlib import Path

project_dir = Path(__file__).resolve().parents[2]
data_dir = project_dir.joinpath("data")