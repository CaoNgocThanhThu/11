# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:43:52 2024

@author: Cao Ngọc Thanh Thu 23719291
"""
# phần a
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
solon = max(a,b,c)
sonho = min(a,b,c)
d = a + b + c - solon - sonho
print("Số xếp theo thứ tự tăng dần:",sonho,",",d,",",solon)
# phần b
N = input("nhap mot so nguyen: ")

if N.isdigit():
    digits = list(N)
    digits.sort()
    sorted_number_str = ''.join(digits)
    print("so sau khi sap xep theo thu tu tang dan la:",sorted_number_str )
else:
    print("so khong hop le")