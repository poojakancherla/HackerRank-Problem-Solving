from collections import Counter

def numUniqueEmails(emails):
    modified = Counter()

    for email in emails:
        names = email.split('@')
        local, domain = names[0], names[1]
        local = local.split('+')[0]
        local = local.replace('.','')
        email = local+'@'+domain

        modified[email] += 1

    return len(modified)



print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
