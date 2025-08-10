# ex2_scientific1.py
# Chương trình tính toán các phép toán cơ bản

# Nhập 2 số
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

# Thực hiện các phép toán
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b if b != 0 else "Không chia được cho 0"

# Hiển thị kết quả
print(f"Tổng: {tong}")
print(f"Hiệu: {hieu}")
print(f"Tích: {tich}")
print(f"Thương: {thuong}")

