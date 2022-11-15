
def emsokalkulator():
    emso = str(input("Vnesi emso od datuma naprej(14 stevilk): "))
    if emso[4] == "0":
        leto = "2" + emso[4:7:]
        starost = 2022 - int(leto)
        print("Star si %d" % starost)
        #print(starost)
    else:
        leto =  "1" + emso[4:7:]
        starost = 2022 - int(leto)
        print("Star si %d" % starost)
        #print(starost)
    return starost

vrednost = emsokalkulator()
print(vrednost)

