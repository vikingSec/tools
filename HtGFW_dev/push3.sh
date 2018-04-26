#!/bin/bash
cd /home/node3/GitHub/
sudo git pull tools master;
sudo git add --all;
sudo git commit -m "Node3 Push";
sudo git push tools;
