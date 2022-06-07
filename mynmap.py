import re
import nmap

scanner = nmap.PortScanner()
target= input('please enter : ')
scanner.scan(target,'1-1024','-sV')

print("the host is : " + scanner[target].hostname())
print("the host status :" + scanner[target].state())

keys =scanner[target]['tcp'].keys()
for i in keys:
    print('..............')
    print('the port :' + str (i)+ ":")
    res = scanner[target]['tcp'][i]
    for re in res :
            print(re + " : " +res[re])



