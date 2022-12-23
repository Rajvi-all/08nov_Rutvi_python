mystr= input('write any sentence:')

yourstr=mystr.split()
yourstr.insert(3,"you")
usstr=' '.join(yourstr)

print(usstr)