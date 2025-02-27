import requests
import json
import re
import pandas

class get_name:
    def __init__(self,name):
        self.nickname = name
        self.headers = {
            'accept': 'application/json',
            'authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAwODc4NTYifQ.Kz1Q31XCxpow-7vQUhjx8sejfVuQHi0T7BLfVoIXd4LErYMYJZ82oc9PX3Ls19rVxgvnNrwnpu2a2Ctg3vX8qO0214NgAh1Ab8M2hPPEksai7LY2enjhBGu7nvs8Ic9eq43p4DiGlpHQ68zZBbTo1WFbumayIrWkVAD-m7AHbkuguM0pMuXv8qL7ar6ZR-vVUsOetOuAannv6OpFhss3db1n4PuJM6S1TPyo2-Uo6T2FTp5Ue9C8TmIFnj97ZESorEU5KttbZ9qkL8yYnsK1A6glbYQksGMkCS0zQCp87BRQPccKAw41WlybHWcdjU3Zz3iDtMmQ5zv0GI_s0tzEmQ',
            'Content-Type': 'application/json',
            }
    
    @classmethod
    def help(clr):
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

form = {'피해 증가':[],
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
        '생명력 활성':[]
        }


"""
        return print(info_help)
    
    def get_response(self):
        url_1 = f'https://developer-lostark.game.onstove.com/armories/characters/{self.nickname}/equipment'
        response_1 = requests.get(url_1,headers=self.headers)

        weapon = json.loads(response_1.json()[0]['Tooltip'].replace('''\r\n''','').replace(' ',''))
        armor = [json.loads(response_1.json()[i]['Tooltip'].replace('''\r\n''','').replace(' ','')) for i in range(1,6)]
        accessory = [json.loads(response_1.json()[i]['Tooltip'].replace('''\r\n''','').replace(' ','')) for i in range(6,11)]
        stone = json.loads(response_1.json()[11]['Tooltip'].replace('''\r\n''','').replace(' ',''))
        armlet = json.loads(response_1.json()[12]['Tooltip'].replace('''\r\n''','').replace(' ',''))


        url_2 = f'https://developer-lostark.game.onstove.com/armories/characters/{self.nickname}/engravings'
        response_2 = requests.get(url_2,headers=self.headers)

        url_3 = f'https://developer-lostark.game.onstove.com/armories/characters/{self.nickname}/arkpassive'
        response_3 = requests.get(url_3,headers=self.headers)

        url_4 = f'https://developer-lostark.game.onstove.com/armories/characters/{self.nickname}/combat-skills'
        response_4 = requests.get(url_4,headers=self.headers)

        url_5 = f'https://developer-lostark.game.onstove.com/armories/characters/{self.nickname}/gems'
        response_5 = requests.get(url_5,headers=self.headers)

        url_6 = f'https://developer-lostark.game.onstove.com/armories/characters/{self.nickname}/profiles'
        response_6 = requests.get(url_6,headers=self.headers)

        response_all = {
            'weapon':weapon,
            'armor':armor,
            'accessory':accessory,
            'stone':stone,
            'armlet':armlet,
            'engravings':response_2.json(),
            'arkpassive':response_3.json(),
            'skill':response_4.json(),
            'gems':response_5.json(),
            'profile':response_6.json()
        }

        return response_all


class arkpassive:
    def __init__(self,response):
        self.response = response['arkpassive']
    
    def evolve(self):
        x_0 = [x['Description'].replace("<FONT color='#83E9FF'>",'').replace("<FONT color='#F1D594'>",'').replace("<FONT color='#C2EA55'>",'').replace("</FONT>",'') for x in self.response['Effects'] if x['Name']=='진화']
        x_1 = [x1.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x1 in x_0 if '1티어' in x1]
        x_2 = [x2.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x2 in x_0 if '2티어' in x2]
        x_3 = [x3.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x3 in x_0 if '3티어' in x3]
        x_4 = [x4.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x4 in x_0 if '4티어' in x4]

        tier1 = {'치명':0,'신속':0,'특화':0}
        for m,n in enumerate(x_1):
            if '치명' == n[0]:
                tier1['치명'] = int(n[1])
            if '신속' == n[0]:
                tier1['신속'] = int(n[1])
            if '특화' == n[0]:
                tier1['특화'] = int(n[1])

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
            if '뭉툭한 가시' == n[0]:
                tier4['t4_1'] = int(n[1])
            if '음속 돌파' == n[0]:
                tier4['t4_2'] = int(n[1])
            if '인파이팅' == n[0]:
                tier4['t4_3'] = int(n[1])
            if '입식 타격가' == n[0]:
                tier4['t4_4'] = int(n[1])
            if '마나 용광로' == n[0]:
                tier4['t4_5'] = int(n[1])

        evolve_response = {
            'tier1':tier1,
            'tier2':tier2,
            'tier3':tier3,
            'tier4':tier4,
        }

        return evolve_response
    
    
    def enlight(self):
        y_0 = [y['Description'].replace("<FONT color='#83E9FF'>",'').replace("<FONT color='#F1D594'>",'').replace("<FONT color='#C2EA55'>",'').replace("</FONT>",'') for y in self.response['Effects'] if y['Name']=='깨달음']
        y_1 = [y1.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for y1 in y_0 if '1티어' in y1]
        y_2 = [y2.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for y2 in y_0 if '2티어' in y2]
        y_3 = [y3.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for y3 in y_0 if '3티어' in y3]
        y_4 = [y4.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for y4 in y_0 if '4티어' in y4]
        return y_1,y_2,y_3,y_4
    
    def jump(self):
        z_0 = [z['Description'].replace("<FONT color='#83E9FF'>",'').replace("<FONT color='#F1D594'>",'').replace("<FONT color='#C2EA55'>",'').replace("</FONT>",'') for z in self.response['Effects'] if z['Name']=='도약']
        z_1 = [z1.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for z1 in z_0 if '1티어' in z1]
        z_2 = [z2.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for z2 in z_0 if '2티어' in z2]
        return z_1, z_2

    
    def evolve_Tier_1(self):
        t1 = self.evolve()['tier1']

        stat_base = {'치명': 69, '신속': 72, '특화': 70}
        stat_base['치명'] = stat_base['치명'] + t1['치명']*50
        stat_base['신속'] = stat_base['신속'] + t1['신속']*50
        stat_base['특화'] = stat_base['특화'] + t1['특화']*50
        return stat_base

    def evolve_Tier_2(self):
        t2 = self.evolve()['tier2']

        t2_1 = t2['t2_1']
        t2_2 = t2['t2_2']
        t2_3 = t2['t2_3']
        t2_4 = t2['t2_4']
        t2_5 = t2['t2_5']

        if t2_1+t2_2+t2_3+t2_4+t2_5>3:
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

    def evolve_Tier_3(self):
        t3 = self.evolve()['tier3']

        t3_1 = t3['t3_1']
        t3_2 = t3['t3_2']
        t3_3 = t3['t3_3']
        t3_4 = t3['t3_4']
        t3_5 = t3['t3_5']

        if t3_1+t3_2+t3_3+t3_4+t3_5>2:
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

    def evolve_Tier_4(self):
        t4 = self.evolve()['tier4']

        t4_1 = t4['t4_1']
        t4_2 = t4['t4_2']
        t4_3 = t4['t4_3']
        t4_4 = t4['t4_4']
        t4_5 = t4['t4_5']

        if t4_1+t4_2+t4_3+t4_4+t4_5>2:
            print('Error')
        else:
            tier4_stat = {
            '진화형 피해':[t4_3*9+t4_4*10.5],
            '뭉툭한 가시':[False if t4_1==0 else True],
            '마나 용광로':[False if t4_5==0 else True],
            '음속 돌파':[False if t4_2==0 else True]
            }

        return tier4_stat

    def evolve_tier_all(self):
        return self.evolve_Tier_1(), self.evolve_Tier_2(), self.evolve_Tier_3(), self.evolve_Tier_4()


    def enlight(self):
        x_0 = [x['Description'].replace("<FONT color='#83E9FF'>",'').replace("<FONT color='#F1D594'>",'').replace("<FONT color='#C2EA55'>",'').replace("</FONT>",'') for x in self.response['Effects'] if x['Name']=='깨달음']
        x_1 = [x1.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x1 in x_0 if '1티어' in x1]
        x_2 = [x2.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x2 in x_0 if '2티어' in x2]
        x_3 = [x3.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x3 in x_0 if '3티어' in x3]
        x_4 = [x4.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x4 in x_0 if '4티어' in x4]
        
        enlight_response = {
            'tier1':x_1,
            'tier2':x_2,
            'tier3':x_3,
            'tier4':x_4,
        }
        
        return enlight_response
    
    def jump(self):
        x_0 = [x['Description'].replace("<FONT color='#83E9FF'>",'').replace("<FONT color='#F1D594'>",'').replace("<FONT color='#C2EA55'>",'').replace("</FONT>",'') for x in self.response['Effects'] if x['Name']=='도약']
        x_1 = [x1.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x1 in x_0 if '1티어' in x1]
        x_2 = [x2.replace('티어 ','//').replace(' Lv.','//').split('//')[1:3] for x2 in x_0 if '2티어' in x2]
        
        jump_response = {
            'tier1':x_1,
            'tier2':x_2
        }
        
        return jump_response