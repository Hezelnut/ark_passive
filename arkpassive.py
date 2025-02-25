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
        
        evolve_info = """
# t2_1 : 끝없는 마나
# t2_2 : 금단의 주문
# t2_3 : 예리한 감각
# t2_4 : 한계 돌파
# t2_5 : 최적화 훈련

# t3_1 : 무한한 마력
# t3_2 : 혼신의 강타
# t3_3 : 일격
# t3_4 : 파괴 전차
# t3_5 : 타이밍 지배
# t3_bh : 방향성 여부

# t4_1 : 뭉특한 가시
# t4_2 : 음속 돌파
# t4_3 : 인파이팅
# t4_4 : 입식 타격가
# t4_5 : 마나 용광로
        """

        print(evolve_info)

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
            '진화형 피해':[t4_3*9+t4_4*10.5+t4_1*7.5],
            '뭉툭한 가시':[False if t4_1==0 else True],
            '마나 용광로':[False if t4_5==0 else True],
            '음속 돌파':[False if t4_2==0 else True]
            }

        return tier4_stat
    
    def evolve_all(self):
        evolve_all_json = {
            'tier1':self.evolve_Tier_1(),
            'tier2':self.evolve_Tier_2(),
            'tier3':self.evolve_Tier_3(),
            'tier4':self.evolve_Tier_4()
        }
        return evolve_all_json

    # def enlight_all(self):
    #     return self.u1, self.u2, self.u3, self.u4
    
    # def jump_all(self):
    #     return self.v1, self.v2