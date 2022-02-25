n=int(input('n = '))
print("\n")
mul=1
for i in range(1,n+1):
    mul*=i
    print(mul)

print('The factorial of ',n,'is =',mul)
