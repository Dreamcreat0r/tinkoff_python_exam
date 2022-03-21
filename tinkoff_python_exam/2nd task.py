# Вам даны три неизвестных числа, обозначенных ﻿aa﻿, ﻿bb﻿, ﻿cc﻿, а также все попарные сравнения этих чисел друг с другом. 
# Напишите программу, которая выведет эти числа в порядке возрастания (неубывания).

# Формат входных данных
# Вводятся три строки. 
# В первой записан результат сравнения между собой чисел ﻿aa﻿ и ﻿bb﻿. 
# Во второй строке — результат сравнения ﻿aa﻿ и ﻿cc﻿. 
# В третьей строке — результат сравнения ﻿bb﻿ и ﻿cc﻿. 
# Результат сравнения выражается соответствующим знаком — символом "﻿<<﻿", "﻿>>﻿" или "﻿==﻿".

# Формат выходных данных
# Выведите символы ﻿aa﻿, ﻿bb﻿, ﻿cc﻿ без разделителей в порядке возрастания (неубывания) соответствующих чисел, 
# каждое следующее число должно быть не меньше предыдущего. 
# Если возможных вариантов ответа несколько, выведите их все в лексикографическом порядке (порядок, использующийся для сравнения строк в словаре).

a2b = input()
a2c = input()
b2c = input()
comps = {}

if a2b == '>':
    a, b = 3, 1
elif a2b == '=':
    a, b = 3, 3
else:
    a, b = 1, 3
comps.update({'a':a, 'b':b})

if a2c == '>':
    c = a-2
elif a2c == '=':
    c = a
else:
    c = a+2
comps.update({'c':c})

if b2c == '>':
    b = c+1
elif b2c == '=':
    b = c
else:
    b = c-1
comps.update({'b':b})


sorted_keys = sorted(comps, key=comps.get)

for i in sorted_keys:
    print(i, end='')

# рациональней было сделать на классах, но допер слишком поздно, а переделывать - время