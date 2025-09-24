

n=int(input('ENTER A NUMBER:'))
c=0
for i in range(1,n):
    if n%i==0:
        c=c+1

if c==1:
    print('prime number')
else:
    print('NOT A PRIME')
