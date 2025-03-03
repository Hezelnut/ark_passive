from player_load import get_name, arkpassive
from engrave import engraving
from spec import transcendence,elixer,accessory, stat, armlet
import logging

"""
user_info = get_name(input('플레이어 이름 : '))
response = user_info.get_response()

transcendence(response) # 초월 정보
accessory(response) # 악세사리의 특옵 정보
elixer(response) # 엘릭서정보
engraving(response) # 각인서 효과를 종합한 정보

ark_passive = arkpassive(response)

ark_passive.evolve_tier_all()# 진화탭 모든 티어 정보

ark_passive.enlight() # 깨달음 탭

ark_passive.jump() # 도약 탭
"""

def stat_all(name='절정하는창술누나'):
    user_name = get_name(name)
    response = user_name.get_response()
    ark_passive = arkpassive(response)

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
    
    sum_stat = stat(response)
    sum_acc, acc_list = accessory(response)
    sum_eli, elixer_name = elixer(response)
    sum_tra, transcendence_stage = transcendence(response)
    sum_eng, engrave_list = engraving(response)
    sum_arm = armlet(response)
    list_sum = [sum_eli,sum_eng,sum_stat,sum_acc,sum_tra] #,sum_arm은 제외
    for l in list_sum:
        for k in list(form.keys()):
            form[k].extend(l[k])
            
    spec_dict = {
        'accessory':acc_list,
        'elixer':elixer_name,
        'engrave':engrave_list,
        'armlet':sum_arm,
        'evolve':ark_passive.evolve_tier_all(),
        'enlight':ark_passive.enlight(),
        'jump':ark_passive.jump()
    }

    return form, spec_dict


if __name__ == '__main__':
    form, spec_all = stat_all()
    
    print(form)
    print('-'*5)
    print(spec_all)
    
    print(spec_all['evolve'][1])