import numpy as np

array = np.random.randint(0, 10, (3,3))

print('1) Создана матрица\n', (array))

def maks(a):
   y = 0
   if max(a[0]) > max(a[1]) and max(a[0]) > max(a[2]):
      y = max(a[0])
   elif  max(a[1]) > max(a[0]) and max(a[1]) > max(a[2]):
      y = max(a[1])
   elif max(a[2]) > max(a[0]) and max(a[2]) > max(a[1]):
      y = max(a[2])      
              
   return y 
   
print('2) Максимальный элемент матрицы', maks(array))


def minimal(b):
   f = 0 
   if min(b[0]) < min(b[1]) and min(b[0]) < min(b[2]):
      f = min(b[0])
   elif  min(b[1]) < min(b[0]) and min(b[1]) < min(b[2]):
      f = min(b[1])
   elif min(b[2]) < min(b[0]) and min(b[2]) < min(b[1]):
      f = min(b[2])      
              
   return f
   
print('3)Минимальный элемент матрицы', minimal(array))


def suma_m(c):
   sum = 0
   for i in c:
      
      for j in i:
        sum += j   

   return sum


print('4) Сумма элементов матрицы', suma_m(array))

def maks_rd(d):
   summa_rada = 0
   index = 0
   
   for i in range(len(d)):
      if summa_rada < sum(d[0]):
         summa_rada = sum(d[0])
         index = 0
      elif summa_rada <  sum(d[1]):
         summa_rada = sum(d[1])
         index = 1
      elif summa_rada < sum(d[2]):
         summa_rada = sum(d[2])
         index = 2
   return index
      
print('5) Индекс ряда с максимальной суммой', maks_rd(array))

def max_kolon(x):
   summ = list(map(sum, zip(*x)))
   mx = max(summ)
   index = 0
   for i in range(len(summ)):
      if mx == summ[i]:
         index = i

   return index


print('6) Индекс максимальной колонки\n', max_kolon(array))



def min_rd(a):
   summ = list(map(sum, a))
   mn = min(summ)
   index = 0
   for i in range(len(summ)):
      if mn == summ[i]:
         index = i
   return index

print('7) Индекс ряда минимального\n', min_rd(array))


def min_kolon(y):

   summ = list(map(sum, zip(*y)))
   mx = min(summ)
   index = 0
   for i in range(len(summ)):
      if mx == summ[i]:
         index = i

   return index

print('8) Индекс минимальной колонки\n', min_kolon(array))


def v_obnull(v):
   n = len(v)
   mass = []
   for i in range(n):
      for j in range(n):
         if i != j and j != n:
            v[i][j] = 0
   return v

print('10) 11) Обнуление выше и ниже диагонали\n', v_obnull(array))


n = int(input('Сколько рядов матрицы\n'))
m = int(input('Сколько столбцов матрицы\n'))

matrix_a = np.random.randint(0, 10, (n, m))
print('11) Матрица a', matrix_a)
matrix_b = np.random.randint(0, 10, (n, m))
print('11) матрица b', matrix_b)


matrix_result = matrix_a + matrix_b
print('12) Сумма матриц\n', matrix_result)
matrix_result = matrix_a - matrix_b
print('13) Разность матриц\n', matrix_result)


g = int(input('Введите число которое необходимо умножить\n'))

matrix_umnoj = matrix_a*g
print('Матрица умноженная на число\n', matrix_umnoj)
