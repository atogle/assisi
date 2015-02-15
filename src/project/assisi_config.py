import os
import yaml


def get_config(filename):
    cwd = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(cwd, filename)
    config_file = open(filepath)
    try:
        config_yml = yaml.load(config_file)
    finally:
        config_file.close()

    return config_yml
