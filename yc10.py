"""
    Hiển thị danh sách các hóa đơn có thành tiền trên x triệu đồng bán
trong tháng y và tháng z năm 2023 (Nếu z nhập giá trị từ 10 trở lên hoặc 0
trở xuống thì báo lỗi và yêu cầu nhập lại)
"""

with open('BanHang.txt', mode='r', encoding='UTF-8') as file:
    data = file.read()

data = data.split('\n')     #data = ['01:54:43 27/09/2023 1,12497,Pana,11,1,2,24000000.0', '01:55:04 27/09/2023 2,67124,Sonic,4,3,1,10000000.0', '01:55:36 27/09/2023 3,178,Troluc,20,3,1,6800000.0', '']

x = float(input('Nhập x (triệu đồng): '))

while True:
    try:
        z = int(input('Nhập tháng z (1-10): '))
        if z<=0 or z>10:
            print('Vui lòng nhập tháng lớn hơn 0 và nhỏ hơn hoặc bằng 10!')
            continue
    except:
        print('Tháng nhập phải là 1 số nguyên dương (từ 1-10)!')
        continue
    break

y = int(input('Nhập tháng y (1-12): '))

print(f'\nDanh sách hóa đơn bán hàng có thành tiền lớn hơn {x} triệu đồng, bán trong tháng {z} và {y}: ')
for info in data[:-1]:
    tmp = info.split()      #tmp = ['01:54:43', '27/09/2023', '1,12497,Pana,11,1,2,24000000.0,48000000.0']
    if float(tmp[2].split(',')[-1])>x*1000000 and tmp[2].split(',')[4] in [f'{z}', f'{y}']:
        print(info)