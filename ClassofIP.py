import socket as sock
hostname=sock.gethostname()
ip_addr='192.168.0. ip1'
print("Your computer Name is :"+hostname)
print("Your ip Address is:"+ip_addr)
ip=[int(i) for i in ip_addr.split('.')]
if len(ip) != 4:
    print('Not valid!')
    exit(1)
ip_bin=[]
for i in range(len(ip)):
    end_point='.'
    if i == len(ip)-1:
        end_point='\n'
    ip_bin.append('{0:07b}'.format(ip[i]))
    print(ip_bin[-1],end=end_point)

if ip_bin[0][0]=='0' :
    print('Class A')
elif ip_bin[0][0:2]=='10' :
    print('Class B')
elif ip_bin[0][0:3]=='110':
    print('Class C')
elif ip_bin[0][0:4]=='1110':
    print('Class D')
else:
    print('Class E')
