import random
import os
import numpy as np
import pandas as pd
import requests
import json
import re

headers = {
            'accept': 'application/json',
            'authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAwODc4NTYifQ.Kz1Q31XCxpow-7vQUhjx8sejfVuQHi0T7BLfVoIXd4LErYMYJZ82oc9PX3Ls19rVxgvnNrwnpu2a2Ctg3vX8qO0214NgAh1Ab8M2hPPEksai7LY2enjhBGu7nvs8Ic9eq43p4DiGlpHQ68zZBbTo1WFbumayIrWkVAD-m7AHbkuguM0pMuXv8qL7ar6ZR-vVUsOetOuAannv6OpFhss3db1n4PuJM6S1TPyo2-Uo6T2FTp5Ue9C8TmIFnj97ZESorEU5KttbZ9qkL8yYnsK1A6glbYQksGMkCS0zQCp87BRQPccKAw41WlybHWcdjU3Zz3iDtMmQ5zv0GI_s0tzEmQ',
            'Content-Type': 'application/json',
            }


#치,특,신 기본스탯
stat_basic = (69,72,70)


def equipment(name=''):
    url = f'https://developer-lostark.game.onstove.com/armories/characters/{name}/equipment'
    response = requests.get(url,headers=headers)
    equip_list = list()
    for i in range(13):
        e = response.json()[i]['Tooltip'].replace('''\r\n''','').replace(' ','')
        equip_list.append(e)
    return equip_list

def armories(name=''):
    url = f'https://developer-lostark.game.onstove.com/armories/characters/{name}/engravings'
    response = requests.get(url,headers=headers)
    return response.json()

def ark(name=''):
    url = f'https://developer-lostark.game.onstove.com/armories/characters/{name}/arkpassive'
    response = requests.get(url,headers=headers)
    return response.json()

# Element_010 : 엘릭서
# Element_009 : 초월
# Element_007 : 품질 추가효과
# Element_006 : 힘 체력 등 기본효과
# Element_005 : 상급재련 n단계

# equipment(name)[0~12]
# 0     무기
# 1~5   방어구
# 6~10  악세사리
# 11    어빌리티 스톤
# 12    팔찌

