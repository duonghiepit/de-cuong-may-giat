"""
    Hiển thị danh sách các hóa đơn có thành tiền dưới x triệu đồng và các
hóa đơn có thành tiền trên y triệu đồng
"""

with open('BanHang.txt', mode='r', encoding='UTF-8') as file:
    data = file.read()

data = data.split('\n')     #data = ['01:54:43 27/09/2023 1,12497,Pana,11,1,2,24000000.0', '01:55:04 27/09/2023 2,67124,Sonic,4,3,1,10000000.0', '01:55:36 27/09/2023 3,178,Troluc,20,3,1,6800000.0', '']

x, y = map(float, input('Nhập x, y (triệu đồng) (Cách nhau bởi dấu cách): ').split())
print(f'\nDanh sách hóa đơn bán hàng có thành tiền nhỏ hơn {x} triệu đồng hoặc lớn hơn {y} triệu đồng: ')
for info in data[:-1]:
    tmp = info.split()      #tmp = ['01:54:43', '27/09/2023', '1,12497,Pana,11,1,2,24000000.0,48000000.0']
    if float(tmp[2].split(',')[-1])<x*1000000 or float(tmp[2].split(',')[-1])>y*1000000:
        print(info)