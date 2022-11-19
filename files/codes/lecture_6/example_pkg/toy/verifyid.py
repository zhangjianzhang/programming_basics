"""
check if a ID number is valid.
"""

from toy.areas import area_dict




def verify_char_length(ids):
    if len(ids) != 18:
        return False
    if not ids[:-1].isdigit():
        return False
    if ids[-1] not in '0123456789X':
        return False
    return True

def verify_last_num(ids):
    ids_17 = ids[:-1]
    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    S = sum([int(num)*weight for num,weight in zip(list(ids_17),weights)])
    T = S % 11
    R = (12 - T) % 11
    if R == 10:
        last_num = 'X'
    else:
        last_num = R
    if ids[-1] == str(last_num):
        return True
    else:
        return False

def verify_area(ids):
    if ids[:6] not in area_dict.keys():
        return False
    else:
        return True
        
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
        
        
def verify_date(ids):
    year = int(ids[6:10])
    if year > 2022 or year < 1900:
        return False
    month = int(ids[10:12])
    if month > 12 or month < 1:
        return False
    day = int(ids[12:14])
    if month in [1,3,5,7,8,10,12]:
        if day > 31 or day < 1:
            return False
    elif month in [4,6,9,11]:
        if day > 30 or day < 1:
            return False
    else:
        if is_leap_year(year):
            if day > 29 or day < 1:
                return False
        else:
            if day > 28 or day < 1:
                return False
    return True
    
def verify_id(ids):
    if verify_char_length(ids):
        if all([verify_last_num(ids),verify_area(ids),verify_date(ids)]):
            print("VALID")
            return True
        else:
            print("INVALID")
            return False
    else:
        print("INVALID")
        return False

