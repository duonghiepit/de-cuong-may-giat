"""
    Tra cứu thông tin của một hóa đơn theo số hóa đơn
"""

with open('BanHang.txt', mode='r', encoding='UTF-8') as file:
    data = file.read()

data = data.split('\n')

shd = input('Nhập số hóa đơn cần tra cứu: ')

for info in data[:-1]:
    tmp = info.split()      #tmp = ['01:54:43', '27/09/2023', '1,12497,Pana,11,1,2,24000000.0,48000000.0']
    if tmp[2].split(',')[1]==shd:
        print('Thời gian nhập hóa đơn: ')
        print('Ngày: ', tmp[0])
        print('Giờ: ', tmp[1])
        print('Tên máy giặt: ', tmp[2].split(',')[2])
        print('Ngày, tháng bán: {}/{}/2023'.format(tmp[2].split(',')[3], tmp[2].split(',')[4]))
        print('Số lượng: ', tmp[2].split(',')[5])
        print('Đơn giá: ', tmp[2].split(',')[-2])
        print('Thành tiền: ', tmp[2].split(',')[-1])