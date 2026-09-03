'''x = 42 
print(type(x))
print(isinstance(x, int))'''

#integer value
'''p = 125
print(p + 25)
print(p // 10)
print(p % 10)
print(2 ** 8)'''

# float
'''M = 12.89
print(round(M, 1))
print(abs(-3.5))'''

# complex
'''z = 3 + 4j
print(z.real)     #REAL NUMBER
print(z.imag)     #IMAGENARY NUMBER
print(z.conjugate())'''

# complex
'''a, b = 17, 5
print(a / b)
print(a // b)
print(a % b)
print(divmod(a,b))'''

# conversion
'''print(int(12.9))
print(float("3.14"))
print(complex(2, 5))'''

# Boolean Type
'''is_auth = True
failed_attempts = 4
print(failed_attempts > 3)  #TRUE
print(is_auth and failed_attempts < 5)  #TRUE
print(not is_auth)'''  #FALSE

# True-value conversion
'''print(bool(0))   #FALSE
print(bool(""))   #FALSE
print(bool([]))    #FALSE
print(bool("admin"))'''  #TRUE

# String Type
'''prot = "HTTPS"
print(prot[0])  #H
print(prot[-1])  #S
print(prot[1:4])    #TTP
print(prot + " traffic")    #HTTPS TRAFFIC
print("T" in prot)    #TRUE
print(prot.lower())   #https
print(prot.upper())'''   #HTTPS

'''log = " ALERT: Suspicious VPN traffic "
print(log.strip())
print(log.lower())
print(log.replace("VPN", "Proxy"))
print(log.split())
print("-".join(["tcp", "443"]))
print(log.count("s"))
print(log.find("VPN"))
print(log.startswith(" ALERT"))'''

'''ip = "192.168.1.10"
octets = ip.split(".")
print(octets)'''

'''user, role = "Rohit:Admin" .split(":")
print(f"User={user}, Role={role}")'''