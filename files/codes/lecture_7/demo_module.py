'''
This is a demo module
'''

import string


def my_print(content):
    '''
    print alphabets characters vertically.
    '''
    alphanum_list = list(filter(lambda char:char in string.ascii_letters, content))
    print('\n'.join(alphanum_list))
