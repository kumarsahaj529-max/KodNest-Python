percentage = int(input("Enter percentage : "))
backlog = int(input("Enter active backlog : "))

if percentage >= 60 and backlog == 0:
    print("eligible")
else:
    print("not eligible")