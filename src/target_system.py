from abc import ABC, abstractmethod


class TargetSystem(ABC):
    @abstractmethod
    def get_target_name(self):
        pass
