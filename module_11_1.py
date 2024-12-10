import numpy as np

print("#" * 5, "NUMPY", "#" * 120)
# создание трехмерного массива
mx3 = np.array([[[1, 2, 3, 4], [4, 5, 6, 7]], [[7, 8, 9, 10], [10, 11, 12, 13]]])
# вывод измерения
print(mx3.ndim)
# подсчет количества строк и столбцов
print(mx3.shape)
# количество элементов
print(mx3.size)
# обращение к элементу
print(mx3[1, 1, 1])
# вывод часть строки
print(mx3[0, 1, :-1])

print("*" * 20)
# создание четырехмерного массива
mx4 = np.array(
    [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],
     [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]])
print(mx4.ndim)
print(mx4.shape)
print(mx4.size)
# сумма все элементов
print("сумма все эоементов ", mx4.sum())

# математические операции со всем элементами
print(((mx4 + 5) - 7) * 2 / 3)

mx_1 = np.random.randint(-5, 5, size=(4, 4))
mx_2 = np.random.randint(1, 10, size=(4, 4))
print(mx_1)
print(mx_2)
# математические операции
print("mx2_1 + mx2_2\n", mx_1 + mx_2)
print("mx2_1 * mx2_2\n", mx_1 * mx_2)
print("mx2_1 ** mx2_2\n", mx_1 ** mx_2)

print("#" * 5, "matplotlib", "#" * 120)

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = plt.figure(num="Седло")
ax = fig.add_subplot(111, projection='3d')

# Создаем данные
X = np.arange(-25, 25, 0.1)
Y = np.arange(-25, 25, 0.1)
X, Y = np.meshgrid(X, Y)
R = (X ** 2 / 36) - (Y ** 2 / 49)
Z = R / 3

# Построение поверхности
surf = ax.plot_surface(X, Y, Z, cmap='plasma', linewidth=0, antialiased=False)

# Настройка оси z .
ax.set_zlim(-6.01, 6.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Добавьте цветовую полосу, которая сопоставляет значения с цветами.
fig.colorbar(surf, shrink=0.5, aspect=10)

plt.show()


print("#" * 5, "Pillow", "#" * 120)

from PIL import Image

image = Image.open('6447966456.jpg')
cropped = image.crop((750, 400, 1850, 1800)) # обрезка
cropped = cropped.convert('L') # преобразование в черно-белое
cropped.save('cropped_.png', 'png') # конвертация в другой формат
cropped.show()
image.show()