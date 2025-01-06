def calculateAge(birthYear: int, year: int):
    """This Function Calculates Age"""
    present_year = year
    age = present_year - birthYear
    return age


print(calculateAge(year=2027, birthYear=2006))
print("Hello","World",end='*',sep="\t")
