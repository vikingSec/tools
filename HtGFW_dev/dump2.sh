cd "${0%/*}"
sudo python dump2.py
sleep 7200
sudo ./dump.sh
echo "Sleep!"
