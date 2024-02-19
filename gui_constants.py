import os, json, sys


with open("./gui_configs/client_config.json", "r") as f:
    data = json.load(f)

CURRENT_PATH = os.getcwd()
BIN_PATH = os.getcwd() + "bin_path"
LAUNCH_CLIENT_TYPE = data['client']
      
CURRENT_PYTHON_INTERPRETER = sys.executable

      
      