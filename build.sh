#!/bin/#!/usr/bin/env bash
# ----------------------------------
# Colors
# ----------------------------------
NOCOLOR='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
LIGHTGRAY='\033[0;37m'
DARKGRAY='\033[1;30m'
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
YELLOW='\033[1;33m'
LIGHTBLUE='\033[1;34m'
LIGHTPURPLE='\033[1;35m'
LIGHTCYAN='\033[1;36m'
WHITE='\033[1;37m'
image_name="kv-server:latest"
container_name="key-value-server"
printf "${YELLOW}The following script will setup both the ${GREEN}CLIENT${NC} ${YELLOW}and${YELLOW} ${GREEN}SERVER${NC} ${YELLOW}for you ${YELLOW} \

 ${WHITE}--------------------------------------------------------------------------------------------------------${WHITE} \

${PURPLE} 1 . To Setup Server \

${PURPLE} 2 . To Setup Client"
echo ""
read -p "Enter your choice :   "
if [[  $REPLY == 1 ]]
then
  if [ "$(docker ps -a -q -f name=$container_name)" ]
   then
    echo "Image already running"
  else
  docker build -t $image_name .
  docker run -itd -p 8080:5000 --name $container_name $image_name
fi
elif [[ $REPLY == 2 ]]
then
  pyv="$(python -c "import sys; print(sys.version_info.major)")"
  if [[ $pyv == 2 ]]
  then
    pip install virtualenv
    virtualenv client/vnev
    source client/vnev/bin/activate
    pip install -r client/requirements.txt
    cd client/bin/
    bash kv-client.sh
  elif [[ $pyv == 3 ]]
  then
    python3 -m venv client/venv
    source client/venv/bin/activate
    pip install -r client/requirements.txt
    cd client/bin/
    bash kv-client.sh
  else
    echo "Not able to detect python versions"
  fi
else
  printf ${CYAN}"Only Numeric Values are allowed and the allowed values are 1 and 2"${CYAN}
fi
