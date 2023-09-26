"""
    Hiển thị các hóa đơn không trùng tên máy giặt trong tháng 1/2023
và tháng 3/2023
"""

with open('BanHang.txt', mode='r', encoding='UTF-8') as file:
    data = file.read()

data = data.split('\n')     #data = ['01:54:43 27/09/2023 1,12497,Pana,11,1,2,24000000.0', '01:55:04 27/09/2023 2,67124,Sonic,4,3,1,10000000.0', '01:55:36 27/09/2023 3,178,Troluc,20,3,1,6800000.0', '']

lst_m1 = []
lst_m3 = []
for info in data[:-1]:
    tmp = info.split()      #tmp = ['01:54:43', '27/09/2023', '1,12497,Pana,11,1,2,24000000.0,48000000.0']
    if tmp[2].split(',')[4]=='1':
        lst_m1.append(tmp[2].split(',')[2])
    elif tmp[2].split(',')[4]=='3':
        lst_m3.append(tmp[2].split(',')[2])

print(lst_m1, lst_m3)
print('\nDanh sách các hóa đơn không trùng tên máy giặt trong tháng 1/2023 và tháng 3/2023')
for info in data[:-1]:
    tmp = info.split()     
    if tmp[2].split(',')[2] not in list(set(lst_m1)&set(lst_m3)) and tmp[2].split(',')[4] in ['1', '3']:
        print(info)