class all_equip:
    def __init__(self,name):
        self.nickname = name
    @classmethod
    def call_help(clr):
        info_help = """
### 무기 : equip_weapon()
# Element_009 : 초월
# Element_007 : 품질 추가효과
# Element_006 : 무기공격력
# Element_005 : 상급재련n단계

### 방어구 : equip_armor()
### 리스트 형태 : equip_armor()[0~4]
# Element_010 : 엘릭서
# Element_009 : 초월
# Element_007 : 품질 추가효과
# Element_006 : 힘 체력 등 기본효과
# Element_005 : 상급재련 n단계

### 악세사리 : equip_accessory()
### 리스트 형태 : equip_accessory()[0~4]
# Element_007 : 깨달음
# Element_005 : 연마 효과
# Element_004 : 힘 체력 등 기본효과

### 팔찌 : equip_armlet()
# Element_004 : 팔찌 효과
"""
        return print(info_help)

    def equip_weapon(self):
        return json.loads(equipment(self.nickname)[0])

    def equip_armor(self):
        armory = list()
        for i in range(1,6):
            armor = json.loads(equipment(self.nickname)[i])
            armory.append(armor)
        return armory

    def equip_accessory(self):
        accessory_list = list()
        for i in range(6,11):
            accessory = json.loads(equipment(self.nickname)[i])
            accessory_list.append(accessory)
        return accessory_list

    def equip_stone(self):
        return json.loads(equipment(self.nickname)[11])

    def equip_armlet(self):
        return json.loads(equipment(self.nickname)[12])

    def equip_engraving(self):
        tuple_list = list()
        for eng in armories(self.nickname)['ArkPassiveEffects']:
            eng_tuple = (eng['Name'], eng['Level'],eng['AbilityStoneLevel'])
            tuple_list.append(eng_tuple)
        return tuple_list
    
    def equip_arkpassive(self):
        x_0 = [x['Description'].replace("<FONT color='#83E9FF'>",'').replace("<FONT color='#F1D594'>",'').replace("<FONT color='#C2EA55'>",'').replace("</FONT>",'') for x in ark(self.nickname)['Effects'] if x['Name']=='진화']
        x_1 = [x1.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x1 in x_0 if '1티어' in x1]
        x_2 = [x2.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x2 in x_0 if '2티어' in x2]
        x_3 = [x3.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x3 in x_0 if '3티어' in x3]
        x_4 = [x4.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x4 in x_0 if '4티어' in x4]

        tier1 = {'crit':0,'vel':0,'abl':0}
        for m,n in enumerate(x_1):
            if '치명' == n[0]:
                tier1['crit'] = int(n[1])
            if '신속' == n[0]:
                tier1['vel'] = int(n[1])
            if '특화' == n[0]:
                tier1['abl'] = int(n[1])
        tier1

        tier2 = {'t2_1':0,'t2_2':0,'t2_3':0,'t2_4':0,'t2_5':0}
        for m,n in enumerate(x_2):
            if '끝없는 마나' == n[0]:
                tier2['t2_1'] = int(n[1])
            if '금단의 주문' == n[0]:
                tier2['t2_2'] = int(n[1])
            if '예리한 감각' == n[0]:
                tier2['t2_3'] = int(n[1])
            if '한계 돌파' == n[0]:
                tier2['t2_4'] = int(n[1])
            if '최적화 훈련' == n[0]:
                tier2['t2_5'] = int(n[1])
        tier2

        tier3 = {'t3_1':0,'t3_2':0,'t3_3':0,'t3_4':0,'t3_5':0}
        for m,n in enumerate(x_3):
            if '무한한 마력' == n[0]:
                tier3['t3_1'] = int(n[1])
            if '혼신의 강타' == n[0]:
                tier3['t3_2'] = int(n[1])
            if '일격' == n[0]:
                tier3['t3_3'] = int(n[1])
            if '파괴 전차' == n[0]:
                tier3['t3_4'] = int(n[1])
            if '타이밍 지배' == n[0]:
                tier3['t3_5'] = int(n[1])
        
        tier4 = {'t4_1':0,'t4_2':0,'t4_3':0,'t4_4':0,'t4_5':0}
        for m,n in enumerate(x_4):
            if '뭉특한 가시' == n[0]:
                tier4['t4_1'] = int(n[1])
            if '음속 돌파' == n[0]:
                tier4['t4_2'] = int(n[1])
            if '인파이팅' == n[0]:
                tier4['t4_3'] = int(n[1])
            if '입식 타격가' == n[0]:
                tier4['t4_4'] = int(n[1])
            if '마나 용광로' == n[0]:
                tier4['t4_5'] = int(n[1])
        tier3
        return tier1, tier2, tier3, tier4
    
def Tier_1(crit=0,vel=0,abl=0):
    #아크패시브 몇 포인트를 줄 것인지
    if crit+vel+abl>40:
        print('Error')
    else:pass
    crit=crit*50
    vel=vel*50
    abl=abl*50

    return crit, vel, abl

