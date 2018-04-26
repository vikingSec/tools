#!/bin/bash
cd /home/node1/GitHub/
sudo git pull tools master;
sudo git add --all;
sudo git commit -m "Node1 Push";
sudo git push tools;
