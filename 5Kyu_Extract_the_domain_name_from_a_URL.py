# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    my = url.replace('http://', '')
    my = my.replace('https://', '')
    ar = my.split('/')
    b = ar[0]
    if 'www.' in b:
        b = b.replace('www.', '')
    if '.' in b:
        c = b.index('.')
        print(c)
        b = b[0:c]
    return b
  
 url = "http://github.com/carbonfive/raygun"
 print(domain_name(url))
