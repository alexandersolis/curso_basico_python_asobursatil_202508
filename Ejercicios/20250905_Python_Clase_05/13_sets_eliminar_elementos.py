set1 = set()
set1.add("ABC")
set1.add(30)
set1.add('99')

set1['99'] = 200
#esto generaria un error, el elemento 99 no puede ser modificado
print(set1)