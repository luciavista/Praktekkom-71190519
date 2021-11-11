ikan = 25000
es = 6000
rujak = 8000

print("===== MASUKKAN JUMLAH MAKANAN YANG DIPESAN =====")

ikanbakar  = int(input("IKAN BAKAR      Rp 25.000,00   : "))
esdoger = int(input("ES DOGER        Rp 6.000,00    : "))
rujakcingur = int(input("RUJAK CINGUR    Rp 8.000,00    : "))

print("===== TOTAL =====")

ikan1 = int(ikan)*ikanbakar
es1 = int(es)*esdoger
rujak1 = int(rujak)*rujakcingur

print("TOTAL IKAN BAKAR     : Rp ", ikan1)
print("TOTAL ES DOGER       : Rp ", es1)
print("TOTAL RUJAK CINGUR   : Rp ", rujak1)

print("Jumlah total biaya yang harus dibayar adalah Rp", ikan1+es1+rujak1)
