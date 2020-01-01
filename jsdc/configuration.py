from os import environ
from typing import List
import yaml


def load_sensor_configuration() -> dict:
    # only conf loading from env is supported at this time
    return load_sensor_configuration_from_yaml()


def load_sensor_configuration_from_yaml() -> dict:
    return load_configuration_yaml()['sensor']


def load_target_configuration() -> dict:
    # only conf loading from yaml is supported at this time
    return load_target_configuration_from_yaml()


def load_target_configuration_from_yaml() -> dict:
    return load_configuration_yaml()['target']


def load_configuration_yaml() -> dict:
    with open('config.yml', 'r') as config_file:
        cfg = yaml.load(config_file)
    return cfg
