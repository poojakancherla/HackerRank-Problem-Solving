#

import collections

strings = ['aba','baba','aba','xzxb']
queries = ['aba','xzxb','ab']

lookup = collections.Counter(strings) # Creates a lookup of the count of elements in strings

for i in queries: # For each element in the queries
    if i in lookup: # Checks if it is present in lookup
        print(lookup[i])
    else:
        print(0)
