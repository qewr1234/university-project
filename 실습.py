#abs(), divmode(), pow(), round()
'''
x = -123
print("x      = {:4d}".format(x))
print("abs(x) = {:4d}".format(abs(x)))

a, b = 7, 2
q, r = divmod(a, b)
print("q, r = divmode(a, b)")
print("q = ", q)
print("r = ", r)

a_b = pow(a, b)
print("pow ({}, {}) = {}".format(a, b, a_b))

c = 3.1515926535
c_r = round(c, 4)
print("c_r = ", c_r)
'''

# complex
'''
c1 = complex(3, 4)
print("c1 = ", c1)
print("type(c1) = ", type(c1))
print("c1.real = ", c1.real)
print("c1.imag = ",c1.imag)

cj = complex.conjugate(c1)
print("conjugate(c1) = ", cj)
print("cj.real = ", cj.real)
print("cj.imag = ", cj.imag)

c2 = complex(5, 6)
print("c2 = ", c2)
print("c1 + c2 = ", c1 + c2)
print("c1 - c2 = ", c1 - c2)
print("c1 * c2 = ", c1 * c2)
print("c1 / c2 = ", c1 / c2)
'''
# input complex
'''
complex_str_1, complex_str_2 = map(complex,input("input complex number (a+bj): ").split())
c1 = complex(complex_str_1)
c2 = complex(complex_str_2)
print("c1 = ", c1)
print("c2 = ", c2)

print("c1 + c2 = ", c1 + c2)
'''
# for-loop Selection Sorting
'''
L = [5, 3, 8, 1, 2, 7]
size = len(L)
print("L(initial) = ", L)

for i in range(size - 1):
    min_idx = i
    for j in range(i + 1, size):
        if L[min_idx] > L[j]:
            min_idx = j
    if(min_idx != i):
        L[min_idx], L[i] = L[i], L[min_idx]

    print("round{:2} - L : {}".format(i, L))
'''

'''
import copy

t1 = (1, 2, 3)
print("t1: ", t1)

print("t2 = t1")
t2 = t1
print("t2 == t1: ", t2 == t1)
print("id(t1) : ", id(t1))
print("id(t2) : ", id(t2))
print("t2 is t1 : ", t2 is t1)

print("\nt3 = copy.copy(t1)")
#t3 = t1.copy()
t3 = copy.copy(t1)
print("t3 : ", t3)
print("t3 == t1: ", t3 == t1)
print("id(t1) : ", id(t1))
print("id(t2) : ", id(t3))
print("t3 is t1 : ", t3 is t1)

print("\nt4 = copy.deepcopy(t1)") 
t4 = copy.deepcopy(t1)
print("t4 : ", t4)
print("t4 == t1: ", t4 == t1)
print("id(t1) : ", id(t1))
print("id(t4) : ", id(t4))
print("t4 is t1 : ", t4 is t1) 

a = (1, 2, 3, [10, 20, 30])
print("a = ", a)
a[3][0] = 100
print("after a[3][0] = 100, a = ", a)
del a[3][2]
print("after del a[3][2], a = ", a)

t1 = ('a', 'b', 'c')
t2 = ('x', 'y', 'z')
print("t1 = {}".format(t1))
print("t2 = {}".format(t2))

t3 = t1 + t2
print("t3 = t1 + t2 {}".format(t3))

t4 = t1 * 3
print("t4 = t1 * 3 = {}".format(t4))
'''
'''
t1 = ('a', 'b', 'c')
t2 = ('d', 'e', 'f')
print("t1 = t2 : ", t1 == t2)

print('\nt3 = t1')
t3 = t1
print("t3 is t1 : ", t3 is t1)

t4 = t1 + t2
print("min(t4) = {}, max(t4) = {}".format(min(t4), max(t4)))

t5 = (1, 2, 3, 4, 5)
print("sum(t5) = {}".format(sum(t5)))
'''
'''
t1 = ('x', 'y', 'z', 'w', 'a', 'b' ,'c')
print("t1 : {}".format(t1))
t2 = sorted(t1)
print("t2 = {}".format(t2))

t3 = (3, 5, 1, 0, 6, 9, 2, 8, 7, 4)
print("t3 = {}".format(t3))
t4 = sorted(t3)
print("t4 = {}".format(t4))
'''
'''
dates = [(2000, 12,25), (2019, 9, 1), (2019, 3, 1), (1, 1, 1)]

print("dates = ", dates)
sorted_dates = sorted(dates)

print("sorted_dates = ", sorted_dates)
'''

