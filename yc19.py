"""
    Hiển thị các hóa đơn có trùng tên máy giặt trong tháng 2/2023 và
tháng 4/2023
"""

with open('BanHang.txt', mode='r', encoding='UTF-8') as file:
    data = file.read()

data = data.split('\n')     #data = ['01:54:43 27/09/2023 1,12497,Pana,11,1,2,24000000.0', '01:55:04 27/09/2023 2,67124,Sonic,4,3,1,10000000.0', '01:55:36 27/09/2023 3,178,Troluc,20,3,1,6800000.0', '']

lst_m2 = []
lst_m4 = []
for info in data[:-1]:
    tmp = info.split()      #tmp = ['01:54:43', '27/09/2023', '1,12497,Pana,11,1,2,24000000.0,48000000.0']
    if tmp[2].split(',')[4]=='2':
        lst_m2.append(tmp[2].split(',')[2])
    elif tmp[2].split(',')[4]=='4':
        lst_m4.append(tmp[2].split(',')[2])

print('\nDanh sách các hóa đơn có trùng tên máy giặt trong tháng 2/2023 và tháng 4/2023')
for info in data[:-1]:
    tmp = info.split()     
    if tmp[2].split(',')[2] in list(set(lst_m2)&set(lst_m4)) and tmp[2].split(',')[4] in ['2', '4']:
        print(info)
