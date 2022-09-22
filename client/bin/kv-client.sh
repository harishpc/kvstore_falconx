#!/bin/#!/usr/bin/env bash
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
printf "${YELLOW}At any point to exit from the cli type ${GREEN}ctrl+c${NC} ${YELLOW} to exit from shell ${YELLOW} "
echo ""
echo "--------------------------------------------------------------------------------------------------------"
echo ""
echo ""

while :
do
  if [[ ${command_input[0]} == 'exit' ]] || [[ ${command_input[0]} == 'EXIT' ]]
  then
      exit;
  else
 	read command_array
  command_input=( $command_array )

  if [[ ${command_input[0]} == 'get' ]]
  then
    echo ""
    python ../src/get.py ${command_input[0]} ${command_input[1]}
    echo ""
  elif [[ ${command_input[0]} == 'getall' ]]
  then
    echo ""
    python ../src/getall.py ${command_input[0]}
    echo ""
  elif [[ ${command_input[0]} == 'set' ]]
  then
    echo ""
    python ../src/set.py ${command_input[0]} ${command_input[1]} ${command_input[2]}
    echo ""
  elif [[ ${command_input[0]} == 'del' ]]
  then
    echo ""
    python ../src/del.py  "rem" ${command_input[1]}
    echo ""
  elif [[ ${command_input[0]} == 'subs' ]]
  then
    echo ""
    python ../src/subscribe.py ${command_input[0]}  ${command_input[1]}
    echo ""
  elif [[ ${command_input[0]} == 'put' ]]
  then
    echo ""
    python ../src/put.py  ${command_input[0]} ${command_input[1]} ${command_input[2]}
    echo ""
  elif [[ ${command_input[0]} == 'suball' ]]
  then
    echo ""
    python ../src/suball.py  ${command_input[0]}
    echo ""
  elif [[ ${command_input[0]} == '-v' ]] || [[ ${command_input[0]} == '--version' ]]
  then
    echo ""
    python ../src/client.py ${command_input[0]}
  else
    echo ""
    python ../src/client.py -h
    echo ""
  fi


fi
done
