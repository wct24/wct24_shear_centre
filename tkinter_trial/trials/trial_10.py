a= [0.1,0.2,0.3]

a = str(a)
a = a.replace(", ", "_")
a = a.replace("[", "")
a = a.replace("]", "")
print(str(a))
