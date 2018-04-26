import checker
import datetime

now = datetime.datetime.now()
f = open("./reports/"+str(now)+".txt", "w+")

print str(now)
check = checker.check()
print check

for line in check.split("\n"):
	f.write(line)

f.close()

