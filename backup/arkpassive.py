class load_evolve:
    def __init__(self,ark_process):
        self.ark_process = ark_process
        tuple_1 = ark_process.equip_arkpassive()
        self.t1 = tuple_1[0]
        self.t2 = tuple_1[1]
        self.t3 = tuple_1[2]
        self.t4 = tuple_1[3]
    
    def Tier_1(self):
        stat_base = {'치명': 69, '신속': 72, '특화': 70}
        stat_base['치명'] = stat_base['치명'] + self.t1['치명']*50
        stat_base['신속'] = stat_base['신속'] + self.t1['신속']*50
        stat_base['특화'] = stat_base['특화'] + self.t1['특화']*50
        return stat_base

    def Tier_2(self):
        t2_1 = self.t2['t2_1']
        t2_2 = self.t2['t2_2']
        t2_3 = self.t2['t2_3']
        t2_4 = self.t2['t2_4']
        t2_5 = self.t2['t2_5']
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

    def Tier_3(self):
        t3_1 = self.t3['t3_1']
        t3_2 = self.t3['t3_2']
        t3_3 = self.t3['t3_3']
        t3_4 = self.t3['t3_4']
        t3_5 = self.t3['t3_5']
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

    def Tier_4(self):
        t4_1 = self.t4['t4_1']
        t4_2 = self.t4['t4_2']
        t4_3 = self.t4['t4_3']
        t4_4 = self.t4['t4_4']
        t4_5 = self.t4['t4_5']
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
    
    def Tier_all(self):
        return self.Tier_1(), self.Tier_2(), self.Tier_3(), self.Tier_4()


class load_enlight:
    def __init__(self,ark_process):
        self.ark_process = ark_process
        tuple_2 = ark_process.equip_enlight()
        self.u1 = tuple_2[0]
        self.u2 = tuple_2[1]
        self.u3 = tuple_2[2]
        self.u4 = tuple_2[3]
    def ark_enlight(self):
        return self.u1, self.u2, self.u3, self.u4

class load_jump:
    def __init__(self,ark_process):
        self.ark_process = ark_process     
        tuple_3 = ark_process.equip_jump()
        self.v1 = tuple_3[0]
        self.v2 = tuple_3[1]
    def ark_jump(self):
        return self.v1, self.v2