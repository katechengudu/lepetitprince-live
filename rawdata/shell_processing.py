from original_text.models import *
from rawdata.models import Rawdata
from original_text.models import Sentence,Token

datas = Rawdata.objects.all()
total = len(datas)
print(total)
datas.delete()

datas = Sentence.objects.all()
total = len(datas)
print(total)
datas.delete()

datas = Token.objects.all().values_list('pos', flat=True).distinct()
total = len(datas)
print(total)
pos=[]
for data in datas:
    pos.append(data)
print(pos)




# 打印出有重复的：打印出来看看
i = 1
for data in datas:
    duplicates = Rawdata.objects.filter(pk__in=Rawdata.objects.filter(content_lower_case=data).values_list('id', flat=True)[1:])
    print(len(duplicates))
    for duplicate in duplicates:
        print(duplicate)
    print(f'---------{i} OUT OF {total}--------------')
    i = i+1


