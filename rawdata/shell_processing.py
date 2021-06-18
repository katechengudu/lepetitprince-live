from original_text.models import *
from rawdata.models import Rawdata,Source

datas = Rawdata.objects.all()
total = len(datas)
print(total)