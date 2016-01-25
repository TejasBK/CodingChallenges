import re
filename = "test_regexemail.txt"
with open(filename) as f:
    for test in f:
        test = test.strip()
    #Generic match
    if (re.search(r"^[a-zA-z0-9.+]+@[a-zA-z0-9.]+\.[a-z]{2,}$",test)):
        print test, "true"
        continue
    #If there's a space in the text, return false
    if (re.search(r"\s", test)):
        print test, "false"
        continue
    #If the local name is enclosed by double quotes, return true
    if (re.search(r'(\")(.+?)\1@\w+\.[a-z]+', test)):
        print test ,"true"
        continue
    #If there are any ."content".
    if (re.search(r"(\.)(\")(.+?)\2\1", test)):
        print test, "true"
        continue
    print test, "false"


