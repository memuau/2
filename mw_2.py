from difflib import SequenceMatcher
import pandas as pd

similar_chars = {'A': '4', 'B': 'DO80', 'C': '', 'D': 'O8B0', 'E': 'F', 'F': 'E', 'G': '', 'H': '', 
'I': '1L', 'J': '', 'K': '', 'L': '1J', 'M': 'NW', 'N': 'MW', 'O': '0UD', 'P': 'R', 'R': 'P', 'S': '5', 
'T': '', 'U': 'OD', 'V': 'WNMU', 'W': 'MN', 'X': 'Y', 'Y': 'X', 'Z': '2', '0': 'OUD', '1': 'IL', '2': 
'Z', '3': '', '4': 'A','5': 'S', '6': '', '7': '', '8': 'BO0', '9': ''} ## kluczem jest znak, a wartością znaki wyglądające podobnie

unique_plates = ['W1SMART', 'NUDE202', 'NODE202', 'NDDE202', 'NDDE202J', 'WDDE202', 'NDDE20',
 'WODE202', 'NDDEQ', 'NUDE302', 'NDDE', 'NDDE302', 'WU0E02', 'NODE302', 'NOBE202',
 'NDDE20E', 'NODE03', 'NUDED', 'NOBE20', 'NDBE202', 'NODE20E', 'NDDE02', 'WDDEQ',
 'NODEED2', 'WUDE202', 'NDDEEDE', 'WDDE20E', 'NDE202', 'NDDE003', 'NUE202',
 'NODEQE', 'NUDE20E', 'WDBE202', 'ND0E02', 'NOBE302', 'NDDED', 'NU0E20', 'WDBE02',
 'NODEQ', 'NODEDE', 'WODE20E', 'NDDEDC', 'NU0E202', 'NUOE02', 'NODE02', 'NODE20',
 'NOBE402', 'NODEED', 'NDDEED', 'NUBE202', 'NDDEEOE', 'NODE', 'NOBEDE', 'WDBE302',
 'NUDEEDE', 'NUDE02', 'NDDEEO2', 'WDBEQ', 'NUDE33', 'NDBE20E', 'NDOE202', 'NDBED',
 'NOBE20E', 'NDDE272'] #wczytane z zadania 1 na potrzeby badawcze


def similarity_2(a: str, b: str, similar_char_tolerance: float):
    match = SequenceMatcher(None, a, b).find_longest_match(0, len(a), 0, len(b)) # na początku znajduję najdłuższy identyczny substring,
    # robię to po to, aby "wygładzić" skutki braku jednego znaku w środku stringa, które w poprzednim algorytmie mocno zaniżały wynik
    new_a = a[:match.a] + a[match.a+match.size:]
    new_b = b[:match.b] + b[match.b+match.size:]
    #print(new_a)
    #print(new_b)
    #od tego miejsca funkcja ma taki sam przebieg, ale rozważa już tylko stringi pomniejszone o największy wspólny substring
    big_counter = 0 # na końcu zostanie podzielony przez liczbę znaków aby otrzymać średnie podobieństwo
    pairs = list(zip(new_a,new_b)) # z obu napisów tworzę pary znaków występujących na tych samych miejscach
    for pair in pairs:
        small_counter = 0 
        if pair[0] == pair[1]:
            small_counter +=1 # znaki są takie same
        elif pair[1] in similar_chars[pair[0]]:
            small_counter += similar_char_tolerance # tę wartość można jeszcze dostroić
        big_counter += small_counter 
        small_counter = 0
    return ((match.size * (max(len(a), len(b)) - abs(match.a - match.b))/max(len(a), len(b))) + big_counter )/max(len(a), len(b))


dflist = []
for plate in unique_plates :
    mylist = []
    #print(f"NODE202 and {plate} {similarity_2(unique_plates[2], plate, 0.5)}")
    mylist.append(f"NODE202 and {plate}")
    mylist.append(similarity_2(unique_plates[2], plate, 0.4))
    mylist.append(similarity_2(unique_plates[2], plate, 0.5))
    mylist.append(similarity_2(unique_plates[2], plate, 0.6))
    mylist.append(similarity_2(unique_plates[2], plate, 0.7))
    mylist.append(similarity_2(unique_plates[2], plate, 0.8))
    mylist.append(similarity_2(unique_plates[2], plate, 0.9))
    dflist.append(mylist)


out = pd.DataFrame(dflist, columns=["Porównywane napisy", "0,4", "0,5", "0,6", "0,7", "0,8", "0,9"])
out.to_excel("tolerance_0_4_to_0_9.xlsx")

#wygenerowałem excela z danymi, które posłużą mi do wybrania optymalnej wartości współczynnika 'similar_char_tolerance'