# find_min_max
'''
def find_min_max(L):
    nMin = nMax = L[0]
    for i in L:
        if nMin > i:
            nMin = i
        if nMax < i:
            nMax = i
    return nMin, nMax

print("min max = find_min_max([3, 1, 0, 5, 6, 9, 4, 2])")
min, max = find_min_max([3, 1, 0, 5, 6, 9, 4, 2])

print("min: ", min)
print("max: ", max)

print("min, max = find_min_max([3, 1, 0, 5, 6, 9, 4, 2, -1, 10])")
min, max = find_min_max([3, 1, 0, 5, 6, 9, 4, 2, -1, 10])

print("min: ", min)
print("max: ", max)
'''

# default value
'''
def volume(width = 1, length = 1, height = 1):
    print("passed argument: width = {:3}, length = {:3}, height = {:3}".format(width, length, height))
    return width * length * height

print("volume() = ", volume())
print("volume() = ", volume(10))
print("volume() = ", volume(10, 20))
print("volume() = ", volume(10, 20, 30))
'''
# map() function
'''
x = [1, 2, 3, 4, 5]
Sq_x = list(map(lambda x : x ** 2, x))
print("x    :", x)
print("Sq_x :", Sq_x)

y = [1, 2, 3, 4, 5]
print("Y  : ", y)
Pow_x_y = list(map(pow, x, y))
print("x ^ y : ", Pow_x_y)
'''

# zip(), *zip()
'''
x = [1, 2, 3]
y = ['a', 'b', 'c']
z = [100, 200, 300]

print("x: ", x)
print("y: ", y)
print("z: ", z)

Zip_xy = list(zip(x, y))
print("Zip_xy : ", Zip_xy)

A, B = zip(*Zip_xy)
print("A : ", A)
print("B : ", B)

D = list(zip(x, y, z))
print("D : ", D)

d1, d2, d3 = zip(*D)
print("d1 = ", d1)
print("d2 = ", d2)
print("d3 = ", d3)
'''

# lambda function
'''
from tokenize import Triple


double = lambda x : x * 2
triple = lambda x : x + x + x

print("double: ", double)
print("double(5): ", double(5))
print("double('ABC'): ", double('ABC'))

print("triple: ", triple)
print("triple(5): ", triple(5))
print("triple('ABC'): ", triple('ABC'))
'''

# first class function
'''
def Greeting(name):
    return "Hello, " + name

sayHello = Greeting
print("sayHello('Kim') ==> ", sayHello('Kim'))
print("dir(sayHello) : ", dir(sayHello))
'''

# measureTime()
'''
import time

def measureTime(f):
    def wrapper(n):
        t_before = time.time()
        ret = f(n)
        t_after = time.time()
        elapsed_time = t_after - t_before
        return ret, elapsed_time
    return wrapper

def rFibo(n):
    if n <= 1:
        return n
    return rFibo(n - 1) + rFibo(n - 2)

measureTime_rFibo = measureTime(rFibo)
for n in range(1, 35, 1):
    fibo_n, t_elapsed = measureTime_rFibo(n)
    print("Fibo({:3d}) = {:8d}, took {:10.3f}milli-seconds".format(n, fibo_n, t_elapsed * 1000))
'''

