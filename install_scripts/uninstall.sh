CONFIG_DIR="/etc/jsdc/"

printf "Removing jsdc\n"

# removing services
printf "Stopping services...\n"
sudo systemctl stop jsdc
sudo rm /etc/systemd/system/jsdc.service

printf "Removing services...\n"

#removing configuration
printf "Removing configuration...\n"
sudo rm -rf $CONFIG_DIR

#removing package
printf "Removing package..."
pip uninstall jacfal-sensor-data-collector

printf "Removing complete\n"