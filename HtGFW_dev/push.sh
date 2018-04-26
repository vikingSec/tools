#!/bin/bash
sudo git pull tools_ssh master;
sudo git add --all;
sudo git commit -m "Node1 Push";
sudo git push tools_ssh;
