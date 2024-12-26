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
    
    for k in range(0,5):
        elixer_1 = info[k]['Element_010']['value']['Element_000']['contentStr']['Element_000']['contentStr']
        elixer_2 = info[k]['Element_010']['value']['Element_000']['contentStr']['Element_001']['contentStr']
        elixer_list.append(compile(elixer_1))
        elixer_list.append(compile(elixer_2))

    list_elixeroption = list()
    for e in elixer_list:
        if len(e)==2:
            list_elixeroption.append(e[1])
        if len(e)==4:
            list_elixeroption.extend(e[0:-1])

    dict_stat = {'피해 증가':[],
        '추가 피해':[],
        '공격력 증가 (%)':[],
        '공격력 증가 (+)':[],
        '무기공격력 증가 (%)':[],
        '무기공격력 증가 (+)':[],
        '스탯 증가 (%)':[],
        '스탯 증가 (+)':[],
        '치명타 적중률 증가':[],
        '치명타 피해 증가':[],
        '치명타 시 피해 증가':[],
        '백어택':[],
        '헤드어택':[],
        '비방향성':[],
        '캐스팅':[],
        '차징':[],
        '쿨타임 감소':[],
        '진화형 피해':[],
        '물리 방어력':[],
        '마법 방어력':[],
        '최대 생명력':[],
        }
    
    i = 0
    j = 0

    for e in list_elixeroption:
        if ('무기공격력' in e) and ('%' not in e) :
            dict_stat['무기공격력 증가 (+)'].append(int(e.split('+')[1]))
        if ('공격력' in e) and ('무기' not in e) and ('%' in e):
            dict_stat['공격력 증가 (%)'].append(float(e.replace("%",'').split('+')[1]))
        if ('공격력' in e) and ('무기' not in e) and ('%' not in e):
            dict_stat['공격력 증가 (+)'].append(int(e.split('+')[1]))
        if '추가피해' in e :
            dict_stat['추가 피해'].append(float(e.replace("%",'').split('+')[1]))
        if ('적에게주는피해' in e) or ('보스' in e) :
            dict_stat['피해 증가'].append(float(e.replace("%",'').split('+')[1]))
        if '치명타피해' in e :
            dict_stat['치명타 피해 증가'].append(float(e.replace("%", '').split('+')[1]))
        if '최대생명력' in e :
            dict_stat['최대 생명력'].append(int(e.split('+')[1]))

        if '회심(질서)' in e:
            i += 1
        if '회심(혼돈)' in e:
            i += 1
        if '달인(질서)' in e:
            j += 1
        if '달인(혼돈)' in e:
            j += 1

    if j == 2 :
        dict_stat['추가 피해'].append(8.5)
        dict_stat['치명타 적중률 증가'].append(7)
    if i == 2 :
        dict_stat['치명타 시 피해 증가'].append(1.12)

    return dict_stat


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
        return [tran_0, tran_1]
    
    for k in range(0,5):
        transcendence_all.extend(tran_sub(info_armor[k]))

    transcendence_all.extend(tran_sub(info_weapon))
    
    dict_stat = {'피해 증가':[],
        '추가 피해':[],
        '공격력 증가 (%)':[],
        '공격력 증가 (+)':[],
        '무기공격력 증가 (%)':[],
        '무기공격력 증가 (+)':[],
        '스탯 증가 (%)':[],
        '스탯 증가 (+)':[],
        '치명타 적중률 증가':[],
        '치명타 피해 증가':[],
        '치명타 시 피해 증가':[],
        '백어택':[],
        '헤드어택':[],
        '비방향성':[],
        '캐스팅':[],
        '차징':[],
        '쿨타임 감소':[],
        '진화형 피해':[],
        '물리 방어력':[],
        '마법 방어력':[],
        '최대 생명력':[],
        }

    transcendence_stage = list()
    sum_transcendence = 0

    for u in transcendence_all:
        if '무기공격력' in u:
            dict_stat['무기공격력 증가 (+)'].append(int(u.split('+')[1]))
        if ('힘' in u) or ('지능' in u) or ('민첩' in u) :
            dict_stat['스탯 증가 (+)'].append(int(u.split('+')[1]))
        if '단계' in u:
            sum_transcendence += int(u.split(' ')[-1])
            transcendence_stage.append(u)

    transcendence_stage.append(f'총 {sum_transcendence}')
    
    #투구
    dict_stat['최대 생명력'].append(int(sum_transcendence*80))
    dict_stat['무기공격력 증가 (+)'].append(int(sum_transcendence*14))
    dict_stat['스탯 증가 (+)'].append(int(sum_transcendence*55))
    dict_stat['공격력 증가 (+)'].append(int(sum_transcendence*6))
    
    #어꺠
    dict_stat['무기공격력 증가 (+)'].append(3600)
    dict_stat['마법 방어력'].append(1800)

    #상의
    dict_stat['무기공격력 증가 (+)'].append(7200)
    dict_stat['최대 생명력'].append(1400)

    #하의
    dict_stat['피해 증가'].append(1.015)

    #장갑
    dict_stat['스탯 증가 (+)'].append(12600)
    dict_stat['물리 방어력'].append(1800)

    #무기
    dict_stat['공격력 증가 (+)'].append(3525)

    return dict_stat, transcendence_stage


