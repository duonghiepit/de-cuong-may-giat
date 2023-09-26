"""
    Tính số tiền trung bình theo từng hóa đơn đã bán trong tháng x năm 2023
"""

with open('BanHang.txt', mode='r', encoding='UTF-8') as file:
    data = file.read()

data = data.split('\n')     #data = ['01:54:43 27/09/2023 1,12497,Pana,11,1,2,24000000.0', '01:55:04 27/09/2023 2,67124,Sonic,4,3,1,10000000.0', '01:55:36 27/09/2023 3,178,Troluc,20,3,1,6800000.0', '']

x = input('Nhập tháng x (1-12): ')
c = 0
s = 0
for info in data[:-1]:
    tmp = info.split()      #tmp = ['01:54:43', '27/09/2023', '1,12497,Pana,11,1,2,24000000.0,48000000.0']
    if tmp[2].split(',')[4]==x:
        s += float(tmp[2].split(',')[-1])
        c += 1

print(f'Thành tiền trung bình mỗi hóa đơn bán máy giặt trong tháng {x} là {round(s/c, 2)}!')