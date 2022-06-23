from django.shortcuts import render, HttpResponse
import pandas as pds
from home.models import Filedata
from datetime import datetime
# Create your views here.


def index(request):
    if  request.method == 'POST':
        imageData = request.FILES['excel_file']
        file = (imageData)
        newData = pds.read_excel(file)
        for i in range(len(newData)) :
            print(newData.loc[i, "Child Part Number"], newData.loc[i, "Child Part Description"])
            document = Filedata(
                child_part_no=newData.loc[i, "Child Part Number"],
                child_part_description=newData.loc[i, "Child Part Description"],
                item_ref_number=newData.loc[i, "item reference number"],
                quantity_production=newData.loc[i, "quantity production"],
                created_on=datetime.today(),
            )
            document.save()
        return HttpResponse(newData.to_json(orient = 'records'))
    else:
        return render(request, 'home.html')


def list(request):
    fetchedData = Filedata.objects.all()
    context = {
        "data": fetchedData
    }
    return render(request, 'list.html', context)
