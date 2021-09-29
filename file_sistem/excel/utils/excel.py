from pathlib import Path
import json

import openpyxl
from django.conf import settings
import os
import pathlib


def find_file(path):
    for root, dirs, files in os.walk(path):
        for fn in files:
            if fn.endswith('.xlsx'):
                return fn


def list_files(path):
    return [f for root, dirs, files in os.walk(path) for f in files if f.endswith('.pdf')]
    # lst = []
    # for root, dirs, files in os.walk(path):
    #
    #     for fn in files:
    #         lst.append(fn)
    # return lst


def files(val):
    return list_files(Path(val))


def read_json(path) -> json:
    fn = f'{Path.cwd()}/{path}'
    fn = Path(fn)
    with open(fn, encoding='utf-8') as f:
        data = json.load(f)
        return data


def get_excel(val):
    strpath = r'D:\Django\test\file_sistem\static'
    fn = r'24П4021Е_поставлен экран 65мм+ новые вставки_полный протокол_27.06.14.xlsx'

    # path = settings.BASE_DIR / 'static/24П4021Е_поставлен экран 65мм+ новые вставки_полный протокол_27.06.14.xlsx'
    # for root, dirs, files in os.walk(strpath):
    #     print(files)
    path = Path(strpath, fn)
    if val is not None or val != "":
        path = Path(val['path'])
    if Path.exists(path):
        fn = find_file(path)
        wb = openpyxl.load_workbook(Path(path, fn))
        sheet = wb.active
        cells = sheet['B27': 'R35']
        for row in cells:
            val = ''
            if row[0].value is None:
                continue
            for cell in row:
                if cell.value is not None:
                    val = val + str(cell.value) + ' '
            print(val)
