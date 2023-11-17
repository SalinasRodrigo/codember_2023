def interprete (entrada):
  val = 0
  cod = [*entrada]
  for i in cod:
    if (i == '#'):
      val+=1
      continue
    if (i == '@'):
      val-=1
    if (i == '*'):
      val*=val
      continue
    if (i == '&'):
      print(val, end='')
      continue
  return

if __name__ == '__main__':
  entrada = input("Ingrese el codigo a interpretar: ")
  interprete(entrada)