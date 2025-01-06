maths = int(input("Enter Marks maths: "))
science = int(input("Enter Marks science: "))
soScience = int(input("Enter Marks soScience: "))

try:
    if maths < 0 or science < 0 or soScience < 0:
        raise ValueError("Marks Cannot be negative")

    if maths > 100 or science > 100 or soScience > 100:
        raise ValueError("Marks Cannot be Greater than 100")

    if maths < 70 or science < 70 or soScience < 70:
        raise PermissionError("You Cannot get the Certification")
except Exception as e:
    print("There is an Issue: ", e)

finally:
    print("Exception Handling Study.")

print(maths, science, soScience)