# Generator Function
'''
def myRange(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in myRange(5):
    print("return value from myRange(n) : {:2d}".format(i))
'''

# merge sort
'''
def _merge(L_left, L_right):
    L_res = []
    i, j = 0, 0
    len_left, len_right = len(L_left), len(L_right)
    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]:
            L_res.append(L_left[i])
            i += 1
        else:
            L_res.append(L_right[j])
            j += 1
    while(i < len_left):
        L_res.append(L_left[i])
        i += 1
    while(j < len_right):
        L_res.append(L_right[j])
        j += 1
    return L_res

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        L_left = mergeSort(L[:middle])
        L_right = mergeSort(L[middle:])
        return _merge(L_left, L_right)

L = [3, 2, 1, 0, 9, 4, 7, 5, 8, 6, 10, 13, 15, 14, 12, 11]
print("L = ", L)
sorted_L = mergeSort(L)
print("sorted_L = ", sorted_L)
'''

# Quick Sort
'''
def _partition(arr, left, right, pi):
    pv = arr[pi]
    arr[pi], arr[right] = arr[right], arr[pi]
    npi = i = left
    while (i <= right - 1):
        if (arr[i] <= pv):
            arr[npi], arr[i] = arr[i], arr[npi]
            npi += 1
        i += 1
    arr[npi], arr[right] = arr[right], arr[npi]
    return npi

def _quickSortLoop(arr, left, right):
    if(left >= right):
        return
    pi = (left + right) // 2
    new_pi = _partition(arr, left, right, pi)
    if (left < new_pi - 1):
        _quickSortLoop(arr, left, new_pi - 1)
    if(new_pi + 1 < right):
        _quickSortLoop(arr, new_pi + 1, right)

def quickSort(arr):
    left, right = 0, len(arr) - 1
    _quickSortLoop(arr, left, right)

L = [3, 2, 1, 0, 9, 4, 7, 5, 8, 6, 10, 13, 15, 14, 12, 11]
print("L = ", L)
quickSort(L)
print("sorted L = ", L)
'''

# class Person
'''
class Person():
    def __init__(self, name = None, age = None): # 초기화 함수
        self.name = name
        self.age = age
        print("Person:: _init_() is executed with \n name = {}, age = {}".format(name, age))
    def __new__(cls, *args, **kwargs): # 새롭게 생성하는 생성자 기능
        print("__new__(constructor) with \n cls = {}, args = {}, kwargs = {}".format(cls, args, kwargs))
        cls.__inst = super(Person, cls).__new__(cls)
        return cls.__inst
    def __str__(self): # print()를 사용하여 객체를 출력할 때 사용되는 문자열 제공
        return "Person (name = {}, age = {})".format(self.name, self.age)
    def __del__(self): # 클래스 소멸자
        print("Person:: __del__() is executed")
    def __dict__(self): # 속성 이름과 현재 설정된 값을 매핑시키는 딕셔너리를 반환
        print("Person:: __dict__() is executed")
        return self.name, self.age 

p = Person("Kim", 25)
print("p = ", p)
print("type(p) = {}".format(type(p)))
print("p.__doc__ = ", p.__doc__)
p.name = "Lee"
p.age = 20
print("after updates of p's name and age = {}".format(p))

name, age = p.__dict__()
print("name = {}, age = {}".foramt(name, age))
print("deleting instance p...")
del p
print("after del p, p = ", p)
'''

# class with instance, class method, static method
'''
class A():
    data = 0
    @classmethod

    def cls_incr(cls, value):
        A.data += value
        return 'cl_incr invoked', cls

    def inst_incr(self, value):
        self.data += value

    def __repr__(self):
        return "instance od class A(current self.data = {}".format(self.data)

print("A.__dict__ = ", A.__dict__)
print("A.data = ", A.data)
A.cls_incr(50)
print("after A.cls_incr(50), A.data = ", A.data)

a = A()
print("a.__dict__ = ", a.__dict__)
print("a = ", a)
a.data = 0
print("after a.data = 0, a.__dict__ = ", a.__dict__)
a.inst_incr(100)
print("after a.inst_incr(100), a.data = ", a.data)
print("after a.inst_incr(100), A.data = ", A.data)
'''

