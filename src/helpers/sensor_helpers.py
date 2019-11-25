from typing import List
from sensor import Sensor
from sensors.dummy_sensor import DummySensor, dummy_sensor_type
from target_system import TargetSystem
from targets.influxdb_target import influxdb_target_type, InfluxDBTarget
from targets.log_target import LogTarget, log_target_type


def create_sensor_from_configuration(sensor_conf: dict, available_targets: List[TargetSystem]) -> List[Sensor]:
    sensors: List[Sensor] = []

    for name in sensor_conf.keys():
        sensor_type: str = sensor_conf[name]['sensorType']

        sensor: Sensor
        if sensor_type == dummy_sensor_type:
            sensor = DummySensor()
        else:
            raise ValueError(sensor_type + ": invalid sensor type")

        # add targets to the sensor
        for target in available_targets:
            if target.target_name in sensor_conf[name]['targets']:
                sensor.add_sensor_data_subscriber(target.send_data)

        sensor.set_gathering_interval(sensor_conf[name]['gatheringInterval'])
        sensors.append(sensor)

    return sensors


def create_targets_from_configuration(target_conf: dict) -> List[TargetSystem]:
    targets: List[TargetSystem] = []

    for name in target_conf.keys():
        target_type: str = target_conf[name]['targetType']

        if target_type == log_target_type:
            targets.append(LogTarget(name))
        elif target_type == influxdb_target_type:
            influx_hostname = target_conf[name]['hostname']
            influx_port = target_conf[name]['port']
            targets.append(InfluxDBTarget(name, influx_hostname, influx_port))
        else:
            raise ValueError(target_type + ": invalid target type")

    return targets
