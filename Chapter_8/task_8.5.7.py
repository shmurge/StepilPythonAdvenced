# Используя генератор множеств, дополните приведенный код так, чтобы он выбрал из списка files уникальные
# имена файлов c расширением .png, независимо от регистра имен и расширений. Имена файлов вывести вместе с расширением,
# все на одной строке, в нижнем регистре, в алфавитном порядке через пробел.

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT',
         'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py',
         'stepik.org', 'kotlin.ko', 'github.git']

myset1 = {i.lower() for i in files if ".png" in i.lower()}

print(*sorted(myset1))