# x = int(input("Number: "))

x = 10
for i in range (x, 0, -1):
    print(" "* (x-i) + "* "*i)

# Output:
'''
* * * * * * * * * * 
 * * * * * * * * * 
  * * * * * * * *
   * * * * * * *
    * * * * * *
     * * * * *
      * * * *
       * * *
        * *
         *
'''