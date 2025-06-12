# Replace the double space from problem 3 with single spaces.

str = "This is a  string  contain  double space"

# print(str.find("  "))
# print(str.count("  "))
print(str.replace("  ", " "))
print(str) # Strings are immutable which means that you cannot change them by running functions on them.