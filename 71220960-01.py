def jumlah_hari(nama_bulan):
  
    hari_31=['januari','maret','mei','juli','agustus','oktober','desember']
    hari_28=['februari']
    hari_30=['april','juni','september','november']
    if nama_bulan in hari_31:
        print('31 Hari')
    elif nama_bulan in hari_28:
        print('28 Hari')
    elif nama_bulan in hari_30:
        print('30 Hari')
    else:print('Tidak Valid')

nama_bulan=input('Masukan Nama Bulan:')
jumlah_hari(nama_bulan)