

n=int(input('ENTER A NUMBER:'))
for i in range(2,n//2+1):
    if n%i==0:
        print('not a prime')
        break

else:
    print('prime number')
