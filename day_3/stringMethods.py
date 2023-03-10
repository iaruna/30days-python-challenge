Name = "Aruna Kumari"
print(Name.upper()) # converts a string to upper case
print(Name.lower()) # converts a string to lower case

Name1 = "--Aruna-kumari--"
# removes any white spaces before & after string.
print(Name1.strip())

print(Name1.strip("-")) # removes any trailing characters

print(Name1.replace("Ar", "At")) # replace

''' splits the given string at the specified instance and returns the separated strings as list items.'''
print(Name1.split("-"))

'''first character of the string to uppercase and the rest other characters of the string are turned to lowercase.'''
print(Name.capitalize())

'''aligns the string to the center as per the parameters given by the user.'''
print(Name.center(50))
print(Name.center(25, "."))

'''Count() method returns the number of times the given value has occurred within the given string.'''
print(Name.count("a"))

'''checks if the string ends with a given value. If yes then return True, else return False.'''
print(Name.endswith("i"))

'''searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.'''
print(Name.find("a"))

'''searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.'''
print(Name.index("K"))

'''returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.'''
print(Name.isalnum())

'''returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.'''
print(Name.isalpha())

print(Name.islower()) # true if all characters in lowercase

print(Name.isprintable()) # true if printable

# True only and only if the string contains white spaces,
print(Name1.isspace())

# true if the first letter of each word of the string is capital
print(Name.istitle())

print(Name.isupper()) # true if all characters in uppercase

print(Name.startswith("Ar")) #if yes print true

print(Name.swapcase()) #Upper case are converted to lower case

#capitalize each letter of word within the string.
print(Name.title())

name = "Aruna"
print(list(name))