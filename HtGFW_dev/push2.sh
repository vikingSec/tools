#!/bin/bash
cd /home/node2/GitHub/
sudo git pull tools master;
sudo git add --all;
sudo git commit -m "Node2 Push";
sudo git push tools master;
sudo ./check2.sh
