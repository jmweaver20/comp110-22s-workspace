"""An oracle that predicts the future."""

from random import randint

input("Ask a yes/no question: ")

response: int = randint(0, 3)

if response == 0:
    print("Most definitely")
elif response == 1:
    print("Highly Likely")
elif response == 2:
    print("Ask again later")
else:
    print("No way, not a chance")

# elif = else if; we can use this to simplify syntax - syntactical sugar
# means the same thing as nested else if statements but cleans up the code
# so that it looks more clean and clear. 