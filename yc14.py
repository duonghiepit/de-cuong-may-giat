"""
    Hiển thị danh sách các hóa đơn có tên máy giặt x và có số lượng
bán từ y trở lên, gồm các thông tin: Số hóa đơn, tên máy giặt và số lượng.
"""

with open('BanHang.txt', mode='r', encoding='UTF-8') as file:
    data = file.read()

data = data.split('\n')     #data = ['01:54:43 27/09/2023 1,12497,Pana,11,1,2,24000000.0', '01:55:04 27/09/2023 2,67124,Sonic,4,3,1,10000000.0', '01:55:36 27/09/2023 3,178,Troluc,20,3,1,6800000.0', '']

x = input('Nhập tên máy giặt: ')
y = int(input('Nhập số lượng y: '))

print(f'Danh sách các hóa đơn có tên máy giặt {x}, bán từ {y} máy trở lên: ')
for info in data[:-1]:
    tmp = info.split()      #tmp = ['01:54:43', '27/09/2023', '1,12497,Pana,11,1,2,24000000.0,48000000.0']
    if tmp[2].split(',')[2]==x and int(tmp[2].split(',')[5])>=y:
        print('Số hóa đơn: {}, Tên máy giặt: {}, Số lượng: {}'.format(tmp[2].split(',')[1], tmp[2].split(',')[2], tmp[2].split(',')[5]))