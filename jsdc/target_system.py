from abc import ABC, abstractmethod
from logging import getLogger


class TargetSystem(ABC):
    """Target system super class"""
    def __init__(self, target_name: str):
        self.target_name = target_name
        self._log = getLogger(self.target_name)

    @abstractmethod
    def get_target_type(self) -> str:
        pass

    @abstractmethod
    def send_data(self, sensor_type: str, sensor_data: dict) -> None:
        pass
