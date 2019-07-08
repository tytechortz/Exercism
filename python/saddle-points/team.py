t = "team"
x = t.translate({ord(i): None for i in "ta"})
x = x[::-1]
print(x)