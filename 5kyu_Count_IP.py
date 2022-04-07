# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).
# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.
# Examples
# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246

def ips_between(start, end):
    r = []
    start = start.split('.')
    end = end.split('.')
    count = 1
    for i in range(3,-1,-1):
        r.append((int(end[i]) - int(start[i]))*count)
        count *= 256
    return sum(r)
