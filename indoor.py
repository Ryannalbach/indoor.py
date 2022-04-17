# ask user for the class they are taking and correct for spacing and lower case
course = input("hello, what course are you taking? ").strip().title().lower()

# respond to user about the class
print(f"that's great, {course} is a fun class")