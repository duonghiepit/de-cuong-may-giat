"""
    Bổ sung thêm thông tin Thành tiền cho mỗi hóa đơn bán máy giặt trong tập tin text. Và tính giá trị thành tiền cho mỗi hóa đơn.
    Biết rằng: Thành tiền=Số lượng x Đơn giá
"""

with open('BanHang.txt', mode='r', encoding='UTF-8') as file:
    data = file.readlines()

for i, info in enumerate(data):
    tmp = info.split()
    soluong = int(tmp[2].split(',')[5])
    dongia = float(tmp[2].split(',')[6])
    thanhtien = soluong*dongia
    data[i] = info.replace('\n', f',{thanhtien}\n')

with open('BanHang.txt', mode='w', encoding='UTF-8') as file:
    file.write(''.join(data))
