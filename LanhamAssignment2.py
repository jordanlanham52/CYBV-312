'''
 Assignment 2
 CYBV 312
 by Jordan Lanham
'''

import ipaddress

txt_str='''45.180.22.35
89.81.227.5
96.94.166.213
165.102.214.22
8.145.195.83
254.223.81.396
228.32.40.171
45.180.22.35
166.219.83.19
226.233.161.231
218.130.131.69
178.183.235.224
59.198.246.13
37.48.72.78
182.108.128.238
243.227.128.44
184.169.180.213
157.120.245.64
80.93.220.190
30.116.37.25
162.135.131.112
25.234.15.145
61.165.84.184
55.155.165.80
124.50.174.14
116.184.53.175
84.88.154.78
155.41.8.160
124.89.248.22
200.76.51.173
53.90.18.157
82.142.191.166
199.198.82.152
232.89.86.55
78.57.248.67
72.138.79.24
72.47.139.192
90.13.8.155
189.183.40.202
82.37.160.239
250.76.19.76
109.191.76.188
214.42.237.124
44.66.161.119
165.102.214.22
245.165.98.255
30.216.140.14
249.7.149.173
230.10.94.39
132.79.44.143
226.233.161.231
191.198.67.32
115.117.20.48
106.154.188.206
199.198.82.152
222.170.235.134
56.44.200.171
103.225.120.105
31.187.119.54
187.116.32.144
103.225.120.105
105.137.156.216
55.210.66.204
2.66.148.188
106.154.188.206
73.78.22.54
132.79.44.143
184.169.180.213
250.160.72.43
233.1.26.168
249.113.48.63
108.136.128.159
31.187.119.54
90.13.8.155
229.126.107.145
161.139.96.47
113.119.77.116
165.102.214.22
191.198.67.32
72.47.139.192
164.244.25.56
245.165.98.255
146.142.90.73
205.115.249.187
15.188.247.218
79.68.43.0
64.166.77.171
179.355.166.155
80.15.188.227
89.168.164.155
87.74.32.90
203.179.218.135
73.78.22.54
116.184.53.175
2.66.148.188
179.46.172.246
30.116.37.25
177.168.35.75
164.244.25.56
233.1.26.168
'''
#1. Write a state that displays display the content of txt_str
print(txt_str)
#2. Write a statement that displays the data type of txt_str
print(type(txt_str))
#3. Write a statement that displays the length of txt_str
print(len(txt_str))
#4. Create a list named ips that holds all the words within txt_str. (Hint: use the .split() method) 
ips = txt_str.split()
#5. Write a statement to display the total number of IP addresses in the ips list.
print(len(ips))
#6 Write a statement to display the first 10 IP addresses from the ips list.
print(ips[:10])
#7. Define a function is_valid_ip(ip: str)->bool to verify if an ip address is in a valid IPv4 format. 
def is_valid_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

#8. After you write the definition, call the function two time: one call returns True and the other returns False.  
#You should use function calls different from the hints
print(is_valid_ip('127.0.0.1'))
print(is_valid_ip('124.0.0.300'))
#9. Write code to display IP addresses in ips that are not in a valid IPv4 format.
invalid_ips = [ip for ip in ips if not is_valid_ip(ip)]
print(invalid_ips)
#10. Write statements to remove the invalid IP addresses from the  ips list.  And display the total number of IP addresses in the updated ips list.
ips = [ip for ip in ips if is_valid_ip(ip)]
print(len(ips))
#11. Convert the ips list into a set named unique_ips using the set() function to remove duplicate IP addresses.
unique_ips = set(ips)
#12. Write a statement to display the total number of unique IP addresses in the set.
print(len(unique_ips))
#13. Write code to display all unique IP addresses, sorted by their numeric values in ascending order. 
print(sorted(unique_ips, key=lambda ip: tuple(map(int, ip.split('.')))))
#For example, given the list ['192.168.1.1', '10.0.0.1', '172.16.0.1'],the sorted result should be ['10.0.0.1', '172.16.0.1', '192.168.1.1']

