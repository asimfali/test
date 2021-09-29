from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .utils.excel import get_excel, list_files, read_json
from django.views.generic.base import View
from .forms import PathForm
import json
from pathlib import Path
from .fill import test_import


def read_excel(request):
    get_excel()
    return render(request, 'test.html')


def get_path(request):
    if request.method == 'POST':
        form = PathForm(request.POST)
        if form.is_valid():
            # get_excel(form.cleaned_data)
            clean = form.cleaned_data
            path = clean['path']
            fs = list_files(path)

            # return HttpResponseRedirect('/')
    else:
        fs = ''
        path = ''
        form = PathForm()

    return render(request, 'path.html', {'form': form, 'files': fs, 'path': path})


#
# def pdfView(request):
#     filename = 'media/A_EKD_KEV_P2211E_book_A4-A3.pdf'
#     # filename = filename.encode('utf-8')
#     with open(settings.BASE_DIR / filename, 'rb') as pdf:
#         res = HttpResponse(pdf.read(), content_type='application/pdf')
#         res['Content-Disposition'] = 'inline;filename=test.pdf'
#         return res

def get_file(request):
    if request.method == 'POST':
        # return 'test'
        data = json.loads(request.body)
        filename = Path(data['fn'])
    else:
        filename = request.GET['fn']
    # filename = filename.encode('utf-8')
    with open(filename, 'rb') as pdf:
        res = HttpResponse(pdf.read(), content_type='application/pdf')
        res['Content-Disposition'] = 'inline;filename=test.pdf'
        return res


class Test(View):
    name = 'excel.models.Category'
    template_name = 'path.html'

    def get(self, request):
        data = read_json('excel/test.json')
        [test_import(e) for e in data]
        # test_import(self.name, data)
        form = PathForm(request)
