ds_lop = []

f = open('diem_trungbinh_input.csv')
for line in f:
    hoten, diemhs1, diemhs2, diemhs3 = line.split(',')
    diemhs1 = int(diemhs1)
    diemhs2 = int(diemhs2)
    diemhs3 = int(diemhs3)
    diem_tb = (diemhs1 + 2*diemhs2 + 3*diemhs3) / 6.0
    ds_lop.append((hoten, diemhs1, diemhs2, diemhs3, diem_tb))

f.close()

f = open('diem_trungbinh_output.csv', 'wt')
for hocsinh in ds_lop:
    hoten, diemhs1, diemhs2, diemhs3, diem_tb = hocsinh    
    line = '{}, {}, {}, {}, {: 1.1f}'.format(hoten, diemhs1, diemhs2, diemhs3, diem_tb)
    f.write(line + '\n')

f.close()
