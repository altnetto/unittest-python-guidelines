l = ['Bob', 'Marcus', 'Andrea']
t = ('Bob', 'Marcus', 'Andrea')
s = {'Bob', 'Marcus', 'Andrea'}

print("l[0]:",l[0])
print("t[1]:",t[1])
print("s:",s)

# um set não pode ser acessado por rótulos

# uma tuple não pode ter seus valores atualizados e nem adicionar novos valores

# um set pode ter adição de valores, usando set.add(elemento_a_adicionar)
# também se pode remover valores que já existem dentro do set

s.add('Carlos')
print(s)

s.remove('Carlos')
print(s)