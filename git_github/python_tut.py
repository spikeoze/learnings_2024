from collections import defaultdict

data = defaultdict(list)

names = ['ali', 'mohamed', 'mukhtar', 'spike']

for name in names:
    data[name].append(1)
    data[name].append(2)
    data[name].append(3)
    data[name].append(4)
    
    
print(data)