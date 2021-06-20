from django.shortcuts import render, redirect
import pandas as pd
from .models import *


# Create your views here.

def excelfile(request):

    if request.method == "POST":
        excel_file = request.FILES['excel_file']
        handelfile = HandleExcel.objects.create(excel_file = excel_file)

        datas = pd.read_excel(handelfile.excel_file)

        for data in datas.values.tolist():
            Musician_obj, _ = Musician.objects.get_or_create(

                first_name= data[0],
                last_name = data[1],
                instrument = data[2]
            )

            Album.objects.create(

                artist = Musician_obj,
                name = data[3],
                release_date = data[4],
                num_stars = data[5]
            )
        return redirect('/')    

               

    return render(request, 'excelhome.html')