def accessory(user_info):
    info = user_info.equip_accessory()
    acc_list = list()
    for k in range(0,5):
        acc_0 = info[k]['Element_007']['value']['Element_001']
        acc_1 = info[k]['Element_005']['value']['Element_001'].lower().replace("</img>",'split/').replace("<br",'split/').split('split/')
        acc_1 = acc_1[1::2]    
        acc_list.extend(acc_1)
    # acc_list_head = [x for x in acc_list if '%' in x]
    acc_list = [x for x in acc_list if ('파티원' not in x) and ('아군' not in x) and ('상태이상' not in x) and ('전투' not in x)]

    dict_stat = {'피해 증가':[],
        '추가 피해':[],
        '공격력 증가 (%)':[],
        '공격력 증가 (+)':[],
        '무기공격력 증가 (%)':[],
        '무기공격력 증가 (+)':[],
        '스탯 증가 (%)':[],
        '스탯 증가 (+)':[],
        '치명타 적중률 증가':[],
        '치명타 피해 증가':[],
        '치명타 시 피해 증가':[],
        '백어택':[],
        '헤드어택':[],
        '비방향성':[],
        '캐스팅':[],
        '차징':[],
        '쿨타임 감소':[],
        '진화형 피해':[],
        '물리 방어력':[],
        '마법 방어력':[],
        '최대 생명력':[],
        }
    
    for e in acc_list:
        if ('무기공격력' in e) and ('%' in e):
            dict_stat['무기공격력 증가 (%)'].append(float(e.replace("%",'').split('+')[1]))
        if ('무기공격력' in e) and ('%' not in e) :
            dict_stat['무기공격력 증가 (+)'].append(int(e.split('+')[1]))
        if ('공격력' in e) and ('무기' not in e) and ('%' in e):
            dict_stat['공격력 증가 (%)'].append(float(e.replace("%",'').split('+')[1]))
        if ('공격력' in e) and ('무기' not in e) and ('%' not in e):
            dict_stat['공격력 증가 (+)'].append(int(e.split('+')[1]))
        if '추가피해' in e :
            dict_stat['추가 피해'].append(float(e.replace("%",'').split('+')[1]))
        if '적에게주는피해' in e :
            dict_stat['피해 증가'].append(float(e.replace("%",'').split('+')[1]))
        if '치명타적중률' in e :
            dict_stat['치명타 적중률 증가'].append(float(e.replace("%", '').split('+')[1]))
        if '치명타피해' in e :
            dict_stat['치명타 피해 증가'].append(float(e.replace("%", '').split('+')[1]))
        if '최대생명력' in e :
            dict_stat['최대 생명력'].append(int(e.split('+')[1]))

    return dict_stat

def stat(user_info):
    armor = user_info.equip_armor()
    weapon = user_info.equip_weapon()

    stat_list = list()
    stat_weapon = weapon['Element_006']['value']['Element_001'].split('<BR>')
    stat_list.extend(stat_weapon)
    for k in range(0, 5):
        stat_armor = armor[k]['Element_006']['value']['Element_001'].split('<BR>')
        stat_list.extend(stat_armor)
    
    dict_stat = {'피해 증가':[],
        '추가 피해':[],
        '공격력 증가 (%)':[],
        '공격력 증가 (+)':[],
        '무기공격력 증가 (%)':[],
        '무기공격력 증가 (+)':[],
        '스탯 증가 (%)':[],
        '스탯 증가 (+)':[],
        '치명타 적중률 증가':[],
        '치명타 피해 증가':[],
        '치명타 시 피해 증가':[],
        '백어택':[],
        '헤드어택':[],
        '비방향성':[],
        '캐스팅':[],
        '차징':[],
        '쿨타임 감소':[],
        '진화형 피해':[],
        '물리 방어력':[],
        '마법 방어력':[],
        '최대 생명력':[],
        }

    for u in stat_list:
        if '무기공격력' in u:
            dict_stat['무기공격력 증가 (+)'].append(int(u.split('+')[1]))
        if ('힘' in u) or ('지능' in u) or ('민첩' in u) :
            dict_stat['스탯 증가 (+)'].append(int(u.split('+')[1]))
        if '물리방어력' in u:
            dict_stat['물리 방어력'].append(int(u.split('+')[1]))
        if '마법방어력' in u:
            dict_stat['마법 방어력'].append(int(u.split('+')[1]))

    return dict_stat

def armlet(user_info):
    armlet_json = user_info.equip_armlet()
    jump_point = armlet_json['Element_007']['value']['Element_001']
    armlet_option = armlet_json['Element_004']['value']['Element_001'].lower().replace("<fontcolor='#99ff99'>",'').replace("<fontcolor='#ff9999'>",'').replace("</font>",'').replace("</img>",'[]').replace("<br>",'[]').split('[]')
    armlet_option = [x for x in armlet_option if '<' not in x ]

    return jump_point, armlet_option