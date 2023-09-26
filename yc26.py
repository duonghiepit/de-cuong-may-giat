"""
    Xác định Số hóa đơn và tên máy giặt có thành tiền lớn nhất đã bán
trong tháng x năm 2023.
"""

with open('BanHang.txt', mode='r', encoding='UTF-8') as file:
    data = file.read()

data = data.split('\n')     #data = ['01:54:43 27/09/2023 1,12497,Pana,11,1,2,24000000.0', '01:55:04 27/09/2023 2,67124,Sonic,4,3,1,10000000.0', '01:55:36 27/09/2023 3,178,Troluc,20,3,1,6800000.0', '']

x = input('Nhập tháng x (1-12): ')
tt_max = max([float(element.split()[2].split(',')[-1]) for element in data[:-1] if element.split()[2].split(',')[4]==x])

for info in data[:-1]:
    tmp = info.split()      #tmp = ['01:54:43', '27/09/2023', '1,12497,Pana,11,1,2,24000000.0,48000000.0']
    if tmp[2].split(',')[-1]==f'{tt_max}' and tmp[2].split(',')[4]==x:
        print('Số hóa đơn: {}, Tên máy giặt: {}'.format(tmp[2].split(',')[1], tmp[2].split(',')[2]))