def engraving(user_info):
    engrave_list = user_info.equip_engraving()
    a = engrave_list[0]
    b = engrave_list[1]
    c = engrave_list[2]
    d = engrave_list[3]
    e = engrave_list[4]
    # a,b,c,d,e는 튜플형태로 할 것.
    # 유물 : 0 / 유물 5 : 1 / 유물10 : 2 / 유물15 : 3 / 유물20 : 4
    # 돌이 무슨 돌인가? 6 7 9 10 -> 1 2 3 4  
    # ex) 원한 유각 10장 돌맹이9 = (원한,2,3)
    engraving_dict = {
        'Form' : {
            '피해 증가':[],
            '공격력 증가 (%)':[],
            '공격력 증가 (+)':[],
            '무기공격력 증가 (%)':[],
            '무기공격력 증가 (+)':[],
            '치명타 적중률 증가':[],
            '치명타 피해 증가':[],
            '치명타 시 피해 증가':[],
            '백어택':[],
            '헤드어택':[],
            '캐스팅':[],
            '차징':[],
            '쿨타임 감소':[],
            '진화형 피해':[]
            },
         
        '원한' : {
            '피해 증가':[1.18,1.1875,1.195,1.2025,1.21],
            '어빌리티 스톤':[0.03,0.0375,0.0525,0.06]
            },
        
        '아드레날린' : {
            '공격력 증가 (%)':[1.054,1.054,1.054,1.054,1.054],
            '치명타 적중률 증가':[14,15.5,17,18.5,20],
            '어빌리티 스톤':[0.0288,0.036,0.05,0.057]
            },
        '정밀 단도' : {
            '치명타 적중률 증가':[18,18.75,19.5,20.25,21],
            '치명타 피해 증가':[-6,-6,-6,-6,-6],
            '어빌리티 스톤':[3,3.75,5.25,6]
            },        
            
        '저주받은 인형' : {
            '피해 증가':[1.14,1.1475,1.155,1.1625,1.17],
            '어빌리티 스톤':[0.03,0.0375,0.0525,0.06]
            },

        '안정된 상태' : {
            '피해 증가':[1.14,1.1475,1.155,1.1625,1.17],
            '어빌리티 스톤':[0.03,0.0375,0.0525,0.06]
            },

        '돌격대장' : {
            '피해 증가':[1.16,1.168,1.176,1.184,1.192],
            '어빌리티 스톤':[0.03,0.0376,0.0528,0.06]
            },

        '질량 증가' : {
            '피해 증가':[1.16,1.1675,1.175,1.1825,1.19],
            '어빌리티 스톤':[0.03,0.0375,0.0525,0.06]
            },

        '예리한 둔기' : {
            '피해 증가':[0.98,0.98,0.98,0.98,0.98],
            '치명타 피해 증가':[44,46,48,50,52],
            '어빌리티 스톤':[7.5,9.4,13.2,15]
            },

        '결투의 대가' : {
            '피해 증가':[1.048,1.055,1.062,1.069,1.076],
            '헤드어택':[1.25/1.1,1.25/1.1,1.25/1.1,1.25/1.1,1.25/1.1],
            '어빌리티 스톤':[0.027,0.034,0.047,0.054]
            },

        '기습의 대가' : {
            '피해 증가':[1.048,1.055,1.062,1.069,1.076],
            '백어택':[1.20/1.05,1.20/1.05,1.20/1.05,1.20/1.05,1.20/1.05],
            '어빌리티 스톤':[0.027,0.034,0.047,0.054]
            },

        '타격의 대가' : {
            '피해 증가':[1.14,1.1475,1.155,1.1625,1.17],
            '어빌리티 스톤':[0.03,0.0375,0.0525,0.06]
            },
        
        
        '바리케이드' : {
            '피해 증가':[1.14,1.1475,1.155,1.1625,1.17],
            '어빌리티 스톤':[0.03,0.0375,0.0525,0.06]
            },
        
        '달인의 저력' : {
            '피해 증가':[1.14,1.1475,1.155,1.1625,1.17],
            '어빌리티 스톤':[0.03,0.0375,0.0525,0.06]
            },
        
        '슈퍼 차지' : {
            '차징':[1.18,1.1875,1.195,1.2025,1.21],
            '어빌리티 스톤':[0.03,0.0375,0.0525,0.06]
            },
        
        '속전속결' : {
            '캐스팅':[1.18,1.1875,1.195,1.2025,1.21],
            '어빌리티 스톤':[0.03,0.0375,0.0525,0.06]
            },

        '마나 효율 증가' : {
            '피해 증가':[1.13,1.1375,1.145,1.1525,1.16],
            '어빌리티 스톤':[0.03,0.0375,0.0525,0.06]
            }               
        }
    # 원한 -> (원한,2,2) 형태로 넣을 것이라고 가정
    def engrave_def(x):
        if x[-1] == None:
            pass
        else:
            key_list = list(engraving_dict[x[0]].keys())
            stone_stat = engraving_dict[x[0]]['어빌리티 스톤'][x[2]-1]
            engraving_dict[x[0]][key_list[-2]] = [v+stone_stat for v in engraving_dict[x[0]][key_list[-2]]]
        for m,n in list(engraving_dict[x[0]].items())[:-1]:
            engraving_dict['Form'][m].append(n[x[1]])

    engrave_def(a)
    engrave_def(b)
    engrave_def(c)
    engrave_def(d)
    engrave_def(e)

    return engraving_dict['Form']
