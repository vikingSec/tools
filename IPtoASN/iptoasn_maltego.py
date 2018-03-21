from MaltegoTransform import *
import IPtoASN
import sys


val = sys.argv[1]
trx = MaltegoTransform()
trx.addEntity('maltego.AS',IPtoASN.getASN(val))
trx.returnOutput()