# Dynamic inclusion of class method
'''
def incr(cls, value = 1):
    print("cls = %s" %cls)
    cls.data += value
    return cls.data

class A(object):
    "class A"
    data = 0

setattr(A, 'incr', classmethod(incr))

print("A.incr() : ", A.incr())
a = A()
print("a.data : ", a.data)
b = A()
print("b.data : ", b.data)
a.incr(10)
print("after a.incr(10) ==> a.data : ", a.data)
print("after a.incr(10) ==> b.data : ", b.data)
print("a.__dict__ : ", a.__dict__)
print("b.__dict__ : ", b.__dict__)
print("A.__dict__ : ", A.__dict__)

a.inst_x = 20
a.inst_y = 30

print("a.__dict__ : ", a.__dict__)
print("b.__dict__ : ", b.__dict__)
print("A.__dict__ : ", A.__dict__)
'''

# class A with staticmethod incr()
'''
class A:
    data = 0
    @staticmethod
    def incr(value = 1):
        A.data += value
        return A.data

print("A : ", A)
print("A.data : ", A.data)
print("A.incr() : ", A.incr())
print("A.incr(10) : ", A.incr(10))

a = A()
b = A()

print("a : ", a)
print("a.data : ", a.data)
print("a.incr(50) : ", a.incr(50))
print("a.data : ", a.data)
'''

# class A with staticmethod incr()
'''
def incr(value = 1):
    A.data += value
    return A.data

class A:
    data = 0

setattr(A, 'incr', staticmethod(incr))
print("A : ", A)
print("A.incr() : ", A.incr())
print("A.data : ", A.data)
print("A.incr(10) : ", A.incr(10))

a = A()
b = A()
print("a : ", a)
print("a.data : ", a.data)
print("a.incr(50) : ", a.incr(50))
print("a.data : ", a.data)
print("b : ", b)
print("b.data : ", b.data)
print("b.incr(50) : ", b.incr(50))
print("a.data : ", a.data)
'''

# class cmplx with operator overloading
'''
class cmplx:
    def __init__(self, real = 0.0, imagin = 0.0):
        self.real = real
        self.imagin = imagin

    def __add__(self, other):
        r = self.real + other.real
        i = self.imagin + other.imagin
        return cmplx(r, i)

    def __sub__ (self, other):
        r = self.real - other.real
        i = self.imagin - other.imagin
        return cmplx(r, i)

    def __mul__(self, other):
        r = self.real * other.real - self.imagin * other.imagin
        i = self.real * other.real + self.imagin * other.imagin
        return cmplx(r, i)

    def __str__(self):
        s = "cmplx({:>8.4}, {:>8.4})".format(self.real, self.imagin)
        return s

c1 = cmplx(1.51, 2.22)
c2 = cmplx(3.83, 4.74)
c3 = c1 - c2
c4 = c1 + c2
c5 = c1 * c2

print("c1 : ", c1)
print("c2 : ", c2)
print("c3 : ", c3)
print("c4 : ", c4)
print("c5 : ", c5)
'''

# Example of class inheritance in Python
'''
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        s = "person(name = {}, age = {})".format(self.name, self.age)
        return s

class student(person):
    def __init__(self, name, age, school, st_id, major):
        person.__init__(self, name, age)
        self.school = school
        self.st_id = st_id
        self.major = major
    
    def __str__(self):
        s = "student({}, {}, {}, {}, {})".format(self.name, self.age, self.school, self.st_id, self.major)
        return s

class employee(person):
    def __init__(self, name, age, company, salary):
        person.__init__(self, name, age)
        self.company = company
        self.salary = salary

    def __str__(self):
        s = "employee({}, {}, {}, {})".format(self.name, self.age, self.company, self.salary)
        return s

p1 = person("Kim", 20)
print(p1)

p2 = student("park", 22, "yeungnam Univ", 12345, "Info & comm Eng")
print(p2)

p3 = employee("Hong", 25, "Samsung", 5000)
print(p3)
'''

