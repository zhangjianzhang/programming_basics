# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@project: programming_basics_course
@file   : BMI_calculation.py
@version: 1.0
@time   : 2022-09-01
@author : Jianzhang Zhang, <jianzhang.zhang@foxmail.com>
"""

# BMI指数计算

Height = float(input("请输入身高(m): "))
Weight = float(input("请输入体重(kg): "))

BMI = round(Weight/Height**2, 2)

if BMI>=23.9:
    print("BMI指数为", BMI, "体质偏重")
elif BMI<=18.5:
    print("BMI指数为", BMI, "体质偏轻")
else:
    print("BMI指数为", BMI, "正常")


