password = input('Nhập mật khẩu : ')

if len(password) < 6:
    print('Mật khẩu quá ngắn')
    exit()

chuaChuCai = False
for c in password:
    C = c.upper()
    if (C >= 'A' and C <= 'Z'):
        chuaChuCai = True
        break

if not chuaChuCai:
    print('Mật khẩu cần chứa ít nhất một chữ cái (a-z/A-Z)')
    exit()

chuaChuSo = False
for c in password:
    if c >= '0' and c <= '9':
        chuaChuSo = True
        break

if not chuaChuSo:
    print('Mật khẩu cần chứa ít nhất một chữ số (0-9)')
    exit()

print('Mật khẩu bạn chọn hợp lệ !')
