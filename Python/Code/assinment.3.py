# python Basics Exercises 
# Assign a message to a variable and then print that message 
message = "Pakistan is a muslim country."
print(message)
#2-1 Assign a message to a variable and then print that message
message = "pakistan has five provinces."
print(message)
# 2-2 Change the value of the variable to a new message., and print the new message.
message= "pakistan is a country." 
print(message)
message= "Lahore City in Pakistan." 
print(message)
#3-1 use a variable t represent  a person's name 
Name = "Muhammad Zaib"
print(Name) 
#3-2 print a message to that person, such as, "Hello Eric, would you like to learn some python today? "
message= f"Hello {Name}, would you like to learn some python today."
print(message)
#4-1 use a variable to represent a person's name.print a message to that person,  
#4-2 print the person's  name in lowercase , uppercase and title case.
name= "mUammad  zaIb"
print(name. lower())
print(name.upper())
print(name. title())
#5 Faind a quote from a famous person yoi admire. print the qoute and the name of its author.
# The output should look something like the following: 
# Albert Einstein once said, "A person who never made a mistake never tried anything new."
author = "Albrt Einstein"
quote = "A person who never mad a mistake never tried anything new."
print(f'{author} once said,"{quote}"')
#6 Use a variable called famous_person to represent the famous person's name.
# Compose the message and represent it with a variable called message
famous_person = "Albert Einstein"
message = "once said, 'Life is like riding a bicycle. To keep your balance, you must keep moving.'"
print(f'{famous_person},said,"{message}"')
#7 Stripping Names - Use a variable to represent a person's name, and include some whitespace 
# characters at the beginning and end of the name. Make sure you use each character combination, 
# \t and \n, at least once. Print the name once, so the whitespace around the name is displayed. 
# Print the name using each of the three stripping functions: 1strip(), rstrip(), and strip().
name = "       Muhammad Zaib \n\t"
# Print the original name with whitespace
print("Original name with whitespace:")
print(f"'{name}'")
print(f"name after lstrip')():'{name.lstrip()}'")
print(f"name after rstrip')():'{name.rstrip()}'")
#8 Assign the values 5, 10, and 15 to three variables x, y, and z. Print their sum.
# Assign values to the variables
x = 5
y = 10
z = 15

# Calculate the sum of the variables
sum_of_variables = x + y + z

# Print the sum
print("The sum of {x}, {y}, and {z} is: {sum}")
# 9 Swap the values of two variables a and b. Print the values before and after the swap.
a = 5
b = 10
# Print values before the swap
print("Before swapping:")
print("a =", a)
print("b =", b)
a,b = b,a
#10 Create a variable with your favorite color and print it. Then change the variable name
# to something else and print the color again.
favorite_color = "blue"
# Step 2: Print the color
print(favorite_color)
# Step 3: Change the variable name to something else
color_choice = favorite_color
#11 Create a variable pet_name and set it to "Buddy". Change the value of pet_name
# to "Max" and print the new value.
# Step 1: Create a variable pet_name and set it to "Buddy"
pet_name = "Buddy"
pet_name = "Max"
print(pet_name)
print(color_choice)
#12 Assign the value "Sunshine" to a variable and print it.
# Then, mistakenly try to print a variable with a different name (like sunsine) 
# and observe the error.
# Assign the value "Sunshine" to a variable
weather = "Sunshine"
print("the weather is")
# 13 Assign the value 100 to a variable score and print it. Then assign a new value 
# to score and print it again.
score = 100
print("initial value of Score is :",score)
score = 200
print(score)
# 14 Create a string variable city and assign it the name of a city you like. Print the city name.
city= "makkah" 
print("city i like is",city )
# 15 Create a variable text with the value "python programming" and print it in title case.
text = "python programming"
print("in title case:",text.title())
# 16 Assign a string with mixed cases to a variable and print it in all lowercase letters.
mixed_cases = "zAib"
print("in lower case:", mixed_cases.lower())
# 17 Assign a string with mixed cases to a variable and print it in all uppercase letters.
mixed_case = "zAib"
print("in uper case:",mixed_cases.upper())
#18 Create a variable temperature with the value 25. Print "The current temperature is [temperature] 
# degrees." using the variable.
temperature = 25
print(f"The current temperature is {temperature} degrees.")
#19 Create a variable poem with a short poem that has multiple lines. 
# Print the poem with each line starting on a new line.
poem = """\
Roses are red,
Violets are blue,
Sugar is sweet,
And so are you."""
print(poem)