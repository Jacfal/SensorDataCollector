from abc import ABC, abstractmethod


class TargetSystem(ABC):
    """Target system super class"""

    @abstractmethod
    def get_target_name(self) -> str:
        pass

    @abstractmethod
    def send_data(self, sensor_data: dict) -> None:
        pass
