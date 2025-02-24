print ("enter your marks:")
m = int(input("maths:"))
s = int(input("science:"))
e = int(input("english:"))
h = int(input("hindi:"))
sum = m+s+e+h
print ("Sum of maths, english, science, and hindi:", sum)
perc = (sum/400)*100
print(end="Percentage Mark=")
print(perc)