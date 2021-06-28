from original_text.models import *
from rawdata.models import Rawdata
from original_text.models import Sentence

datas = Rawdata.objects.all()
total = len(datas)
print(total)
datas.delete()

datas = Sentence.objects.all()
total = len(datas)
print(total)
datas.delete()

