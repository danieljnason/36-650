# question 4
def triangles(n):
    if (not isinstance(n, int)):
        return("Invalid Input")
    elif (n < 0):
        return("Invalid Input")
    else:
        # creates values for nested while loop
        i, k = 1, 1
        while i <= n:
            j = 1 # start of new row, is reset to 1 every time
            while j <= i:
                print(k, end = " ") # uses end to get desired format
                j += 1 # increases length of row every time
                k += 1 # is incremented with every loop
            print() # ends the row once j is the same length as i
            i += 1 # updates the original loop variable so next row is longer than the last

triangles(3)
triangles(6)