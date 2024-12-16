import re

def elixer(user_info):
    info = user_info.equip_armor()
    elixer_list = list()
    def compile(x):
        x = x.replace('[','<').replace(']','>')
        x = x.lower()
        x = re.sub(r"<fontcolor='#ffd200'>",'',x)
        x = re.sub(r"</font>",'',x)
        x = re.sub(r"<\w\w>",'/',x)
        x = x.strip('/')
        x = x.split('/')
        return x
    for k in [0,3]:
        elixer_1 = info[k]['Element_010']['value']['Element_000']['contentStr']['Element_000']['contentStr']
        elixer_2 = info[k]['Element_010']['value']['Element_000']['contentStr']['Element_001']['contentStr']
        elixer_list.append(compile(elixer_1)[0])
        elixer_list.append(compile(elixer_2)[0])
    return elixer_list


def transcendence(user_info):
    transcendence_all = list()
    info_armor = user_info.equip_armor()
    info_weapon = user_info.equip_weapon()
    def tran_sub(user_info_equip_):
        tran_0 = user_info_equip_['Element_009']['value']['Element_000']['contentStr']['Element_000']['contentStr']
        tran_1 = user_info_equip_['Element_009']['value']['Element_000']['topStr']
        tran_1 = tran_1.replace("<FONTCOLOR='#FFD200'>",'split/').replace("</FONT>",'split/').replace("</img>",'split/')
        tran_1 = tran_1.split('split/')
        tran_1 = tran_1[3]+'단계 '+tran_1[-1]
        return tran_0, tran_1
    for k in range(0,5):
        tuple_tran = tran_sub(info_armor[k])
        transcendence_all.append(tuple_tran)
    transcendence_all.append(tran_sub(info_weapon))
    return transcendence_all


def accessory(user_info):
    info = user_info.equip_accessory()
    acc_list = list()
    for k in range(0,5):
        acc_0 = info[k]['Element_007']['value']['Element_001']
        acc_1 = info[k]['Element_005']['value']['Element_001'].lower().replace("</img>",'split/').replace("<br",'split/').split('split/')
        acc_1 = acc_1[1::2]    
        acc_list.extend(acc_1)
    acc_list_head = [x for x in acc_list if '%' in x]
    acc_list_head = [x for x in acc_list_head if ('파티원' not in x) and ('아군' not in x) and ('상태이상' not in x)]
    return acc_list_head