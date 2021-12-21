# Metadata registry

## Getting started

1. Clone GitHub repository  
`https://github.com/sbilge/GHGA_APP.git`

2. Create conda environment from `environment.yml`  
`conda env create -f environment.yml`

3. Activate environment  
`conda activate ghga_app`

4. Start the flask app  
`python run.py`

5. To upload metadata, open a new terminal with ghga_app as conda environment  
`python import_data.py -f <JSON_FILE>`

6. View metadata on `http://localhost:5000/view`


Please note that, the application assumes there should be one JSON file per study. The JSON file should follow the same schema as the example file given [here](https://github.com/sbilge/GHGA_APP/blob/main/test_data/metadata.json)