phone = input("Phone:")
numberWords={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four,"
}
output=""
for ch in phone:
    output += numberWords.get(ch,"!")+" "
print(output)