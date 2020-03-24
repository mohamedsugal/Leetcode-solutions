def subdomainVisits(cpdomains):
    counter = {}
    for i in cpdomains: 
        visits, domains = i.split(' ')
        visits, domains= int(visits), domains.split('.')

        for j in range(len(domains)): 
            sub_domains = '.'.join(domains[j:])
            if sub_domains in counter: 
                counter[sub_domains] += visits
            else: 
                counter[sub_domains] = visits
       
    return [str(counter[i]) + ' ' + i for i in counter]
    


cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(subdomainVisits(cpdomains))
