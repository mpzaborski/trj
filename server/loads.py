# This file contains all the configurations and functions that are
# needed to load and parse the files. For example the configuration 
# file.
import yaml

def load_configuration():
    """
    This function is used to load the configuration (~/configuration.yaml)
    using the YAML Python module.

    Returns
    -------
    configuration: structure
        The Yaml file setted up as a structure.
    """
    route = "../configuration.yaml"
    with open(route) as f:
        return yaml.load(f, Loader=yaml.FullLoader())

if __name__ == "__main__":
    print(load_configuration())