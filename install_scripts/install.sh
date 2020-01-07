CONFIG_DIR="/etc/jsdc/"
REPO_URL="https://github.com/Jacfal/SensorDataCollector.git"
REPO_CLONE_PATH="/tmp/jsdc_tmp"

printf "Installing jsdc\n"
git clone $REPO_URL $REPO_CLONE_PATH

# install package
printf "Installing python package via pip...\n"
pip install -r /tmp/jsdc_tmp/requirements.txt $REPO_CLONE_PATH

#creating configuration
printf "Adding configuration...\n"
sudo mkdir $CONFIG_DIR
sudo wget -P $CONFIG_DIR https://raw.githubusercontent.com/Jacfal/SensorDataCollector/master/jsdc/config.yml

# install service
printf "Installing services...\n"
sudo wget -P /etc/systemd/system/ https://raw.githubusercontent.com/Jacfal/SensorDataCollector/master/jsdc/install_scripts/jsdc.service

#cleaning
rm -rf $REPO_CLONE_PATH

printf "Installation complete\n"