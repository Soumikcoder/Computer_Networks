print('Enter ip Address:',end='')
[ip_addr,net_id]=input().split('/')
net_id=int(net_id)
temp=net_id
mas=((1<<net_id)-1)<<(32-net_id)
mask=[(mas>>((3-i)*8))&255 for i in range(4)]
ip_addr=[int(i) for i in ip_addr.split('.')]
mask_addr='.'.join(str(mask[i]) for i in range(len(mask)))
print('Network mask:',mask_addr)
start_addr='.'.join(str(mask[i]&ip_addr[i]) for i in range(len(mask)))
print('Starting Address:',start_addr)
end_addr='.'.join(str(((mask[i]^255)|ip_addr[i])) for i in range(len(mask)))
print('Ending Address:',end_addr)
print("No of Address in that block:",1<<(32-net_id))