stat = {
    '피해 증가':[],
    '공격력 증가 (%)':[],
    '공격력 증가 (+)':[],
    '무기공격력 증가 (%)':[],
    '무기공격력 증가 (+)':[],
    '치명타 적중률 증가':[],
    '치명타 피해 증가':[],
    '치명타 시 피해 증가':[],
    '백어택':[],
    '헤드어택':[],
    '캐스팅':[],
    '차징':[],
    '쿨타임 감소':[],
    '진화형 피해':[]
    }
evol_stat = {
    '진화형 피해':[],
    '쿨타임 감소_마나':[],
    '쿨타임 감소_지배':[],
    '치명타 피해 증가':[],
    '치명타 적중률 증가':[],
    '뭉특한 가시':[]
}
def Tier_2(t2):
    t2_1 = t2[0]
    t2_2 = t2[1]
    t2_3 = t2[2]
    t2_4 = t2[3]
    t2_5 = t2[4]
    if sum(t2)>3:
        print('Error')
    elif t2_1>2 or t2_2>2 or t2_3>2 or t2_5>2:
        print('Error')
    else:
        # t2_1 : 끝없는 마나
        # t2_2 : 금단의 주문
        # t2_3 : 예리한 감각
        # t2_4 : 한계 돌파
        # t2_5 : 최적화 훈련
        tier2_stat = {
            '진화형 피해':[t2_2*10+t2_3*5+t2_4*10+t2_5*5],
            '쿨타임 감소_마나':[t2_1*7],
            '쿨타임 감소_지배':[t2_5*4],
            '백헤드 스킬 치명타 피해 증가':[],
            '치명타 적중률 증가':[t2_3*4]
        }
    return tier2_stat
def Tier_3(t3):
    t3_1 = t3[0]
    t3_2 = t3[1]
    t3_3 = t3[2]
    t3_4 = t3[3]
    t3_5 = t3[4]
    if sum(t3)>2:
        print('Error')
    else:
        # t3_1 : 무한한 마력
        # t3_2 : 혼신의 강타
        # t3_3 : 일격
        # t3_4 : 파괴 전차
        # t3_5 : 타이밍 지배
        # t3_bh : 방향성 여부
        tier3_stat = {
            '진화형 피해':[t3_1*8,t3_2*2,t3_4*12,t3_5*8],
            '쿨타임 감소_마나':[t3_1*7],
            '쿨타임 감소_지배':[t3_5*5],
            '백헤드 스킬 치명타 피해 증가':[t3_3*16],
            '치명타 적중률 증가':[t3_2*12,t3_3*10]
        }
    return tier3_stat
def Tier_4(t4):
    t4_1 = t4[0]
    t4_2 = t4[1]
    t4_3 = t4[2]
    t4_4 = t4[3]
    t4_5 = t4[4]
    if sum(t4)>2:
        print('Error')
    else:
        tier4_stat = {
        '진화형 피해':[t4_3*9+t4_4*10.5],
        '뭉특한 가시':[False if t4_1==0 else True],
        '마나 용광로':[False if t4_5==0 else True],
        '음속 돌파':[False if t4_2==0 else True]
        }

    return tier4_stat
player = '그늘을벼려낸칼날'
# player = 'user_name'

user_info = all_equip(player)
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

# 엘릭서 두 줄을 튜플의 형태로 출력함
# 추후 전처리 필요함


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

# 성공
# transcendence(user_info)
# [('민첩+5880', '7단계 21'),
#  ('민첩+5880', '7단계 21'),
#  ('민첩+5880', '7단계 21'),
#  ('민첩+5880', '7단계 21'),
#  ('민첩+5880', '7단계 21'),
#  ('무기공격력+2940', '7단계 21')]

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

# 성공
# accessory(user_info)
# >> ['추가피해+1.60%', '무기공격력+1.80%', '공격력+0.95%', '치명타적중률+0.95%', '치명타피해+2.40%']
# 위와 같은 방식으로 출력함.



print(f"""
elixer : {elixer(user_info)}, \n
accessory : {accessory(user_info)}, \n
transcend : {transcendence(user_info)}, \n
engraving : {engraving(user_info)}
""")

