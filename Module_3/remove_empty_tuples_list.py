def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
 

tuples = [(), ('56','15','8'), (), ('raja', 'sita'),
          ('krishna', 'akbari', '105'), ('',''),()]
print(Remove(tuples))