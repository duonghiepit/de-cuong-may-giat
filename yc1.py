"""
    Nhập k hóa đơn bán máy giặt. Mỗi hóa đơn bán máy giặt gồm các thông tin:
    STT, Số hóa đơn, Tên máy giặt, Ngày bán,Tháng bán, Số Lượng, Đơn giá
"""

from datetime import datetime

with open('BanHang.txt', mode='w', encoding='UTF-8') as file:
    file.write()
    
def ghi_file(content):
    with open('BanHang.txt', mode='a', encoding='UTF-8') as file:
        file.write(content)

def thoigian():
    # Lấy thời gian hiện tại
    now = datetime.now()

    # Định dạng thời gian
    formatted_now = now.strftime("%H:%M:%S %d/%m/%Y")

    return formatted_now

while True:
    try:
        k = int(input('Nhập số lượng hóa đơn bán máy giặt: '))
        if k<=0:
            print('Vui lòng nhập số lượng hóa đơn lớn hơn 0!')
            continue
    except:
        print('Số lượng hóa đơn phải là 1 số nguyên dương!')
        continue
    break


for i in range(k):
    print(f'\nNhập thông tin hóa đơn {i+1}:')
    hoadon = [str(i+1)]
    while True:
        try:
            shd = int(input('Nhập số hóa đơn: '))
            if shd<0:
                print('Vui lòng nhập số hóa đơn lớn hơn 0!')
                continue
        except:
            print('Số hóa đơn phải là 1 số nguyên dương!')
            continue
        break
    hoadon.append(str(shd))

    while True:
        tmg = input('Nhập tên máy giặt: ')
        if tmg.isdigit():
            print('Tên máy giặt không hợp lệ, vui lòng nhập lại!')
            continue
        break
    hoadon.append(tmg)

    while True:
        try:
            ngayban = int(input('Nhập ngày bán: '))
            if ngayban<=0 or ngayban>31:
                print('Ngày bán không hợp lệ, vui lòng nhập lại!')
                continue
        except:
            print('Ngày bán phải là 1 số nguyên dương (1-31)!')
            continue
        break
    hoadon.append(str(ngayban))

    while True:
        try:
            thangban = int(input('Nhập tháng bán: '))
            if thangban<=0 or thangban>12:
                print('Tháng bán không hợp lệ, vui lòng nhập lại!')
                continue
        except:
            print('Tháng bán phải là 1 số nguyên dương (1-12)!')
            continue
        break
    hoadon.append(str(thangban))

    while True:
        try:
            soluong = int(input('Nhập số lượng: '))
            if soluong<0:
                print('Vui lòng nhập số lượng lớn hơn 0!')
                continue
        except:
            print('Số lượng phải là 1 số nguyên dương!')
            continue
        break
    hoadon.append(str(soluong))

    while True:
        try:
            dongia = float(input('Nhập đơn giá: '))
            if dongia<0:
                print('Vui lòng nhập đơn giá lớn hơn 0!')
                continue
        except:
            print('Đơn giá phải là 1 số thực dương!')
            continue
        break
    hoadon.append(str(dongia))

    content = ','.join(hoadon)
    ghi_file(f'{thoigian()} {content}\n')