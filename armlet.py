import re
from player_load import get_name

class armlet_option:
    def __init__(self,response):
        self.response = response
        self.option_list = []
        self.dict_stat = {
            '특성':{'치명':0,'신속':0,'특화':0},
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

    def armlet_output(self):
        armlet_json = self.response['armlet']
        jump_point = armlet_json['Element_007']['value']['Element_001']
        armlet_output = [jump_point]
        armlet_option = armlet_json['Element_004']['value']['Element_001'].lower().replace("<fontcolor='#99ff99'>",'') #.split('[]')
        armlet_option = armlet_option.replace("<fontcolor='#ff9999'>",'').replace("</font>",'').replace("</img>",'[]').replace("<br>",'[]')
        armlet_option = armlet_option.replace("<imgsrc='emoticon_tooltip_bracelet_locked'vspace='-5'>",'').replace("<imgsrc='emoticon_tooltip_bracelet_changeable'width='20'height='20'vspace='-6'>",'')
        armlet_option = armlet_option.replace("[][]","<>").replace("[]",'').split("<>")
        # armlet_option = [x for x in armlet_option if '<' not in x ]
        armlet_output.extend(armlet_option)
        return armlet_output


    def option(self,option):
        s1 = r"특화\W(.+)"
        match_s1 = re.search(s1, option)
        if match_s1:
            print("특화")
            n = int(match_s1.group(1))
            self.dict_stat['특성']['특화'] = n
            self.option_list.append('특화')
            return
        else:
            pass

        s2 = r"치명\W(.+)"
        match_s2 = re.search(s2, option)
        if match_s2:
            print("치명")
            n = int(match_s2.group(1))
            self.dict_stat['특성']['치명'] = n
            self.option_list.append('치명')
            return
        else:
            pass
        
        s3 = r"신속\W(.+)"
        match_s3 = re.search(s3, option)
        if match_s3:
            print("신속")
            n = int(match_s3.group(1))
            self.dict_stat['특성']['신속'] = n
            self.option_list.append('신속')
            return
        else:
            pass
        
        s4_0 = r"힘\W(\d{4})"
        match_s4_0 = re.search(s4_0, option)
        if match_s4_0:
            n = int(match_s4_0.group(1))
            self.dict_stat['스탯 증가 (+)'].append(n)
            print("힘")
            self.option_list.append('힘')
            return
        else:
            pass
        
        s4_1 = r"민첩\W(\d{4})"
        match_s4_1 = re.search(s4_1, option)
        if match_s4_1:
            n = int(match_s4_1.group(1))
            self.dict_stat['스탯 증가 (+)'].append(n)
            print("민첩")
            self.option_list.append('민첩')
            return
        else:
            pass
        
        s4_2 = r"지능\W(\d{4})"
        match_s4_2 = re.search(s4_2, option)
        if match_s4_2:
            n = int(match_s4_2.group(1))
            self.dict_stat['스탯 증가 (+)'].append(n)
            print("지능")
            self.option_list.append('지능')
            return
        else:
            pass        
        
        p1_0 = r"\b적에게주는피해가(\d.?\d?)%증가한다."
        match_p1_0 = re.search(p1_0, option)
        if match_p1_0:
            n = float(match_p1_0.group(1))
            self.dict_stat['피해 증가'].append(n)
            print("피증 단일")
            self.option_list.append(f'피증 단일 : {n}%')
            return
        else:
            pass
        
        p1_1 = r"적에게주는피해가(\d.?\d?)%증가하며,무력화상태의적에게주는피해가(\d.?\d?)%증가한다."
        match_p1_1 = re.search(p1_1, option)
        if match_p1_1:
            n = float(match_p1_1.group(1))
            self.dict_stat['피해 증가'].append(n)
            print("피증 이중옵 - 무력화")
            self.option_list.append(f'피증 이중옵 - 무력화 : {n}%')
            return
        else:
            pass
        
        p1_2 = r"스킬의재사용대기시간이2%증가하지만,적에게주는피해가(\d.?\d?)%증가한다."
        match_p1_2 = re.search(p1_2, option)
        if match_p1_2:
            n = float(match_p1_2.group(1))
            self.dict_stat['피해 증가'].append(n)
            print("피증 이중옵 - 쿨타임증가")
            self.option_list.append(f'피증 이중옵 - 쿨타임증가 : {n}%')
            return
        else:
            pass
        
        p2_0 = r"치명타적중률\W(\d\W\d{2})%"
        match_p2_0 = re.search(p2_0, option)
        if match_p2_0:
            n = float(match_p2_0.group(1))
            self.dict_stat['치명타 적중률 증가'].append(n)
            print("치적 단일옵")
            self.option_list.append(f'치적 단일 : {n}%')
            return
        else:
            pass

        p2_1 = r"치명타적중률이(.+)%증가한다.공격이치명타로적중시적에게주는피해가(.+)%증가한다."
        match_p2_1 = re.search(p2_1, option)
        if match_p2_1:
            n = float(match_p2_1.group(1))
            self.dict_stat['치명타 적중률 증가'].append(n)
            m = float(match_p2_1.group(2))
            self.dict_stat['치명타 시 피해 증가'].append(m)
            print("치적 이중옵 - 회심")
            self.option_list.append(f'치적 이중옵 / 회심 : {n}% / {m}%')
            return
        else:
            pass
        
        p3_0 = r"치명타피해\W(\d\d?\W\d{2})%"
        match_p3_0 = re.search(p3_0, option)
        if match_p3_0:
            n = float(match_p3_0.group(1))
            self.dict_stat['치명타 피해 증가'].append(n)
            print("치피증 단일옵")
            self.option_list.append(f'치피증 단일 : {n}%')
            return
        else:
            pass    
        
        p3_1 = r"치명타피해가(.+)%증가한다.공격이치명타로적중시적에게주는피해가(.+)%증가한다."
        match_p3_1 = re.search(p3_1, option)
        if match_p3_1:
            n = float(match_p3_1.group(1))
            self.dict_stat['치명타 피해 증가'].append(n)
            m = float(match_p3_1.group(2))
            self.dict_stat['치명타 시 피해 증가'].append(m)
            print("치피증 이중옵 - 회심")
            self.option_list.append(f'치피증 이중옵 / 회심 : {n}% / {m}%')
            return
        else:
            pass


        p4_0 = r"무기공격력\W(\d{4})"
        match_p4_0 = re.search(p4_0, option)
        if match_p4_0:
            n = int(match_p4_0.group(1))
            self.dict_stat['무기공격력 증가 (+)'].append(n)
            print("무공 단일옵")
            self.option_list.append(f'무공 단일 : {n}')
            return
        else:
            pass
        
        p4_1 = r'무기공격력이(\d{4})증가한다.자신의생명력이50%이상일경우적에게공격적중시5초동안무기공격력이(.+)증가한다.'
        match_p4_1 = re.search(p4_1, option)
        if match_p4_1:
            n = int(match_p4_1.group(1))
            m = int(match_p4_1.group(2))
            self.dict_stat['무기공격력 증가 (+)'].append(n+m)
            print("안상 무공")
            self.option_list.append(f'안상 무공 : {n} + {m}')
            return
        else:
            pass

        p4_2 = r"무기공격력이(\d{4})증가한다.공격적중시30초마다120초동안무기공격력이(\d{3})증가한다.(.+)"
        match_p4_2 = re.search(p4_2, option)
        if match_p4_2:
            n = int(match_p4_2.group(1))
            m = int(match_p4_2.group(2))
            self.dict_stat['무기공격력 증가 (+)'].append(n+m*30)
            print("에포 무공")
            self.option_list.append(f'에포 무공 : {n} + {m}*30')
            return
        else:
            pass
        
        p4_3 = r"공격적중시매초마다10초동안무기공격력이(.+)\W공격및이동속도가1%증가한다.(.+)"
        match_p4_3 = re.search(p4_3, option)
        if match_p4_3:
            n = int(match_p4_3.group(1))
            self.dict_stat['무기공격력 증가 (+)'].append(n*6)
            self.dict_stat['공격속도'].append(6)
            self.dict_stat['이동속도'].append(6)
            print("공이속 무공")
            self.option_list.append(f'공이속 6% + 무공 {n*6}')
            return
        else:
            pass

        p5_0 = r"추가피해\W(.+)%"
        match_p5_0 = re.search(p5_0, option)
        if match_p5_0:
            print(option)
            n = float(match_p5_0.group(1))
            self.dict_stat['추가 피해'].append(n)
            print("추피 단일옵")
            self.option_list.append(f'추피 단일 : {n}%')
            return
        else:
            pass

        p5_1 = r'추가피해가(.+)%증가한다.악마및대악마계열피해량이(.+)%증가한다.'
        match_p5_1 = re.search(p5_1, option)
        if match_p5_1:
            n = float(match_p5_1.group(1))
            self.dict_stat['추가 피해'].append(n)
            m = float(match_p5_1.group(2))
            self.dict_stat['추가 피해'].append(m) ## 최종컨텐츠에 따라 배율 수정하기
            print("추피 이중옵 - 진멸")
            self.option_list.append(f'추피 이중옵 - 진멸 : {n}% / {m}%')
            return
        else:
            pass    
        
        p10_0 = r"방향성공격이아닌스킬이적에게주는피해가(.+)%증가한다.각성기는적용되지않는다."
        match_p10_0 = re.search(p10_0, option)
        if match_p10_0:
            n = float(match_p10_0.group(1))
            self.dict_stat['비방향성'].append(n)
            print("비방향성")
            self.option_list.append(f'비방향성 : {n}%')
            return
        else:
            pass
        
        p10_1 = r"헤드어택스킬이적에게주는피해가(.+)%증가한다."
        match_p10_1 = re.search(p10_1, option)
        if match_p10_1:
            n = float(match_p10_1.group(1))
            self.dict_stat['헤드어택'].append(n)
            print("헤드어택")
            self.option_list.append(f'헤드어택 : {n}%')
            return
        else:
            pass
        
        p10_2 = r"백어택스킬이적에게주는피해가(.+)%증가한다."
        match_p10_2 = re.search(p10_2, option)
        if match_p10_2:
            n = float(match_p10_2.group(1))
            self.dict_stat['백어택'].append(n)
            print("백어택")
            self.option_list.append(f'백어택 : {n}%')
            return
        else:
            pass
        
    def armlet_options(self):
        options = self.armlet_output()
        for o in options:
            self.option(o)
        
        return self.dict_stat, self.option_list
    
if __name__ == '__main__':
    
    user_info = get_name('솔이곰')
    response = user_info.get_response()

    armlet_info = armlet_option(response)
    stat, option_list = armlet_info.armlet_options()
    print(stat)
    print(option_list)
    