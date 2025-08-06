import json
import pandas as pd

list_header = [];list_values = []

with open('./file_to_extract.json', 'r') as file:
    data = json.load(file)

#gettin header of dimensions
for x in data['dimensionHeaders']:
    for y in x.values():
        list_header.append(y.split(":")[-1].strip())

#gettin header of metrics
for x in data['metricHeaders']: 
    for y in x.values():
        list_header.append(y.split(":")[-1].strip())

#index del csv
list_header.remove('TYPE_INTEGER') # hard coded, no es lo mejor
print(list_header)

#gettin header of metrics
for x in data['rows']:
    for y in x.values():
        for i in y:
            for j in i.values():
                list_values.append(j)


length_list = len(list_header)
final_list = [list_values[i:i + length_list] for i in range(0, len(list_values), length_list)] # crear listas dentro de una lista, con un rango (matriz)
print(len(final_list)) # check number of rows

#create df, adding each value
df = pd.DataFrame(final_list, columns=list_header)
print(df.head())
df.to_csv('json_output.csv', index=False, sep=';')
