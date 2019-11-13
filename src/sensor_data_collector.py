from Helpers.sensor_helpers import create_sensor_from_configuration
from src.configuration import Configuration


def main():
    sensor_configuration = Configuration.load_sensor_configuration()

    for conf in sensor_configuration:
        create_sensor_from_configuration()

    raise NotImplementedError


if __name__ == "__main__":
    main()
