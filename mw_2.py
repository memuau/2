similar_chars = {'A': '4', 'B': 'DO80', 'C': '', 'D': 'ODB0', 'E': 'F', 'F': 'E', 'G': '', 'H': '', 
'I': '1L', 'J': '', 'K': '', 'L': '1J', 'M': 'NW', 'N': 'MW', 'O': '0UD', 'P': 'R', 'R': 'P', 'S': '5', 
'T': '', 'U': 'OD', 'V': 'WNMU', 'W': 'MN', 'X': '', 'Y': '', 'Z': '2', '0': 'OUD', '1': 'IL', '2': 
'Z', '3': '', '4': 'A','5': 'S', '6': '', '7': '', '8': 'BO0', '9': ''} ## kluczem jest znak, a wartością znaki wyglądające podobnie

unique_plates = ['W1SMART', 'NUDE202', 'NODE202', 'NDDE202', 'NDDE202J', 'WDDE202', 'NDDE20',
 'WODE202', 'NDDEQ', 'NUDE302', 'NDDE', 'NDDE302', 'WU0E02', 'NODE302', 'NOBE202',
 'NDDE20E', 'NODE03', 'NUDED', 'NOBE20', 'NDBE202', 'NODE20E', 'NDDE02', 'WDDEQ',
 'NODEED2', 'WUDE202', 'NDDEEDE', 'WDDE20E', 'NDE202', 'NDDE003', 'NUE202',
 'NODEQE', 'NUDE20E', 'WDBE202', 'ND0E02', 'NOBE302', 'NDDED', 'NU0E20', 'WDBE02',
 'NODEQ', 'NODEDE', 'WODE20E', 'NDDEDC', 'NU0E202', 'NUOE02', 'NODE02', 'NODE20',
 'NOBE402', 'NODEED', 'NDDEED', 'NUBE202', 'NDDEEOE', 'NODE', 'NOBEDE', 'WDBE302',
 'NUDEEDE', 'NUDE02', 'NDDEEO2', 'WDBEQ', 'NUDE33', 'NDBE20E', 'NDOE202', 'NDBED',
 'NOBE20E', 'NDDE272',]


def similarity(a: str, b: str):
    big_counter = 0
    pairs = list(zip(a,b))
    for pair in pairs:
        small_counter = 0
        if pair[0] == pair[1]:
            small_counter +=1
        elif pair[1] in similar_chars[pair[0]]:
            small_counter +=0.75
        big_counter += small_counter
        small_counter = 0
    ratio = big_counter/len(pairs)
    ratio = ratio - abs(len(a) - len(b))/max(len(a), len(b))
    if ratio > 0:
        return ratio
    else:
        return 0
