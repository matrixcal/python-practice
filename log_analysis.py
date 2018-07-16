import collections
import json
import csv
ip_addrs=[]
requests=[]
with open("access_small.log","r") as fread:
    with open("output.txt","w") as fwrite:
        w=csv.writer(fwrite)
#Using Collection
        for line in fread:
            IP=line.split('- -')[0]
            dttm = line.split('- -')[1].split()[0]
            ip_addrs.append(IP)
            requests.append(dttm[13:18])
            freq=collections.Counter(ip_addrs)
            reqs_per_hour=collections.Counter(requests)
        fwrite.write(json.dumps(freq))
        w.writerow(freq)
        fwrite.write("\n")
        fwrite.write(json.dumps(reqs_per_hour))
print reqs_per_hour.items()
print freq.items()

#Dictoinary
#for line in lines:
#    ip1=line.split("- -")[0]

#    ips[ip1] = ips.get(ip1,0) + 1
#print ips
