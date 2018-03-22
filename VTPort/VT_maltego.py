import VirusTotal
import sys
from MaltegoTransform import MaltegoTransform



val = sys.argv[1]
lists = VirusTotal.checkIP(val)


detected = lists[0]

trx = MaltegoTransform()

for detect in detected:
    trx.addEntity('maltego.Domains',detect)

trx.returnOutput()
