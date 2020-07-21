Input = raw_input("enter number : \n")
print(Input)
print("input type")
print(type(Input))
try:
        a = int(Input)
        print("number converrsion: \n")
        print(a)
        print("converted to type:")
        print(type(a))
except:
        print("sorry,not an int")

