from player_load import equip, process
from engrave import engraving
from spec import transcendence,elixer,accessory
from arkpassive import load_evolve, load_enlight, load_jump

user_info = equip(input('플레이어 이름 : '))

# API 호출을 딱 세번만 하도록 분리해서 저장.
# _, _, _ = user_info.equipment() 
# 각각 장비, 각인, 아크패시브
equ, eng, ark = user_info.equipment()

equip_process = process(equ)
engrave_process = process(eng)
ark_process = process(ark)

transcendence(equip_process) # 초월 정보
accessory(equip_process) # 악세사리의 특옵 정보
elixer(equip_process) # 엘릭서정보
engraving(engrave_process) # 각인서 효과를 종합한 정보

load_evolve(ark_process).Tier_all() # 진화탭 모든 티어 정보
# Tier_1()
# Tier_2()
# Tier_3()
# TIer_4() 가능

load_enlight(ark_process).ark_enlight() # 깨달음 탭

load_jump(ark_process).ark_jump() # 도약 탭