# Python classes with inheritance
'''
class shape:
    def __init__(self, stype, x, y, color):
        self.stype = stype
        self.x = x
        self.y = y
        self.color = color

class circle(shape):
    def __init__(self, x, y, radius, color = "black"):
        shape.__init__(self, "circle", x, y, color)
        self.radius = radius
    
    def __str__(self):
        return "a {} circle: [center = ({}, {}), radius = {}]".format(self.color, self.x ,self.y, self.radius)

class Rectangle(shape):
    def __init__(self, x, y, width, length, color = "black"):
        shape.__init__(self, "Rectangle", x, y, color)
        self.width = width
        self.length = length
    
    def __str__(self):
        return "a {} rectangle: [center = ({}, {}), width = {}, length = {}]".format(self.color, self.x, self.y, self.width, self.length)

s1 = circle(0, 0, 100)
print(s1)

s2 = Rectangle(3, 4, 10, 20, 'red')
print(s2)
'''

# class date
'''
from calendar import month_name

class date:
    def __init__(self, yr, mt, dy):
        self.setYear(yr)
        self.setMonth(mt)
        self.setDay(dy)
    def setYear(self, yr):
        self.year = yr
    def setMonth(self, mt):
        if 1 <= mt <= 12:
            self.month = mt
        else:
            print("Error")
            self.month = 1
    def isLeapYear(self, yr):
        if ((yr % 4 == 0) and(yr % 100 != 0)) or (yr % 400 == 0):
            return True
        else:
            return False
    def setDay(self, dy):
        daysofMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear(self.year):
            daysofMonth[2] = 29
        if 1 <= dy <= daysofMonth[self.month]:
            self.day = dy
        else:
            print("Error")
            self.day = 1
    def getYear(self):
        return self.year
    def getMonth(self):
        return self.month
    def getDay(self):
        return self.day
    def __lt__(self, other):
        if self.__eq__(other):
            return False
        elif (self.year, self.month, self.day) < (other.year, other.month, other. day):
            return True
        else:
            return False
    def __str__(self):
        return "({:2d} : {:2d} : {:2d})".format(self.getYear(), self.getMonth(), self.getDay())

d1 = date(2022, 1, 20)
print("d1 = ", d1)
'''

# class Matx and Application Program
'''
class Mtrx:
    def __init__(self, name, n_row, n_col, L_data):
        self.name = name
        self.n_row = n_row
        self.n_col = n_col
        self.rows = []
        index = 0
        for i in range(0, self.n_row):
            L_row = []
            for j in range(0, self.n_col):
                L_row.append(L_data[index])
                index = index + 1
            self.rows.append(L_row)
        
    def setName(self, name):
        self.name = name
    
    def __str__(self):
        s = "{} = \n".format(self.name)
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                s += "{:3d}".format(self.rows[i][j], end = " ")
            s += "\n"
        return s

    def __add__(self, other):
        L_res = []
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                r_ij = self.rows[i][j] + other.rows[i][j]
                L_res.append(r_ij)
        return Mtrx("R", self.n_row, self.n_col, L_res)

    def __sub__(self, other):
        L_res = []
        for i in range(0, self.n_row):
            for j in range(0, self.n_col):
                r_ij = self.rows[i][j] - other.rows[i][j]
                L_res.append(r_ij)
        return Mtrx("R", self.n_row, self.n_col, L_res)

    def __mul__ (self, other):
        L_res = []
        n_row, n_col = self.n_row, other.n_col
        n_k = other.n_row
        for i in range(0, n_row):
            for j in range(0, n_col):
                r_ij = 0
                for k in range(0, n_k):
                    r_ij = r_ij + self.rows[i][k] * other.rows[k][j]
                L_res.append(r_ij)
        return Mtrx("R", self.n_row, other.n_col, L_res)

def main():
    data_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    data_2 = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0 ,0]
    data_3 = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]

    m1 = Mtrx("M1", 4, 5, data_1)
    print(m1)

    m2 = Mtrx("M2", 4, 5, data_2)
    print(m2)

    m3 = Mtrx("M3", 5, 4, data_3)

    m4 = m1 + m2
    m4.setName("M4 = M1 + M2")
    print(m4)

    m5 = m1 - m2
    m5.setName("M5 = M1 - M2")
    print(m5)

    m6 = m1 * m3
    m6.setName("M6 = M1 * M3")
    print(m6)

if __name__ == "__main__":
    main()
'''

