cafe = str
pops = []
numbers = []
while cafe != 'MEOW':
    cafe = input()
    if cafe != 'MEOW':
        s_cafe = cafe.split()
        pop = s_cafe[0]
        pops.append(pop)
        num = int(s_cafe[1])
        numbers.append((num))
    else:
        print(pops[numbers.index(max(numbers))])