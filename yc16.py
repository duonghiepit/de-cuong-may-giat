"""
    Có bao nhiêu loại máy giặt (Có tên khác nhau) đã bán trong tháng
x năm 2023
"""

with open('BanHang.txt', mode='r', encoding='UTF-8') as file:
    data = file.read()

data = data.split('\n')     #data = ['01:54:43 27/09/2023 1,12497,Pana,11,1,2,24000000.0', '01:55:04 27/09/2023 2,67124,Sonic,4,3,1,10000000.0', '01:55:36 27/09/2023 3,178,Troluc,20,3,1,6800000.0', '']

x = input('Nhập tháng x (1-12): ')
lst = []
for info in data[:-1]:
    tmp = info.split()      #tmp = ['01:54:43', '27/09/2023', '1,12497,Pana,11,1,2,24000000.0,48000000.0']
    if tmp[2].split(',')[4]==x:
        lst.append(tmp[2].split(',')[2])

print(f'Có {len(set(lst))} loại máy giặt được bán trong tháng {x}!')