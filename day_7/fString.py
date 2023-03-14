# f-Strings is newly introduced in python after 3.6 onward

letter = "Hey, My name is {} and I am from {}"
country = "India"
name = "Aruna"
print(letter.format(name,country))
letter = "Hey, My name is {1} and I am from {0}"
print(letter.format(country, name))
print(f"Hey, My name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey, My name is {{name}} and I am from {{country}}")

txt = "For only {price: .2f} dollars!"
print(txt.format(price = 49.99993))

price = 35.654
txt = f"For only{price: .2f} dollars!"
print(txt)

print(f"{30*3}")
print(type(f"{30*3}"))