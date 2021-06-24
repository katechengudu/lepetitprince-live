from original_text.models import *
from rawdata.models import Rawdata
from original_text.models import Sentence,Paragraph

datas = Rawdata.objects.all()
total = len(datas)
print(total)

datas = Sentence.objects.all()
total = len(datas)
print(total)

datas = Paragraph.objects.all()
total = len(datas)
print(total)

