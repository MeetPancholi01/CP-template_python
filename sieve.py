import math
class Sieve:
    def all_prime_divisors(self,n):
        arr = [i for i in range(10**6+1)]
        i = 2
        while i*i <= n:
            j = i*i
            if arr[i] == i:
                for f in range(j,n+1,i):
                    if arr[f] == f:
                        arr[f] = i
            i += 1
        st = set()
        while n > 1:
            st.add(arr[n])
            n = n//arr[n]
        return st

    def all_primes(self,n):
        arr = [True for i in range(n+1)]
        i = 2
        while i*i <= n:
            j = i*i
            if arr[i] == True:
                for f in range(j,n+1,i):
                    if arr[f] == True:
                        arr[f] = False
            i += 1
        li = []
        for i in range(2,n+1):
            if arr[i]:
                li.append(i)

        return li

    def prime_divisors_in_range(self,l,r):
        lim = math.floor(math.sqrt(r))
        primes = self.all_primes(lim)
        dummy = [True]*(r-l+1)
        res = []
        for i in primes:
            firstMultiple = (l//i)*i
            if firstMultiple < l:
                firstMultiple += i
            for j in range(max(i*i,firstMultiple),r+1,i):
                dummy[j-l] = False
        for i in range(l,r+1):
            if dummy[i-l]:
                res.append(i)
        return res
