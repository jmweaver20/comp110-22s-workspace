"""QZ00 If,then,else practice statements"""

choice: int = int(input("Enter a number: "))

if choice < 25:
    print("A")
if choice >= 25:
    if choice < 50:
        print("B")
if choice >= 50:
    if choice <= 75:
        print("D")
if choice > 75:
    print("C")
