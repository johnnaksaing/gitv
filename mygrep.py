import sys
from commands import getstatusoutput as comm1

def doGrep(filePattern, grep):
	test_list = comm1('git ls-files ' + comm1('git rev-parse --show-toplevel')[1])[1].split('\n')
	
	for fileName in test_list :
		if filePattern in fileName :
			f = open(fileName, 'r')
			c=f.read()
			f.close()
			i = 1
			for line in c.split('\n') :
				if grep in line :
					print fileName + ':' + str(i) + ':' + line.strip()
				i = i+1

if len(sys.argv) != 4 :
	print 'argument not good.'
else :
	doGrep(sys.argv[2], sys.argv[3])
