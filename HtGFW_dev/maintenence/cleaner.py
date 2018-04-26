import os
f = open('./topics.txt','r')
for line in f:
	
	line = line.strip()
	if not os.path.exists('./'+line.strip()):
		os.makedirs('./'+line.strip())
	    	print line
