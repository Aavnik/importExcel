from django.shortcuts import render, redirect
import pandas as pd
from .models import *
import xlwt
from django.http import HttpResponse
from django.conf import Settings


# Create your views here.

def excelfile(request):

    if request.method == "POST":
        excelfile = request.FILES['excelfile']
        handelfile = HandleExcel.objects.create(excelfile = excelfile)

        datas = pd.read_excel(handelfile.excelfile)

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


def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Books.xls"'

    wb = xlwt.Workbook(encoding='utf-8')

    ws = wb.add_sheet('Album') 
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['artist', 'name', 'release_date', 'num_stars', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)


    font_style = xlwt.XFStyle()
   # aa = Musician.objects.all()
    rows = Album.objects.values_list('artist', 'name', 'release_date', 'num_stars')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response    