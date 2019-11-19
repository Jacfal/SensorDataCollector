from typing import List

from sensor import Sensor
from sensors.dummy_sensor import DummySensor, dummy_sensor_type
from target_system import TargetSystem
from targets.null_target import NullTarget, null_target_type


def create_sensor_from_configuration(sensor_conf: dict) -> List[Sensor]:
    sensors: List[Sensor] = []

    for name in sensor_conf.keys():
        sensor_type: str = sensor_conf[name]['sensorType']

        if sensor_type == dummy_sensor_type:
            dummy = DummySensor()
            dummy.set_gathering_interval(sensor_conf[name]['gatheringInterval'])

            for target in sensor_conf[name]['targets']:
                dummy.add_target_system(target)
            sensors.append(dummy)
        else:
            raise ValueError(sensor_type + ": invalid sensor type")

    return sensors


def create_targets_from_configuration(target_conf: dict) -> List[TargetSystem]:
    targets: List[TargetSystem] = []

    for name in target_conf.keys():
        target_type: str = target_conf[name]['targetType']

        if target_type == null_target_type:
            targets.append(NullTarget(name))
        else:
            raise ValueError(target_type + ": invalid target type")

    return targets
