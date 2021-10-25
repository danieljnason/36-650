# question 5 - pyramid
def pyramid(n):
    if (not isinstance(n, int)):
        return("Invalid Input")
    elif (n < 0):
        return("Invalid Input")
    else:
        i = n - 1
        while i >= 0:
            j = 0
            while j < i:
                print('', end=' ')
                j += 1
            k = i
            while k <= n - 1:
                print('*', end=' ')
                k += 1
            print('')
            i -= 1
pyramid(5)