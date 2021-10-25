# problem 2
test = "Hello in 36-650, & other MSP courses."
def punc_remove(string):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in string:
        if i in punc:
            string = string.replace(i, '')
    return string

print(test)
print(punc_remove(test))
punc_remove(test)