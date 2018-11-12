from sympy import sqrt

a = 1.2
b = 2
n = 4
h = (b - a) / n
vuzol = a
x_array = []


for i in range(0, n + 1):
    x_array.append(round(vuzol, 3))
    vuzol = vuzol + h


def f(x):
    return sqrt(1 + 2 * (x**2) - x**3)


def paired_array_f(x_array):
    paired_array = []
    for i in range(len(x_array)):
        if i % 2 == 0 and i != 0 and i != n:
            paired_array.append(f(x_array[i]))
    return paired_array


def unpaired_array_f(x_array):
    unpaired_array = []
    for i in range(len(x_array)):
        if i % 2 != 0 and i != 0 and i != n:
            unpaired_array.append(f(x_array[i]))
    return unpaired_array


def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum


def simpson_method(h, x_array):
    paired_elements = listsum(paired_array_f(x_array))
    unpaired_elements = listsum(unpaired_array_f(x_array))
    answer = (h / 3) * (f(x_array[0]) + f(x_array[-1]) + 2 * paired_elements + 4 * unpaired_elements)
    return answer


def average_rectangle(h):
    average_rectangle_array = []
    for i in range(n):
        average_rectangle_array.append(f(x_array[i] + h / 2))
    average_rectangle_elements = listsum(average_rectangle_array)
    answer = h * (average_rectangle_elements)
    return answer


s = simpson_method(h, x_array)
av = average_rectangle( h)


def check(s, av):
    if av > s:
        return True


if __name__ == '__main__':
    print("f(x) = sqrt(1+2*(x**2)-x**3)")
    print('a =', a, 'b =', b)
    print("Simpson method")
    print(simpson_method(h, x_array))
    print('Average rectangle method')
    print(average_rectangle(h))