# Text file open(), write(), read(), close()
'''
f1 = open("data.txt", 'w')
f1.write("Lee 80 90 95 \n")
f1.write("Kim 85 75 70 \n")
f1.write("Park 70 85 95 \n")
f1.write("Hong 90 85 95 \n")
f1.write("Yoon 85 85 95 \n")
f1.close()

f2 = open("data.txt", 'r')
while True:
    read_data = f2.read()
    if read_data == '':
        break
    print(read_data)

f2.close()
'''

# studet sata processing with text file input/output
'''
student_records = [('Lee', 80, 90, 95), ('Kim', 85, 75, 70), ('Park', 70, 80, 90), ('Hong', 90, 85, 95), ('Yoon', 85, 85, 95)]

def fread_data(file_name):
    data_list = []
    f = open(file_name, 'r')
    for line in f:
        name, kor, eng, math = line.split()
        tmp = [name, int(kor), int(eng), int(math)]
        data_list.append(tmp)
    f.close()
    return data_list

def fwrite_data(file_name, data_list):
    f = open(file_name, 'w')
    f.write("  name,  kor,  eng,  math,  sum,  avg\n")
    f.write("-------------------------------------\n")
    for data in data_list:
        s = "{:<5},".format(data[0])
        s += "{0:>5},".format(data[1])
        s += "{0:>5},".format(data[2])
        s += "{0:>5},".format(data[3])
        s += "{0:6d},".format(data[4])
        s += "{0:>6.2f},".format(data[5])
        s += '\n'
        f.write(s)
    f.close()

def calculate_score(data_list):
    i = 0
    for name, kor, eng, math in data_list:
        sumScore = kor + eng + math
        data_list[i].append(sumScore)
        data_list[i].append(sumScore / 3.0)
        i = i + 1

f_st_name = "student_records.txt"
f_st = open(f_st_name, 'w')
st_count = 0
for st in student_records:
    print("student_records[{:}] = {}".format(st_count, st))
    st_str = "{} {} {} {}\n".format(st[0], st[1], st[2], st[3])
    f_st.write(st_str)
    st_count += 1
f_st.close()

students = fread_data(f_st_name)
print("\nStudent records read from {} : ".format(f_st_name))
for st in students:
    print(st)
calculate_score(students)

print("\nAfter calculate_student_score(students)")
for st in students:
    s = ""
    s = "{0:<5s},".format(st[0])
    s += "{0:>3},".format(st[1])
    s += "{0:>3},".format(st[2])
    s += "{0:>3},".format(st[3])
    s += "{0:4d},".format(st[4])
    s += "{0:6.2f},".format(st[5])
    print(s)
fwrite_data("result_student.txt", students)

print("\nContest of {}: ".format("result_student.txt"))
f_st = open("result_student.txt", "r")
while True:
    line = f_st.readline()
    if line == '':
        break
    print(line, end = ' ')
f_st.close()
'''

