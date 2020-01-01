import json
from influxdb import InfluxDBClient
from socket import gethostname

from jsdc.target_system import TargetSystem

influxdb_target_type: str = "INFLUXDB_TARGET"


class InfluxDBTarget(TargetSystem):
    """Influxdb target"""

    influxdb_record = [
        {
            "measurement": None,
            "tags": {
                "host": gethostname()
            },
            "fields": {
            }
        }
    ]

    def __init__(self, target_name: str, host: str, port: int):
        super().__init__(target_name)

        self.__influx_client = InfluxDBClient(host=host, port=port)
        self.__create_sensor_database()

    def __create_sensor_database(self):
        self.__influx_client.create_database(self.target_name)

    def send_data(self, sensor_type: str, sensor_data: dict) -> None:
        self.influxdb_record[0]['measurement'] = sensor_type
        self.influxdb_record[0]['fields'] = sensor_data

        self._log.debug(f'Sending data to the influxDB => {sensor_type}: {sensor_data}')
        self.__influx_client.write_points(self.influxdb_record, database=self.target_name)

    def get_target_type(self):
        return influxdb_target_type
