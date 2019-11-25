import json
from influxdb import InfluxDBClient
from socket import gethostname

from target_system import TargetSystem

influxdb_target_type: str = "INFLUXDB_TARGET"
influxdb_record: dict = {
    "measurement": None,
    "tags": {
        "host": gethostname()
    }
}


class InfluxDBTarget(TargetSystem):
    """Influxdb target"""

    def __init__(self, target_name: str, host: str, port: int):
        super().__init__(target_name)

        self.__influx_client = InfluxDBClient(host=host, port=port)
        self.__create_sensor_database()

    def __create_sensor_database(self):
        self.__influx_client.create_database(self.target_name)

    def send_data(self, sensor_type: str, sensor_data: dict) -> None:
        influxdb_record['measurement'] = sensor_type
        influxdb_record['fields'] = sensor_data

        self._log.debug(f'Sending data to the influxDB => {sensor_type}: {sensor_data}')
        self.__influx_client.write_points(json.dumps(influxdb_record))

    def get_target_type(self):
        return influxdb_target_type
