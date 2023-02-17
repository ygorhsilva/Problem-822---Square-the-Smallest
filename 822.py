# Número de elementos da lista
n = 10**4
# Númenro de rounds
m = 10**16

# Criando a lista
numbers = list(range(2,n+1))

# Inicializando o contador como 0 e a variável smaller com o primeiro elemento da lista
i = 0
smaller = numbers[0]


while i < m :
  
    # smaller recebe o menor número do array e index a sua determinada posição
    smaller = min(numbers)
    index = numbers.index(smaller)
    
    # Elevando smaller ao quadrado e substituindo na mesma posição
    square = smaller**2
    numbers[index] = square
    i += 1

# Gerando o resultado em módulo 1234567891
result = sum(numbers)%1234567891
print(result)
