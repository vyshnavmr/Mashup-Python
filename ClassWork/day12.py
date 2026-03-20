import re
try:
    Title = input("Enter book title: ")
    year = input("Publication yeaar ")

    a = r'[A-Za-z ]+$'
    b = r'[19|20\d{2}]$'

    if not re.fullmatch(a, Title):
        raise ValueError("ERROR: Book title error")
    if not re.fullmatch(b, year):
        raise ValueError("ERROR: Book title error")
    print("Accepted succcesssssfully")

except ValueError as e:
    print(e)
finally:
    print("Program execution successful")