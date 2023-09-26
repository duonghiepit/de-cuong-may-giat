"""
    Hiển thị danh sách các hóa đơn có thành tiền dưới z triệu đồng gồm các thông tin: Số hóa đơn, Tên máy giặt và Thành tiền
"""

with open('BanHang.txt', mode='r', encoding='UTF-8') as file:
    data = file.read()

data = data.split('\n')     #data = ['01:54:43 27/09/2023 1,12497,Pana,11,1,2,24000000.0', '01:55:04 27/09/2023 2,67124,Sonic,4,3,1,10000000.0', '01:55:36 27/09/2023 3,178,Troluc,20,3,1,6800000.0', '']

z = float(input('z (triệu đồng) = '))
for info in data[:-1]:
    tmp = info.split()      #tmp = ['01:54:43', '27/09/2023', '1,12497,Pana,11,1,2,24000000.0,48000000.0']
    if float(tmp[2].split(',')[-1])<z*1000000:
        print('Số hóa đơn: {}, Tên máy giặt: {}, Thành tiền: {}'.format(tmp[2].split(',')[1], tmp[2].split(',')[2], tmp[2].split(',')[-1]))