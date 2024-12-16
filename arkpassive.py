def Tier_1(t1):
    stat_base = {'crit': 69, 'vel': 72, 'abl': 70}
    stat_base['crit'] = stat_base['crit'] + t1['crit']*50
    stat_base['vel'] = stat_base['vel'] + t1['vel']*50
    stat_base['abl'] = stat_base['abl'] + t1['abl']*50
    return stat_base

def Tier_2(t2):
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

def Tier_3(t3):
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

def Tier_4(t4):
    t4_1 = t4['t4_1']
    t4_2 = t4['t4_2']
    t4_3 = t4['t4_3']
    t4_4 = t4['t4_4']
    t4_5 = t4['t4_5']
    if t4_1+t4_2+t4_3+t4_4+t4_5>2:
        print('Error')
        print('Error')
    else:
        tier4_stat = {
        '진화형 피해':[t4_3*9+t4_4*10.5],
        '뭉특한 가시':[False if t4_1==0 else True],
        '마나 용광로':[False if t4_5==0 else True],
        '음속 돌파':[False if t4_2==0 else True]
        }

    return tier4_stat