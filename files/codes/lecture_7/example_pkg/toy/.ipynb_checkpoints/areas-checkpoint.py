"""
load areas and their codes from local file area_dict.json
"""

AREA_DICT = 'area_dict.json'

import os
import _locale

_locale._getdefaultlocale = (lambda *args: ['zh_CN', 'utf8'])



basepath = os.path.abspath(__file__)
folder = os.path.dirname(basepath)
data_path = os.path.join(folder, AREA_DICT)
with open(data_path, encoding = 'utf-8') as f:
    area_dict = eval(f.read())

