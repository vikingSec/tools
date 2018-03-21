import VirusTotal
import sys
from MaltegoTransform import MaltegoTransform



val = sys.argv[1]
lists = VirusTotal.checkIP(val)

domains = lists[0]
detected = lists[1]

trx = MaltegoTransform()

for domain in domains:
    trx.addEntity('maltego.Domains',domain)

for detect in detected:
    trx.addEntity('maltego.Domains',detect)

trx.returnOutput()
