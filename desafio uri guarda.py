while True:
    try:
        from math import sqrt

        d, vf, vg = input().split()
        VF = int(vf)
        D = int(d)
        VG = int(vg)
        if  D >= 1 and D <= 100 and VF >= 1 and VF <= 100 and VG >= 1 and VG <= 100:
            dist_g = sqrt(D**2 + 144)
            tempo_g = dist_g/VG
            tempo_f = 12/VF
            if tempo_g > tempo_f:
                 print("N")
            else:
                print("S")
        else: break
    except EOFError:
        break