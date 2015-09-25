__author__ = 'nightblues'


# Euclid's algorithm for searching greater common delimiter
def euclid(a,b):
    if b>a:
        a,b=b,a
    r=a%b
    while not r == 0:
        a,b=b,r
        r=a%b
    return b

# calculating a^n during O(logn) time
def binpow(a,n):
    if n==0:
        return 1
    if n==1:
        return a

    # note: int(n/2) should always floor n/2
    half_pow=binpow(a,int(n//2))
    double_half_pow=half_pow*half_pow
    if n%2==0:
        return double_half_pow
    else:
        return double_half_pow*a

def binpow_non_recursive(a,n):
    if n==0:
        return 1
    if n==1:
        return a
    powers_list = []
    i=n
    while i>0:
        if i%2==0:
            powers_list.append(True)
            i/=2
        else :
            powers_list.append(False)
            i-=1
    calculated_number=1
    for p in reversed(powers_list):
        if p:
            calculated_number*=calculated_number
        else:
            calculated_number*=a

    return calculated_number

# find all prime numbers 1..n
def eratosthenes(n):
    prime_numbers=[x+1 for x in range(n)]
    prime_numbers.pop(0) #1 is not a prime number
    i=0 # 0 index contains 2- the first prime number
    while i<len(prime_numbers):
        j=i+1
        while j<len(prime_numbers):
            if prime_numbers[j]%prime_numbers[i]==0:
                prime_numbers.pop(j)
            else:
                j+=1
        i+=1
    return prime_numbers


# find all prime numbers 1..n
def eratosthenes_m(n):
    prime_numbers=[True for x in range(n+1)]
    prime_numbers[0]=prime_numbers[1]=False
    i=2 # 0 index contains 2- the first prime number
    while i<=n:
        if prime_numbers[i]:
            j=i*i
            while j<=n:
                if j%i==0:
                    prime_numbers[j]=False
                j+=1
        i+=1
    result = []
    for x in range(len(prime_numbers)):
        if prime_numbers[x]:
            result.append(x)

    return result

