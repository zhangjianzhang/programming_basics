"""
get the specific information of an valid ID number, including area, gender, age, and constellation.
"""

from .areas import area_dict

def full_area(ids):
    num = ids[:6]
    sheng = ''
    shi = ''
    xian = ''
    # 34个省级行政区
    if num[:2] + '0000' in area_dict.keys():
        sheng = area_dict[num[:2] + '0000'].strip()
    # 某些省级行政区没有下级地级市编码，如澳门特别行政区
    if num[:4] + '00' in area_dict.keys():
        if num != num[:2] + '0000':
            shi = area_dict[num[:4] + '00'].strip()
    # 某些地级市没有下级县(区)编码，如中山市，东莞市
    if num != num[:4] + '00':
        xian = area_dict[num].strip()

    area = sheng + shi + xian
    
    return area
    
def cal_age(ids):
    year = 2022
    month = 10
    day = 25
    birth_year = int(ids[6:10])
    birth_month = int(ids[10:12])
    birth_day = int(ids[12:14])
    age = year - birth_year
    if birth_month > month:
        age = age - 1
    elif birth_month < month:
        pass
    else:
        if birth_day <= day:
            age = age - 1
    return age

def get_gender(ids):
    num = int(ids[-4:-1])
    if num % 2 == 1:
        return '男'
    else:
        return '女'
        
def get_constellation(ids):
    month = int(ids[10:12])
    day = int(ids[12:14])
    if month == 12:
        astro_sign = '射手' if (day < 22) else '摩羯'
    elif month == 1:
        astro_sign = '摩羯' if (day < 20) else '水瓶'
    elif month == 2:
        astro_sign = '水瓶' if (day < 19) else '双鱼'
    elif month == 3:
        astro_sign = '双鱼' if (day < 21) else '白羊'
    elif month == 4:
        astro_sign = '白羊' if (day < 20) else '金牛'
    elif month == 5:
        astro_sign = '金牛' if (day < 21) else '双子'
    elif month == 6:
        astro_sign = '双子' if (day < 21) else '巨蟹'
    elif month == 7:
        astro_sign = '巨蟹' if (day < 23) else '狮子'
    elif month == 8:
        astro_sign = '狮子' if (day < 23) else '处女'
    elif month == 9:
        astro_sign = '处女' if (day < 23) else '天秤'
    elif month == 10:
        astro_sign = '天秤' if (day < 23) else '天蝎'
    elif month == 11:
        astro_sign = '天蝎' if (day < 22) else '射手'
    return astro_sign

def getinfo(ids):
    area = full_area(ids)
    age = cal_age(ids)
    gender = get_gender(ids)
    astro = get_constellation(ids)
    print("性别: {}\n年龄: {}\n星座: {}\n地址: {}".format(gender, age, astro, area))
    
    
