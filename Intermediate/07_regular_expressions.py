
## Regular Expressions ##

import re

# match (busca únicamente desde el inicio de la cadena)

my_string = 'Esta es la lección número 7: Expressiones Regulares'
my_other_string = 'Esta no es la lección número 6: Manejo de ficheros'

match = re.match('Esta es la lección', my_string, re.I)

start, end = match.span()
print(start, end)

print(my_string[start: end])

print(re.match('Esta es la lección', my_other_string))

# seach (busca en toda la cadebna)

search = re.search('lección', my_string, re.I)

print(search)

# findall

findall = re.findall('lección', my_string, re.I)

print(findall)

# split

split = re.split(' ', my_string, re.I)

print(split)


# sub

sub = re.sub('lección', 'clase', my_string)

print(sub)


# patterns

pattern = r"[l|L]ección"

print(pattern)

print(re.findall(pattern, my_string))




