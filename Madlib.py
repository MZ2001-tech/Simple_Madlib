
name = input("Name: ")
age = int(input("Enter your age: "))
place = input("Enter Place: ")
occupation = input("Enter Occupation: ")
work_place = input("Enter: Place : ")


madlib = f" My name is {name.capitalize()} and I am {age} \
           , years old! I live in {place.capitalize()}. I am a {occupation.capitalize()}\
            at {work_place.capitalize()}."

print(madlib)