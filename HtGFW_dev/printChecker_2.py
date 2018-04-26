import checker
import datetime

now = datetime.datetime.now()
f = open("./reports/Two_"+str((str(now)).replace(":","-"))+".txt", "w+")

print str(now)
check = checker2.check()
print check

for line in check.split("\n"):
	f.write(line)

f.close()