# pandas - df, calculation of average of each class
'''
import pandas as pd

st_ids = [1201, 2202, 1203, 1701, 1500]
st_data = {'st_name': ['Kim', 'Lee', 'Park', 'Yoon', 'Choi'], 
'Eng': [95.7, 92.4, 85.7, 76.8, 98.9], 
'Kor': [92.3, 94.5, 88.7, 80.2, 97.2],
'Math': [95.2, 93.5, 90.3, 83.5, 98.3],
'Sci': [75.9, 92.4, 87.3, 75.4, 95.3]
}

df = pd.DataFrame(st_data, index = st_ids)
print("df = \n", df)

avgs_per_student = df.mean(1)
print("\navgs_per_student = ")
print(avgs_per_student)

df.loc[:,'Avg'] = avgs_per_student
print("\ndf_with_avg = ")
print(df)

avgs_per_class = df.mean()
print("\navgs_per_class = ")
print(avgs_per_class)

df.loc[len(df)] = avgs_per_class
df.at[len(df) - 1, 'st_name'] = "Total_Avg"
print("\ndf_with_avg = ")
print(df)
'''

# pandas - pivoting with pivot()
'''
import pandas as pd

print("Reading df_sensorXYZ from excel file")
df_sensorXYZ = pd.read_excel("Sensor_Reading_XYZ.xlsx")

print("\nSensor_Reading_XYZ (in record format) = ")
print(df_sensorXYZ)

df_sensorXYZ_pivot = df_sensorXYZ.pivot(index = 'Time', columns = 'variable', value = 'value')
print("\nSensor_Reading_XYZ after pivoting = ")
print(df_sensorXYZ_pivot)
'''

# pandas = visualization with plot()
'''
import pandas as pd
import matplotlib.pyplot as plt

st_ids = [1201, 2202, 1203, 1701, 1500]
st_data = {'st_name': ['Kim', 'Lee', 'Park', 'Yoon', 'Choi'], 
'Eng': [95.7, 92.4, 85.7, 76.8, 98.9], 
'Kor': [92.3, 94.5, 88.7, 80.2, 97.2],
'Math': [95.2, 93.5, 90.3, 83.5, 98.3],
'Sci': [75.9, 92.4, 87.3, 75.4, 95.3]
}

df = pd.DataFrame(st_data, index = st_ids)
print("df = \n", df)

df.plot(kind = 'bar', x = 'st_name', y = ['Eng', 'Kor', 'Math', 'Sci'])
plt.show()
'''

# NumPy ndarray - arange()
'''
import numpy as np
A = np.arange(3)
print("A : ", A)

B = np.arange(3.0)
print("B : ", B)

C = np.arange(3, 10)
print("C : ", C)

D = np.arange(3, 10, 2)
print("D : ", D)
'''

# Numpy ndarray - meshgrid()
'''
import numpy as np

x = np.arange(3)
y = np.arange(5)
print("x : \n", x)
print("y : \n", y)

X, Y = np.meshgrid(x, y)
print("X : \n", X)
print("Y : \n", Y)
'''

# Numpy ndarray - vstack(), split()
'''
import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
C = np.vstack((A, B))
print("A : ", A)
print("B : ", B)
print("C : ", C)

D = np.vstack(([1, 2, 3], [4, 5, 6], [7, 8, 9,], [10, 11, 12]))
print("D : \n", D)
E = np.split(D, 2)
print("E : \n", E)
F = np.split(D, [2, 3])
print("F : \n", F)
'''

# testing torch module
'''
import torch

x = torch.rand(5, 3)
print(x)
'''

