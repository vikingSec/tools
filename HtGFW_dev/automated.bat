#!/bin/sh
:baloop
	cd C:\Users\mgedw\Documents\GitHub\tools\HtGFW_dev

	git add .
	git commit -am "made changes"
	git push
	echo done!
	TIMEOUT 600
goto loop