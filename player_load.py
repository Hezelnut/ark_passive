import requests
import json

class all_equip:
    def __init__(self,name):
        self.nickname = name
        self.headers = {
            'accept': 'application/json',
            'authorization': 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAwODc4NTYifQ.Kz1Q31XCxpow-7vQUhjx8sejfVuQHi0T7BLfVoIXd4LErYMYJZ82oc9PX3Ls19rVxgvnNrwnpu2a2Ctg3vX8qO0214NgAh1Ab8M2hPPEksai7LY2enjhBGu7nvs8Ic9eq43p4DiGlpHQ68zZBbTo1WFbumayIrWkVAD-m7AHbkuguM0pMuXv8qL7ar6ZR-vVUsOetOuAannv6OpFhss3db1n4PuJM6S1TPyo2-Uo6T2FTp5Ue9C8TmIFnj97ZESorEU5KttbZ9qkL8yYnsK1A6glbYQksGMkCS0zQCp87BRQPccKAw41WlybHWcdjU3Zz3iDtMmQ5zv0GI_s0tzEmQ',
            'Content-Type': 'application/json',
            }
    
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
    
    def equipment(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.nickname}/equipment'
        response = requests.get(url,headers=self.headers)
        equip_list = list()
        for i in range(13):
            e = response.json()[i]['Tooltip'].replace('''\r\n''','').replace(' ','')
            equip_list.append(e)
        return equip_list

    def armories(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.nickname}/engravings'
        response = requests.get(url,headers=self.headers)
        return response.json()

    def ark(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.nickname}/arkpassive'
        response = requests.get(url,headers=self.headers)
        return response.json()


    def equip_weapon(self):
        return json.loads(self.equipment()[0])

    def equip_armor(self):
        armory = list()
        for i in range(1,6):
            armor = json.loads(self.equipment()[i])
            armory.append(armor)
        return armory

    def equip_accessory(self):
        accessory_list = list()
        for i in range(6,11):
            accessory = json.loads(self.equipment()[i])
            accessory_list.append(accessory)
        return accessory_list

    def equip_stone(self):
        return json.loads(self.equipment()[11])

    def equip_armlet(self):
        return json.loads(self.equipment()[12])

    def equip_engraving(self):
        tuple_list = list()
        for eng in self.armories()['ArkPassiveEffects']:
            eng_tuple = (eng['Name'], eng['Level'],eng['AbilityStoneLevel'])
            tuple_list.append(eng_tuple)
        return tuple_list
    
    def equip_arkpassive(self):
        x_0 = [x['Description'].replace("<FONT color='#83E9FF'>",'').replace("<FONT color='#F1D594'>",'').replace("<FONT color='#C2EA55'>",'').replace("</FONT>",'') for x in self.ark()['Effects'] if x['Name']=='진화']
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
        
        return tier1, tier2, tier3, tier4