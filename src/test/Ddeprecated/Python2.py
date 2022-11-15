import re
import datetime

#findall
text= "ID: 867968 Esta es una de las mejores clases de testing en Udemy expresion 234556"

matching = re.findall('867968|mejores', text, re.IGNORECASE)

for result in matching:
    print(result)

#search
text = "ID: 867968 Esta es una de las mejores clases de testing en Udemy expresion 234556"

search = re.search('867968', text, re.IGNORECASE)
print(search)

if search:
    print('Se encontro el valor')
    text = re.sub('867968', '******', text, re.IGNORECASE)
    print(text)
else:
    print('No se encontro el valor')


#split
text = "ID: 867968 Esta es una de las mejores clases de testing en Udemy expresion 234556"

split = re.split('Udemy', text)
print(split)

#scenario

Scenario = {}

text= "Este texto contiene el valor del id:100"

PatronDeBusqueda = r"(?<=id:)\w+"
variables = re.findall(str(PatronDeBusqueda), text, re.IGNORECASE)
print(variables)
Scenario['btprnro'] = str(variables[0])
print('Se almaceno el btprnro= ' + Scenario['btprnro'])





