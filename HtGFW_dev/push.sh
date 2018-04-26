#!/bin/bash
git pull tools master;
sudo git add --all;
sudo git commit -m "Node1 Push";
sudo git push tools_ssh >> ~/GitHub/HtGFW_dev/log_1.txt;
