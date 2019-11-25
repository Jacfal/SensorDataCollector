from target_system import TargetSystem

log_target_type = "LOG_TARGET"


class LogTarget(TargetSystem):
    """Purpose of this target is of logging sensor values"""

    def send_data(self, sensor_type: str, sensor_data: dict) -> None:
        self._log.debug(f'Received data => {sensor_type}: {sensor_data}')

    def get_target_type(self):
        return log_target_type

