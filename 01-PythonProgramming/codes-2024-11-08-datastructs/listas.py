# From other lists
a = [2,3,4]
b = [3,4,5]
c = a + b
print (c) # Concatenate the lists
print (2*c) # duplicate the list

# Check memory address
a.append(55)
print(f"{id(a[0])}, {id(a[1])}, {id(a[2])}, {id(a[3])}")