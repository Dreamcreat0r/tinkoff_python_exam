#Две группы студентов решали контрольную, состоящую из ﻿NN﻿ задач. Известно, что первая группа решила суммарно ﻿AA﻿ задач, 
#а вторая группа — ﻿BB﻿ задач, при этом каждый студент решил хотя бы одну задачу. 
#Вам интересно, могло ли быть в первой группе студентов больше, чем во второй. 
#Напишите программу, позволяющую узнать ответ на этот вопрос.



#Формат входных данных

#Вводятся три целых числа, каждое в своей строке — ﻿A﻿, ﻿B﻿, ﻿N (﻿0 ≤ A, B ≤ 10^4, 1 ≤ N ≤ 10**40 ≤A, B ≤ 10**4, 1 ≤ N ≤ 10**4)


a = input()
b = input()
n = input()

if int(a) > int(b)/int(n):
    print('Yes')
else:
    print('No')