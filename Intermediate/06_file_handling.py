## File handling ##

# .txt file

txt_file = open(f"Intermediate/my_file.txt", mode= "r+") # leer y escribir

print(txt_file.read())
print(txt_file.read(10))

print(txt_file.readline())
print(txt_file.readline())

print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)

txt_file.write("Aunque también me gusta Kotlin")

