name    = input("Please enter your name\n")
age     = int(input("Please enter your age\n"))
outPut  = f'Name {name}, age {age}'

print(outPut)
print(f'name {type(name)}\nageBefore {type(age)}')

age     = "26 years"
print(f'ageAfter {type(age)}')