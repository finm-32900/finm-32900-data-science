"""Load project configurations from .env files.
Provides easy access to paths and credentials used in the project.
Meant to be used as an imported module.

If `config.py` is run on its own, it will create the appropriate
directories.

For information about the rationale behind decouple and this module,
see https://pypi.org/project/python-decouple/

Note that decouple mentions that it will help to ensure that
the project has "only one configuration module to rule all your instances."
This is achieved by putting all the configuration into the `.env` file.
You can have different sets of variables for difference instances, 
such as `.env.development` or `.env.production`. You would only
need to copy over the settings from one into `.env` to switch
over to the other configuration, for example.

"""
from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / config('DATA_DIR', default='./data/', cast=Path)
OUTPUT_DIR = BASE_DIR / config('OUTPUT_DIR', default='./output/', cast=Path)
BUILD_DIR = BASE_DIR / config('BUILD_DIR', default='./_build/', cast=Path)
WRDS_USERNAME = config("WRDS_USERNAME", default="")

# TEMP: For backwards compatibility
data_dir = DATA_DIR
output_dir = OUTPUT_DIR

if __name__ == "__main__":
    
    ## If they don't exist, create the data and output directories
    (DATA_DIR / 'pulled').mkdir(parents=True, exist_ok=True)

    # Sometimes, I'll create other folders to organize the data
    # (DATA_DIR / 'intermediate').mkdir(parents=True, exist_ok=True)
    # (DATA_DIR / 'derived').mkdir(parents=True, exist_ok=True)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
