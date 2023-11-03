def my_split (texto):
  aux = ''
  stack = []
  for letra in texto:
    if (letra == ' '):
      stack.append(aux.lower())
      aux = ''
    else:
      aux+=letra
  if aux != '': stack.append(aux.lower())
  return stack

def cuenta (palabras):
  lista = palabras.copy()
  stack = []
  count = {}
  num = 1
  while(len(lista)>0):
    if lista[0] in stack:
      del lista[0]
      continue
    else:
      aux = lista[0]
      stack.append(aux)
      del lista[0]
    for resto in lista:
      if ( resto == aux ):
        num+=1
    
    count[aux] = num
    num=1
  return count

if __name__ == '__main__':
  mensaje = input('ingresa tu mensaje encriptado: ')
  palabras = my_split(mensaje)
  cuenta_palabras = cuenta(palabras)
  print("resultado:")
  for palabra, num in cuenta_palabras.items():
    print(palabra, num, sep='', end='')

