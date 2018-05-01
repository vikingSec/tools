import checker3
import datetime

now = datetime.datetime.now()
f = open("./reports/Three_"+str((str(now))).split(" ")[0]+".txt", "w+")

print str(now)
check = checker3.check()
print check

for line in check.split("\n"):
	f.write(line+'\n')

f.close()

