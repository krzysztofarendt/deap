def flowchart():
    v = []
    n = int(input('Enter n: '))
    
    for i in range(n):
        x = float(input('Enter next number x: '))
        v.append(x)
    
    print(v)
    print('Negative numbers:')
    
    for i in range(len(v)):
        if v[i] < 0:
            print(v[i])

flowchart()