'''
import torch
import time

if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print("Current device {} is available".format(device))
mtrx_size = 32*512
x = torch.randn(mtrx_size, mtrx_size)
y = torch.randn(mtrx_size, mtrx_size)

print("Comparison of CPU and GPU in matrix multiplications")
print("x = torch.randn({},{})".format(mtrx_size, mtrx_size))
print("y = torch.randn({},{})".format(mtrx_size, mtrx_size))
print("Testing performance of matmul(x,y) with CPU")
t_before = time.time()
result = torch.matmul(x, y)
t_after = time.time()
print("device({}) took {}sec".format(result.device, t_after - t_before))

x_gpu = x.to(device)
y_gpu = y.to(device)
torch.cuda.synchronize()

for i in range(3):
    print("Testing performance of matmul(x, y) with GPU")
    t_before = time.time()
    result_gpu = torch.matmul(x_gpu, y_gpu)
    torch.cuda.synchronize()
    t_after = time.time()
    print("device({}) took {}sec".format(result_gpu.device, t_after - t_before))
'''

# K-means clustering
'''
from cv2 import kmeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

sample_data = np.array([[7, 5], [12, 13], [15, 22], [20, 12], [6, 25],[ 17, 30], [53, 50], [43, 50], [45, 70], [50, 45], [47, 60], [75, 80], [81, 75], [65, 79], [70, 85], [83, 97], [77, 83]])

kmeans = KMeans(n_clusters = 3)
kmeans.fit(sample_data)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
plt.scatter(sample_data[:,0], sample_data[:,1], c = kmeans.labels_, cmap = 'rainbow')
plt.show()
'''

# gradient desent algorithm
'''
import numpy as np
import matplotlib.pyplot as plt

def gradient_desent(start, gradient, learn_rate, max_iter, tol = 0.01):
    steps = [start]
    x = start
    for _ in range(max_iter):
        diff = learn_rate * gradient(x)
        if np.abs(diff) < tol:
            break
        x = x - diff
        steps.append(x)
    return steps, x

def func1(x):
    return x**2 - 4*x + 1

def gradient_func1(x):
    return 2*x - 4

x = np.arange(-6, 10.1, 0.5)
y = func1(x)

learn_rates = [0.1, 0.3, 0.8, 0.9]
fig, ax = plt.subplots(2, 2)
plt.subplots_adjust(hspace = 0.35)
plt.rc('figure', figsize = (8, 8))
fig.suptitle("y(x) = x**2 - 4*x + 1; x0 = 9")

for i in range(2):
    for j in range(2):
        ax[i][j].plot(x, y, "r-")
        learn_rate = learn_rates[i*2 + j]
        history, result = gradient_desent(9, gradient_func1, learn_rate, 100)
        print("history = ", history)
        y_h = list(map(func1, history))
        ax[i][j].plot(history, y_h, "bd-")
        ax[i][j].set_title("learn_rate = {}".format(learn_rate))
        ax[i][j].grid()

plt.show()
'''

# Estimations with Linear regression using scikit-learn
'''
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("student_info.csv")
print("df.head() => ")
print(df.head())
print(df.tail())
x = df["height_cm"]
X = x.values.reshape(-1, 1)
y = df["weight_kg"]
plt.plot(x, y, 'o')
plt.xlabel("height (cm)")
plt.ylabel("weight (kg)")

line_fitter = LinearRegression()
line_fitter.fit(X, y)
plt.plot(x, y, 'o')
py = line_fitter.predict(X)
plt.plot(x, py)

test_heights = ([[140]], [[150]], [[160]], [[170]], [[180]], [[190]])
for TH in test_heights:
  pw = line_fitter.predict(TH)
  h = TH[0][0]
  print("height {} cm => predicted_weight {:6.2f} kg".format(h, pw[0]))
'''

# keras application - linear regression

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

X = data = np.linspace(1, 2, 50)
Y = X*4 + np.random.randn(50) * 0.3

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(1, input_dim = 1, activtion = 'linear'))

model.compile(optimizer = 'sgd', loss = 'mes', metrics = ['mse'])
model.fit(X,Y, batch_size = 1, epochs = 20, verbose = 2)

predict = model.predict(data)
plt.plot(data, predict, 'r', label = 'linear regression')
plt.plot(data, Y, 'k.', label = 'training data')
plt.title("Linear regression with keras")
plt.legend(loc = "best")
plt.show()