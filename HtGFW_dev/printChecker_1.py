import checker
import datetime

now = datetime.datetime.now()
f = open("./reports/One_"+str(now)+".txt", "w+")

print str(now)
check = checker.check()
print check

for line in check.split("\n"):
	f.write(line)

f.close()

