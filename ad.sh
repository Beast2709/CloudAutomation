#!/bin/bash

sshpass -p redhat ssh -T -l root 192.168.43.86 -X docker run --net=host --env='DISPLAY' --volume='$HOME/.Xauthority:/root/.Xauthority:rw' xeyes:v1 firefox
