import checker
import datetime

now = datetime.datetime.now()
f = open("./reports/Three_"+str((str(now)).replace(":","-"))+".txt", "w+")

print str(now)
check = checker.check()
print check

for line in check.split("\n"):
	f.write(line)

f.close()

