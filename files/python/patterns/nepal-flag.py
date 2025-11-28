# Upper triangle
rows = int(8)
for j in range(1, rows+1):
    print("* " * j)

# Lowere Triangle
for i in range(0, rows):
    for j in range(0, i+1):
        print("*", end=' ')
    print("*\r")

# Output:
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
'''