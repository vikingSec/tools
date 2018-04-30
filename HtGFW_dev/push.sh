#!/bin/bash
cd /home/ubuntu/GitHub/
git pull tools_ssh master;
git add --all;
git commit -m "Node1 Push";
git push tools_ssh;
