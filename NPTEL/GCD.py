def gcd(m,n):
    i=min(m,n)
    while i>=0:
        if(m%i==0) and (n%i==0):
            return (i)
        else:
            i=i-1
m=int(input("Enter the m value"))
n=int(input("Enter the n value"))
print(gcd(m,n))
