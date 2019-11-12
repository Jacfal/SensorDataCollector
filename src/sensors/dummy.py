from src.sensor import Sensor


class Dummy(Sensor):
    def get_sensor_name(self):
        return "DUMMY_SENSOR"

    def get_sensor_data(self):
        # create dummy data
        return {
            "value_1": "1",
            "value_2": "2",
            "value_3": "3"
        }
