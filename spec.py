import re
import pandas
import json


class equipment:
    def __init__(self,response):
        self.response = response
        self.dict_stat = {'특성':{'치명':0,'신속':0,'특화':0},
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

# """
# user_name = get_name('nickname')
# response = user_name.get_reponse()
# armor_info = armor(response)
# """


# 엘릭서
    def elixer(self):    
        
        elixer_armor = self.response['armor']

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
        
        for k in range(0,5):
            elixer_1 = elixer_armor[k]['Element_010']['value']['Element_000']['contentStr']['Element_000']['contentStr']
            elixer_2 = elixer_armor[k]['Element_010']['value']['Element_000']['contentStr']['Element_001']['contentStr']
            elixer_list.append(compile(elixer_1))
            elixer_list.append(compile(elixer_2))

        list_elixer_option = list()
        for e in elixer_list:
            if len(e)==2:
                list_elixer_option.append(e[1])
            if len(e)==4:
                list_elixer_option.extend(e[0:-1])
        
        i = 0
        j = 0

        for e in list_elixer_option:
            if ('무기공격력' in e) and ('%' not in e) :
                self.dict_stat['무기공격력 증가 (+)'].append(int(e.split('+')[1]))
            if ('공격력' in e) and ('무기' not in e) and ('%' in e):
                self.dict_stat['공격력 증가 (%)'].append(float(e.replace("%",'').split('+')[1]))
            if ('공격력' in e) and ('무기' not in e) and ('%' not in e):
                self.dict_stat['공격력 증가 (+)'].append(int(e.split('+')[1]))
            if '추가피해' in e :
                self.dict_stat['추가 피해'].append(float(e.replace("%",'').split('+')[1]))
            if ('적에게주는피해' in e) or ('보스' in e) :
                e_ = float(e.replace("%",'').split('+')[1])
                e_ = (100+e_)/100
                self.dict_stat['피해 증가'].append(e_)
            if '치명타피해' in e :
                self.dict_stat['치명타 피해 증가'].append(float(e.replace("%", '').split('+')[1]))
            if '최대생명력' in e :
                self.dict_stat['최대 생명력'].append(int(e.split('+')[1]))

            if '회심(질서)' in e:
                i += 1
            if '회심(혼돈)' in e:
                i += 1
            if '달인(질서)' in e:
                j += 1
            if '달인(혼돈)' in e:
                j += 1

        if j == 2 :
            self.dict_stat['추가 피해'].append(8.5)
            self.dict_stat['치명타 적중률 증가'].append(7)
            elixer_name = '달인'
        if i == 2 :
            self.dict_stat['치명타 시 피해 증가'].append(1.12)
            elixer_name = '회심'

        return elixer_name

    # 초월
    def transcendence(self):
            
        info_armor = self.response['armor']
        info_weapon = self.response['weapon']

        transcendence_all = list()

        def tran_sub(data):
            tran_0 = data['Element_009']['value']['Element_000']['contentStr']['Element_000']['contentStr']
            tran_1 = data['Element_009']['value']['Element_000']['topStr']
            tran_1 = tran_1.replace("<FONTCOLOR='#FFD200'>",'split/').replace("</FONT>",'split/').replace("</img>",'split/')
            tran_1 = tran_1.split('split/')
            tran_1 = tran_1[3]+'단계 '+tran_1[-1]
            return [tran_0, tran_1]
        
        for k in range(0,5):
            transcendence_all.extend(tran_sub(info_armor[k]))

        transcendence_all.extend(tran_sub(info_weapon))
        
        transcendence_stage = list()
        sum_transcendence = 0

        for u in transcendence_all:
            if '무기공격력' in u:
                self.dict_stat['무기공격력 증가 (+)'].append(int(u.split('+')[1]))
            if ('힘' in u) or ('지능' in u) or ('민첩' in u) :
                self.dict_stat['스탯 증가 (+)'].append(int(u.split('+')[1]))
            if '단계' in u:
                sum_transcendence += int(u.split(' ')[-1])
                transcendence_stage.append(u)

        transcendence_stage.append(f'총 {sum_transcendence}')
        
        #투구
        self.dict_stat['최대 생명력'].append(int(sum_transcendence*80))
        self.dict_stat['무기공격력 증가 (+)'].append(int(sum_transcendence*14))
        self.dict_stat['스탯 증가 (+)'].append(int(sum_transcendence*55))
        self.dict_stat['공격력 증가 (+)'].append(int(sum_transcendence*6))
        
        #어꺠
        self.dict_stat['무기공격력 증가 (+)'].append(3600)
        self.dict_stat['마법 방어력'].append(1800)

        #상의
        self.dict_stat['무기공격력 증가 (+)'].append(7200)
        self.dict_stat['체력'].append(1400)

        #하의
        self.dict_stat['피해 증가'].append(1.015)

        #장갑
        self.dict_stat['스탯 증가 (+)'].append(12600)
        self.dict_stat['물리 방어력'].append(1800)

        #무기
        self.dict_stat['공격력 증가 (+)'].append(3525)

        return transcendence_stage


    # 악세사리
    def accessory(self):
        
        gem = self.response['gems']

        info_acc = self.response['accessory']
        info_stone = self.response['stone']

        gem_stat = (100+float(gem['Effects']['Description'].replace("기본 공격력 총합 : ","<split>").replace("%</FONT>","<split>").split("<split>")[1]))/100

        acc_list = list()
        for k in range(0,5):
            acc_0 = info_acc[k]['Element_007']['value']['Element_001']
            acc_1 = info_acc[k]['Element_005']['value']['Element_001'].lower().replace("</img>",'split/').replace("<br",'split/').split('split/')
            acc_1 = acc_1[1::2]    
            acc_list.extend(acc_1)
            acc_list.extend(info_acc[k]['Element_004']['value']['Element_001'].replace("<FONTCOLOR='#686660'>",'').replace("</FONT>",'').split("<BR>")[2:])
        # acc_list_head = [x for x in acc_list if '%' in x]
        acc_list = [x for x in acc_list if ('파티원' not in x) and ('아군' not in x) and ('상태이상' not in x) and ('전투' not in x)]

        
        stone_1, stone_2 = info_stone['Element_004']['value']['Element_001'], info_stone['Element_005']['value']['Element_001']
        stone = int(stone_1.split('+')[1])+int(stone_2.split('+')[1])
        
        if 'Element_003' in list(info_stone['Element_006']['value']['Element_000']['contentStr'].keys()):
            stone97 = info_stone['Element_006']['value']['Element_000']['contentStr']['Element_003']['contentStr'].replace("기본공격력+","<split>").replace("%<BR>","<split>").split("<split>")[1]
            stone97 = (float(stone97))/100
            self.dict_stat['기본 공격력 증가 (%)'].append(stone97)

        
        for e in acc_list:
            if ('무기공격력' in e) and ('%' in e):
                self.dict_stat['무기공격력 증가 (%)'].append(float(e.replace("%",'').split('+')[1]))
            if ('무기공격력' in e) and ('%' not in e) :
                self.dict_stat['무기공격력 증가 (+)'].append(int(e.split('+')[1]))
            if ('공격력' in e) and ('무기' not in e) and ('%' in e):
                self.dict_stat['공격력 증가 (%)'].append(float(e.replace("%",'').split('+')[1]))
            if ('공격력' in e) and ('무기' not in e) and ('%' not in e):
                self.dict_stat['공격력 증가 (+)'].append(int(e.split('+')[1]))
            if '추가피해' in e :
                self.dict_stat['추가 피해'].append(float(e.replace("%",'').split('+')[1]))
            if '적에게주는피해' in e :
                e_ = float(e.replace("%",'').split('+')[1])
                e_ = (100+e_)/100
                self.dict_stat['피해 증가'].append(e_)
            if '치명타적중률' in e :
                self.dict_stat['치명타 적중률 증가'].append(float(e.replace("%", '').split('+')[1]))
            if '치명타피해' in e :
                self.dict_stat['치명타 피해 증가'].append(float(e.replace("%", '').split('+')[1]))
            if '체력' in e :
                self.dict_stat['체력'].append(int(e.split('+')[1]))
            if '지능' in e :
                self.dict_stat['스탯 증가 (+)'].append(int(e.split('+')[1]))
            if '최대생명력' in e :
                self.dict_stat['최대 생명력'].append(int(e.split('+')[1]))

        self.dict_stat['체력'].append(stone)
        self.dict_stat['기본 공격력 증가 (%)'].append(gem_stat)
        
        return acc_list

    # 품질 & 힘민지 스탯
    def stat(self):
            
        armor = self.response['armor']
        weapon = self.response['weapon']

        stat_list = list()
        stat_weapon = weapon['Element_006']['value']['Element_001'].split('<BR>')
        stat_list.extend(stat_weapon)
        for k in range(0, 5):
            stat_armor = armor[k]['Element_006']['value']['Element_001'].split('<BR>')
            stat_list.extend(stat_armor)
        
        quality_armor = 0
        quality_weapon = float(weapon['Element_007']['value']['Element_001'].replace('%','').split('+')[-1])
        
        for k in range(0, 5):
            quality_armor += int(armor[k]['Element_007']['value']['Element_001'].split('+')[-1])
        
        hp_percent = 1+quality_armor/14000

        for u in stat_list:
            if '무기공격력' in u:
                self.dict_stat['무기공격력 증가 (+)'].append(int(u.split('+')[1]))
            if ('힘' in u) or ('지능' in u) or ('민첩' in u) :
                self.dict_stat['스탯 증가 (+)'].append(int(u.split('+')[1]))
            if '체력' in u:
                self.dict_stat['체력'].append(int(u.split('+')[1]))
            if '물리방어력' in u:
                self.dict_stat['물리 방어력'].append(int(u.split('+')[1]))
            if '마법방어력' in u:
                self.dict_stat['마법 방어력'].append(int(u.split('+')[1]))

        self.dict_stat['추가 피해'].append(quality_weapon)
        self.dict_stat['생명력 활성'].append(hp_percent)

        return self.dict_stat

    def equip_all(self):
        elixer_name = self.elixer()
        self.transcendence()
        acc_list = self.accessory()
        self.stat()
        
        spec_dict ={
            'elixer' : elixer_name,
            'accessory' : acc_list
        }
        return self.dict_stat, spec_dict

# 보석
def gem_info(response):
    gem = response['gems']

    # _, gem = user_info.skill_and_gem()

    gem_dict = dict()
    
    gem_name = [x['Name'] for x in gem['Effects']['Skills']]
    gem_name = list(set(gem_name))    

    for g in gem_name:
        gem_decription = [x['Description'][0] for x in gem['Effects']['Skills'] if x['Name']==g]
        gem_dict[g] = gem_decription

    gem_df = pandas.DataFrame(columns=['Skill_name','gem_effect'])

    row_num = 0
    for g1 in list(gem_dict.keys()):
        for g2 in gem_dict[g1]:
            gem_df.loc[row_num] = [g1, g2]
            row_num += 1

    return gem_df

# 스킬
def skill_tripod(response):
    skill = response['skill']
    # skill, _ = user_info.skill_and_gem()
    selected_skill = list()

    for s in skill:
        if s['Level']>1:
            selected_skill.append(s['Name'])

    skill_info = [{s['Name']:[[x['Name'],str(x['Level'])+'레벨',x['Tooltip']] for x in s['Tripods'] if x['IsSelected']==True]} for s in skill if s['Name'] in selected_skill]

    tripod = pandas.DataFrame(columns=['Skill_name','Tripod','Tripod_level','Tripod_effect'])
    row_num = 0

    for f in range(0,len(skill_info)):
        n = list(skill_info[f].keys())[0]
        for g in skill_info[f][n]:
            tripod.loc[row_num] = [n,g[0],g[1],g[2].replace("<font color='#FFFDE7'>",'').replace("<FONT COLOR='#ffff99'>",'').replace("</FONT>",'').replace("<FONT COLOR='#99ff99'>",'').replace("</font>",'')]
            row_num +=1

    return tripod

#엘릭서, 초월, 악세, 팔찌, 각인서, 