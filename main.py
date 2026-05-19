list=[]
n = 10000

p = 2
# make list with 2 - n
for i in range(2,n+1):
    list.append(i)
print(list)

# deleting the multiple of current checked number
while p <= n ** 0.5:
    for i in range(len(list)-1,-1,-1):
        if list[i] != p and list[i] % p == 0:
            del list[i]
    #set to next number to check
    for i in range(len(list)):
        if list[i] == p:
            p = list[i+1]
            break

print(list)
print(len(list))