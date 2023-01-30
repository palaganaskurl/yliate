import tldextract

"""
As per stackoverflow
No, there is no "intrinsic" way of knowing that (e.g.) zap.co.it is a subdomain (because Italy's registrar DOES sell domains such as co.it) while zap.co.uk isn't (because the UK's registrar DOESN'T sell domains such as co.uk, but only like zap.co.uk).

You'll just have to use an auxiliary table (or online source) to tell you which TLD's behave peculiarly like UK's and Australia's -- there's no way of divining that from just staring at the string without such extra semantic knowledge (of course it can change eventually, but if you can find a good online source that source will also change accordingly, one hopes!-).
"""
def get_top_level_domain(url):
    return tldextract.extract(url)

print(get_top_level_domain('http://www.google.de/something').suffix)
print(get_top_level_domain('http://www.amazon.co.uk/something').suffix)
