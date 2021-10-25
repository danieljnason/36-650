# problem 3
def not_same(a,b): # function for unequal lengths
            long, short = (a,b) if len(a) > len(b) else (b,a)
            for i in range(len(long)):
                tmp = long[:i] + long[i+1:]
                if tmp == short:
                    return True
            return False
def same(a,b): # function for equal lengths
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count <= 1
def one_away(a,b):
    if abs(len(a) - len(b)) > 1: # overall constraint - only one letter separates strings
        print("Invalid input")
    elif len(a) != len(b): # case 1 - unequal lengths
        return not_same(a,b)
    else: # case 2 - equal lengths
        return same(a,b)

print(one_away("pale", "ple"))
print(one_away("pale", "pales"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))