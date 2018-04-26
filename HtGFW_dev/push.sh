#!/bin/bash
git pull tools_ssh
git add --all;
git commit -m "Node1 Push";
git push tools_ssh >> ~/GitHub/HtGFW_dev/log_1.txt;
