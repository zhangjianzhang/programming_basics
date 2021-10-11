
#BMI指数计算

Height = int(input("请输入身高(m):"))
Weight = int(input("请输入体重(kg):"))

BMI = Weight/Height**2

if BMI>=23.9:
    print("BMI指数为", BMI, "体质偏重")
elif BMI<=18.5:
    print("BMI指数为", BMI, "体质偏轻")
else:
    print("BMI指数为", BMI, "正常")


