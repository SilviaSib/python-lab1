print("Insert the string ")

string = input()
if len(string) < 2:
    print("empty string")
else:
    print(string[0] + string[1]+string[len(string)-2]+string[len(string)-1])

quit()