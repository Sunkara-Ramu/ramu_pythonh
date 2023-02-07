'''import csv
import numpy as np

data=[]
with open('data1.csv','r')as csvfile:
    file_reader = csv.reader(csvfile,delimeter=',')
    for row in file_reader:
        data.append(row)

npdata = np.array(data)
print(len(npdata), '\n', type(npdata))
print('Shape: ', npdata.shape)
print('Datatype: ', npdata.dtype.type)
np.save(open('data2.npy', 'wd'), npdata)

for elemenet in data:
    print(element)'''

'''import numpy as np

list1 = [
    [ int(x) for x in range(1, 20, 2) ],
    [ int(x) for x in range(20, 40, 2) ],
    [ int(x) for x in range(41, 60, 2) ],
    [ int(x) for x in range(60, 80, 2) ]
]

np_array = np.array(list1)

for array in np_array:
    print(array)

print('Length: ', len(np_array))
print('Type: ', type(np_array))
print('Shape: ', np_array.shape)
print('Datatype: ', np_array.dtype.type)
print('Size: ', np_array.size)'''

'''import csv
import numpy as np
data=[]
with open('data1.csv','r') as csvfile:
    file_reader=csv.reader(csvfile,delimiter=',')
    for row in file_reader:
        data.append(row)
data=np.array(data)
print(len(data),'\n',type(data))'''

