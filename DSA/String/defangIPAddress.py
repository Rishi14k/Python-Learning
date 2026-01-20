def defangIP(ip):
    return ip.replace(".","[.]")

print(defangIP("1.1.1.1.1"))