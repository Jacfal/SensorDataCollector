# SensorDataCollector

Simple data collector, which collects data from rpi sensors and saving them to predefined target.
Can act as a mediation app between sensors and target databases. 

### Supported sensors

* bmp280 (BMP280_SENSOR)

### Supported targets

* influxdb (INFLUXDB_TARGET)

## Installation

```
bash <(curl -Ss https://raw.githubusercontent.com/Jacfal/SensorDataCollector/master/install_scripts/install.sh)
systemctl enable jsdc
systemctl start jsdc
```

## Configuration

By default is the config file at path `/etc/jsdc/config.yml`. A simple example of the config file with bmp280 sensor and influx target
should look like this:

```yaml
sensor:
  dummySensor:
    sensorType: "BMP280_SENSOR"
    port: 1
    address: 0x76
    gatheringInterval: 30
    targets:
      - influxDb

target:
  influxDb:
    targetType: "INFLUXDB_TARGET"
    hostname: "localhost"
    port: 8086

```

## Uninstallation

```
bash <(curl -Ss https://raw.githubusercontent.com/Jacfal/SensorDataCollector/master/install_scripts/install.sh)
```
