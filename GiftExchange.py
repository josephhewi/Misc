import numpy as np
# everyone who should be included in the exchange
names = np.array([
    'Denise',
    'Keith',
    'Cory',
    'Sheila',
    'Joe',
    'Katharine',
    'Kylie'
])

# couples who are not allowed to directly exchange
notAllowed = np.array([
    ['Denise','Keith'],
    ['Cory','Sheila'],
    ['Joe','Katharine']
    ])





#print(names)

print('''

HOHOHOHOHOHOHOHOHOHOHOHOHOHOHOHOHO

Christmas Exchange Generator V1.0

      Created by Joe Hewitt

HOHOHOHOHOHOHOHOHOHOHOHOHOHOHOHOHO

''')

validArangement = False
# keep randomizing the array until there are no couples that are exchanging.
while not validArangement:

    np.random.shuffle(names)

    checks = [False,False,False]

    for i, couple in enumerate(notAllowed):
        # locate the memebers of each couple and make sure they are greater than 1 position apart.
        d = (np.where(names==couple[0])[0][0]-np.where(names==couple[1])[0][0])**2
        checks[i] = d!=1

    validArangement = set(checks) == {True}

    


# document and display the results
with open('./Exchange Pattern.txt','w+') as opf:
    for i in range(0,len(names)-1):
        exch = f'{names[i]} gives to {names[i+1]}'
        print(exch)
        opf.write(exch + '\n')
    exch = f'{names[-1]} gives to {names[0]}'
    opf.write(exch + '\n')
    print(exch)
    print()


