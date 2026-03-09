
num1 = float(input("أدخل الرقم الأول: "))

# طلب الرقم الثاني من المستخدم
num2 = float(input("أدخل الرقم الثاني: "))

# طلب العملية
operation = input("اختر العملية (+, -, *, /): ")

# تنفيذ العملية
if operation == "+":
    print("الناتج:", num1 + num2)
elif operation == "-":
    print("الناتج:", num1 - num2)
elif operation == "*":
    print("الناتج:", num1 * num2)
elif operation == "/":
    if num2 != 0:
        print("الناتج:", num1 / num2)
    else:
        print("خطأ: القسمة على صفر غير مسموحة")
else:
    print("عملية غير صحيحة")