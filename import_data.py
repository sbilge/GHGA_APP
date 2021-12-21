import argparse
import os
import sys
import json
import requests
import jsonschema
from jsonschema import validate


# Json file structure description
metadata_schema = {
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "sample": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "donor_age": {
              "type": "integer"
            },
            "donor_sex": {
              "type": "string"
            },
            "tissue_type": {
              "type": "string"
            },
            "experiment": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "experiment_type": {
                      "type": "string"
                    },
                    "file": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "file_name": {
                              "type": "string"
                            },
                            "size": {
                              "type": "integer"
                            },
                            "checksum": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "file_name",
                            "size",
                            "checksum"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "experiment_type",
                    "file"
                  ]
                }
              ]
            }
          },
          "required": [
            "donor_age",
            "donor_sex",
            "tissue_type",
            "experiment"
          ]
        }
      ]
    }
  },
  "required": [
    "name",
    "description",
    "sample"
  ]
}

def validateJson(data):
    """Function to check validity of the json schema. input: json object, output: boolean"""
    try:
        validate(instance=data, schema=metadata_schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


def check_extension(filename):
    """Function to check the extension of the input file. input: path_to_file"""
    ext = os.path.splitext(filename)[1][1:]
    if ext != 'json':
       my_parser.error("file doesn't end with .json")
    return filename



# Create the parser
my_parser = argparse.ArgumentParser(prog='import_data', usage='%(prog)s [options] path_to_metadata_json', description='Import metadata from a JSON file')


# Add the argument for json file. also checks for the input file's extension
my_parser.add_argument('-f', '--file', type=lambda s:check_extension(s) , help='path to JSON file', required=True)

# Parse the arguments
args = my_parser.parse_args()

# Input file to a variable
input_file = args.file


# Check if the input file exists
if not os.path.isfile(input_file):
    print('The file specified does not exist')
    sys.exit()

# Check if file is empty
if os.stat(input_file).st_size == 0:
    print('The file specified is empty')
    sys.exit()


# Read JSON file  
with open(input_file, 'r') as f:
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError as err:
        print("Invalid JSON")
        sys.exit()

# Get the validity status of the JSON object
validity = validateJson(data)

if validity:   
    # Post request to flask
    url = 'http://localhost:5000/metadata'

    r = requests.post(url, json=data)
    print(r.status_code, r.reason)

else:
    print('JSON schema is not valid.')
    sys.exit()