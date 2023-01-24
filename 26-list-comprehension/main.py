#list comprehensions

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

names_upper = [name.upper() for name in names if len(name) < 5]
print(names_upper)