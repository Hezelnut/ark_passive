from player_load import get_name, arkpassive
from engrave import engraving
from spec import equipment
from armlet import armlet_option
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
    armlet_info = armlet_option(response)
    equipment_info = equipment(response)

    form = {'특성':{'치명':0,'신속':0,'특화':0},
            '피해 증가':[],
            '추가 피해':[],
            '공격력 증가 (%)':[],
            '공격력 증가 (+)':[],
            '기본 공격력 증가 (%)':[],
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
            '체력':[],
            '최대 생명력':[],
            '생명력 활성':[],
            '공격속도':[],
            '이동속도':[]
            }
    
    form_equipment, equipment_list = equipment_info.equip_all()

    form_engraving, engrave_list = engraving(response)
    
    form_armlet, armlet_list = armlet_info.armlet_options()
    
    form_list = [form_equipment, form_engraving, form_armlet]
   
    for f in form_list:
        for key in form.keys():
            if not(key == '특성'):
                form[key].extend(f[key])
            elif key == '특성':
                form['특성']['치명'] += f['특성']['치명']
                form['특성']['신속'] += f['특성']['신속']
                form['특성']['특화'] += f['특성']['특화']

            
    spec_dict = {
        'accessory':equipment_list['accessory'],
        'elixer':equipment_list['elixer'],
        'engrave':engrave_list,
        'evolve':ark_passive.evolve_tier_all(),
        'enlight':ark_passive.enlight(),
        'jump':ark_passive.jump(),
        'armlet':armlet_list
    }

    return form, spec_dict


if __name__ == '__main__':
    form, spec_dict = stat_all()
    
    print(form)
    print('-'*5)
    print(spec_dict)