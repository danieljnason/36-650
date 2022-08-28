# # problem 3
# def not_same(a,b): # function for unequal lengths
#             long, short = (a,b) if len(a) > len(b) else (b,a)
#             for i in range(len(long)):
#                 tmp = long[:i] + long[i+1:]
#                 if tmp == short:
#                     return True
#             return False
# def same(a,b): # function for equal lengths
#             count = 0
#             for i in range(len(a)):
#                 if a[i] != b[i]:
#                     count += 1
#             return count <= 1
# def one_away(a,b):
#     if abs(len(a) - len(b)) > 1: # overall constraint - only one letter separates strings
#         print("Invalid input")
#     elif len(a) != len(b): # case 1 - unequal lengths
#         return not_same(a,b)
#     else: # case 2 - equal lengths
#         return same(a,b)

## updated version of the function
def one_away(a,b):
            if abs(len(a) - len(b)) > 1:
                        return "Invalid input, strings should have a difference of length less than or equal to one"
            elif len(a) != len(b): # case 1 - unequal lengths
                        # assign variables based on string lengths
                        s,l = tuple(sorted([a,b], key = len))
                        ## loops through longer string and remove index each time
                        ## check if the removed value results in equality of the two strings
                        return any([True if l[:i] + l[i+1:] == s else False for i in range(len(l))])
            else: # case 2 - equal lengths
                        # loop through strings and count if the characters are same at each index
                        # check if number of matches is less than or equal to 1
                        return len([i for i in range(len(a)) if a[i] != b[i]]) <= 1

print(one_away("pale", "ple"))
print(one_away("pale", "pales"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
