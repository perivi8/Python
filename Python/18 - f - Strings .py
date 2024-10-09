# F-Strings

Letter = "My Name Is {} and I Am From {}"
name = "hari"
country = "India"
print(Letter.format(name,country))


#or
Letter = "My Name Is {} and I Am From {}"
name = "India"
country = "hari"
print(Letter.format(name,country))

#or
Letter = "My Name Is {1} and I Am From {0}"
name1 = "India"
country1 = "hari"
print(Letter.format(name1,country1))


#or
name2 = "hari"
country2 = "Africa"
print(f"My Name Is {name2} and I Am From {country2}")\

#add, sub, div, mul ....... by using f-strings

print(f"{3*30}")
