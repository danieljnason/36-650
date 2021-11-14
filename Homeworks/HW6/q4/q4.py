# Question 4 - delete a set of keys from a dictionary
def delete_keys(rem_list, dictionary):
    if not isinstance(rem_list, list):
        raise TypeError("Incorrect type, please input a list as the first argument.")
    if not isinstance(dictionary, dict):
        raise TypeError("Incorrect type, please input a dictionary as the second argument.")
    for key in rem_list:
        if key in dictionary:
            dictionary.pop(key)
    return dictionary

test_dict = {'firstName' : "Daniel", 'lastName' : "Nason", 'birthYear' : "1999", 'nationality' : "American"}
  
rem = ['lastName', 'birthYear']

print("The original dictionary is : " + str(test_dict))

test = delete_keys(rem, test_dict)
print("The new dictionary is: " + str(test))