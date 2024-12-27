from player_load import equip, process
from engrave import engraving
from spec import transcendence,elixer,accessory, stat, armlet
from arkpassive import load_evolve, load_enlight, load_jump

user_info = equip(input('플레이어 이름 : '))

# API 호출을 딱 세번만 하도록 분리해서 저장.
# _, _, _ = user_info.equipment() 
# 각각 장비, 각인, 아크패시브
equ, eng, ark = user_info.equipment()

equip_process = process(equ)
engrave_process = process(eng)
ark_process = process(ark)

transcendence(equip_process) # 초월 정보
accessory(equip_process) # 악세사리의 특옵 정보
elixer(equip_process) # 엘릭서정보
engraving(engrave_process) # 각인서 효과를 종합한 정보

load_evolve(ark_process).Tier_all() # 진화탭 모든 티어 정보
# Tier_1()
# Tier_2()
# Tier_3()
# TIer_4() 가능

load_enlight(ark_process).ark_enlight() # 깨달음 탭

load_jump(ark_process).ark_jump() # 도약 탭


def stat_all(user_info):
    arm, eng, ark = user_info.equipment()
    equip_process = process(arm)
    engrave_process = process(eng)
    ark_process = process(ark)

    form = {'피해 증가':[],
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
        '생명력 활성':[]
        }
    
    sum_stat = stat(equip_process)
    sum_acc = accessory(equip_process)
    sum_eli = elixer(equip_process)
    sum_tra, _ = transcendence(equip_process)
    sum_eng = engraving(engrave_process)
    sum_arm = armlet(equip_process)
    load_enlight(ark_process).ark_enlight()
    load_evolve(ark_process).Tier_all()
    load_jump(ark_process).ark_jump()
    list_sum = [sum_tra,sum_acc,sum_arm,sum_eli,sum_eng,sum_stat]
    for l in list_sum:
        for k in [form.keys()]:
            form[k].extend(l[k])

    return list_sum

print(stat_all(user_info))