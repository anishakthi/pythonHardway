#formatter = "%r %r %r %r"
formatter = "%s %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ('^','&','*','$')
print formatter % ("ani", "anitha", "anu", "anita")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I am anitha.",
    "I m learning python",
    "python's formatter is this exercise",
    "getting to know it"
)


newline = "FirstLine\nSecondLine"

print "%r" %(newline)
