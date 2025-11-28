# x = int(input("Number: "))
# print(f"N: {x}")

x = 10
for i in range (1, x+1):
    if i == 1:
        print("* "*x)
        continue

    if i == x:
        print("* "*x)
        break

    print(f"* " + "  " * (x-2) + "*")


# Output: 
'''
* * * * * * * * * * 
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
* * * * * * * * * *
'''