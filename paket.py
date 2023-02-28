from pkg.modul1 import *
from pkg.modul2 import *
from pkg.hitungnilai import *

def main():
    #Memanggil fungsi-fungsi dalam modul 1
    f1()
    f2()
    #Memanggil fungsu-fungsi dalam modul 2
    f3()
    f4()
    print('Nilai Akhir : ',hitung_nilai(80,90))
    print('Nilai Akhir : ', hitung_kali(80,90))
main()