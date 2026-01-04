import streamlit as st
import math

# --- 1. 核心函數 (調整倍率邏輯) ---

def Spower(power,c,d,buffatk,buffdef,criticle,light,typatk,typem,typdef,status,buff,debuff,plus,move):
    listdamage=[]
    # 這裡 buffatk 與 buffdef 包含階級修正與勾選框倍率
    c*=buffatk ; d*=buffdef
    if item2=="突擊背心":
        d*=1.5
    inner=math.floor(22*power*c/d)
    base=math.floor(inner/72)+2
    damagemin=math.floor(base*0.85)
    damagemax=math.floor(base*1)
    if criticle==True:
        damagemin*=1.5 ; damagemax*=1.5
        light=False
    if light==True:
        damagemin=damagemin*2/3 ;  damagemax=damagemax*2/3 
    if buff==True:
        damagemin*=2 ; damagemax*=2
    if debuff==True:
        damagemin/=2 ; damagemax/=2
    if item1=="生命寶珠":
        damagemin*=1.3 ; damagemax*=1.3
    if item1=="博識眼鏡":
        damagemin*=1.1 ; damagemax*=1.1     
    damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    if typem==typatk[0] or (len(typatk)>1 and typem==typatk[1]):   
       damagemin=math.floor(damagemin*1.5) ; damagemax=math.floor(damagemax*1.5)
    dmin=damagemin ; dmax=damagemax
    
    # 屬性判定邏輯 (完整保留)
    for k in  range(0,len(typdef)):
            if typem=="normal":
                if item1=="一般寶石"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2                  
                if typdef[k]=="steel":
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="ghost":
                     damagemin*=0 ; damagemax*=0
            elif typem=="fighting":
                if item1=="黑帶"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["normal", "steel", "rock", "ice", "dark"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["poison", "bug", "flying", "psychic", "fairy"]:
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="ghost":
                     damagemin*=0 ; damagemax*=0
            elif typem=="flying":
                if item1=="銳利鳥嘴"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["fighting", "bug", "grass"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["rock", "steel", "thunder"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="poison":
                if item1=="毒針"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["grass", "fairy"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["poison", "ground", "rock", "ghost"]:
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="steel":
                     damagemin*=0 ; damagemax*=0
            elif typem=="ground":
                if item1=="柔軟沙子"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if move=="千箭齊發":
                    if "flying" in typdef: continue
                elif typdef[k] in ["poison", "rock", "steel", "fire", "electric"]:
                    damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["bug", "grass"]:
                    damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="flying":
                    damagemin*=0 ; damagemax*=0
            elif typem=="rock":
                if item1=="硬石頭"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["flying", "bug", "fire", "ice"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["fighting", "ground", "steel"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="bug":
                if item1=="銀粉"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["dark", "psychic", "grass"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["fighting", "flying", "poison", "steel", "fire", "fairy", "ghost"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="ghost":
                if item1=="詛咒之符"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["ghost", "psychic"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k]=="dark":
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="normal":
                     damagemin*=0 ; damagemax*=0
            elif typem=="steel":
                 if item1=="金屬膜"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ice", "fairy", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["electric", "fire", "water", "steel"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="water":
                 if item1=="神秘水滴"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ground", "fire", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["grass", "dragon", "water"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="grass":
                 if item1=="奇跡種子"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ground", "water", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["grass", "dragon", "fire", "steel", "flying", "bug", "poison"]: 
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="fire":
                 if item1=="木炭"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["grass", "ice", "bug", "steel"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["fire", "dragon", "water", "rock"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="electric":
                 if item1=="磁鐵"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["water", "flying"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["electric", "dragon", "grass"]:
                     damagemin*=0.5 ; damagemax*=0.5 
                 elif typdef[k]=="ground":
                     damagemin*=0 ; damagemax*=0
            elif typem=="psychic":
                 if item1=="彎曲的湯匙"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["fighting", "poison"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["steel", "psychic"]:
                     damagemin*=0.5 ; damagemax*=0.5 
                 elif typdef[k]=="dark":
                      damagemin*=0 ; damagemax*=0
            elif typem=="dragon":
                 if item1=="龍之牙"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k]=="dragon":
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k]=="steel":
                     damagemin*=0.5 ; damagemax*=0.5 
                 elif typdef[k]=="fairy":
                     if move!="歸無之光":
                        damagemin*=0 ; damagemax*=0 
            elif typem=="ice":
                 if item1=="不融冰"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["flying", "ground", "dragon", "grass"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k]=="water":
                      if move=="冷凍乾燥":
                          damagemin*=2 ; damagemax*=2
                      else:
                          damagemin*=0.5 ; damagemax*=0.5 
                 elif typdef[k] in ["steel", "fire", "ice"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="dark":
                 if item1=="黑色眼鏡"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ghost", "psychic"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["dark", "fighting", "fairy"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="fairy":
                 if item1=="妖精之羽"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["dragon", "dark", "fighting"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["steel", "poison", "fire"]:
                     damagemin*=0.5 ; damagemax*=0.5
    damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    
    
    if damagemin>(dmin*1.7) and damagemax>(dmax*1.7):
        if plus==True:
            damagemin*=1.3 ; damagemax*=1.3
            damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
        if item1=="達人帶":
            damagemin*=1.2 ; damagemax*=1.2
            damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    else:
        if plus==True:
            damagemin*=1.2 ; damagemax*=1.2
            damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    if damagemin>0 and damagemin<1:
        damagemin=1
    if damagemax>0 and damagemax<1:
        damagemax=1
        
    listdamage.append(damagemin) ; listdamage.append(damagemax)
    return listdamage

def Ppower(power,a,b,buffatk,buffdef,criticle,reflect,typatk,typem,typdef,status,buff,debuff,plus,move):
    listdamage=[]
    a*=buffatk ; b*=buffdef
    inner=math.floor(22*power*a/b)
    base=math.floor(inner/72)+2
    damagemin=math.floor(base*0.85)
    damagemax=math.floor(base*1)
    if criticle==True:
        damagemin*=1.5 ; damagemax*=1.5
        reflect=False
    if reflect==True:
        damagemin=damagemin*2/3 ;  damagemax=damagemax*2/3
    if status==True:
        damagemin*=0.5 ; damagemax*=0.5
    if buff==True:
        damagemin*=2 ; damagemax*=2
    if debuff==True:
        damagemin/=2 ; damagemax/=2
    if item1=="生命寶珠":
        damagemin*=1.3 ; damagemax*=1.3
    if item1=="力量頭帶":
        damagemin*=1.1 ; damagemax*=1.1
    damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    if typem==typatk[0] or (len(typatk)>1 and typem==typatk[1]):
       damagemin=math.floor(damagemin*1.5) ; damagemax=math.floor(damagemax*1.5)
    dmin=damagemin ; dmax=damagemax
    
    # 物理屬性判定 (與特攻一致)
    for k in  range(0,len(typdef)):
            if typem=="normal":
                if item1=="一般寶石"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2                  
                if typdef[k]=="steel":
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="ghost":
                     damagemin*=0 ; damagemax*=0
            elif typem=="fighting":
                if item1=="黑帶"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["normal", "steel", "rock", "ice", "dark"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["poison", "bug", "flying", "psychic", "fairy"]:
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="ghost":
                     damagemin*=0 ; damagemax*=0
            elif typem=="flying":
                if item1=="銳利鳥嘴"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["fighting", "bug", "grass"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["rock", "steel", "thunder"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="poison":
                if item1=="毒針"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["grass", "fairy"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["poison", "ground", "rock", "ghost"]:
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="steel":
                     damagemin*=0 ; damagemax*=0
            elif typem=="ground":
                if item1=="柔軟沙子"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if move=="千箭齊發":
                    if "flying" in typdef: continue
                elif typdef[k] in ["poison", "rock", "steel", "fire", "electric"]:
                    damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["bug", "grass"]:
                    damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="flying":
                    damagemin*=0 ; damagemax*=0
            elif typem=="rock":
                if item1=="硬石頭"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["flying", "bug", "fire", "ice"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["fighting", "ground", "steel"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="bug":
                if item1=="銀粉"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["dark", "psychic", "grass"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k] in ["fighting", "flying", "poison", "steel", "fire", "fairy", "ghost"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="ghost":
                if item1=="詛咒之符"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                if typdef[k] in ["ghost", "psychic"]:
                     damagemin*=2 ; damagemax*=2
                elif typdef[k]=="dark":
                     damagemin*=0.5 ; damagemax*=0.5
                elif typdef[k]=="normal":
                     damagemin*=0 ; damagemax*=0
            elif typem=="steel":
                 if item1=="金屬膜"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ice", "fairy", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["electric", "fire", "water", "steel"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="water":
                 if item1=="神秘水滴"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ground", "fire", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["grass", "dragon", "water"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="grass":
                 if item1=="奇跡種子"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ground", "water", "rock"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["grass", "dragon", "fire", "steel", "flying", "bug", "poison"]: 
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="fire":
                 if item1=="木炭"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["grass", "ice", "bug", "steel"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["fire", "dragon", "water", "rock"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="electric":
                 if item1=="磁鐵"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["water", "flying"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["electric", "dragon", "grass"]:
                     damagemin*=0.5 ; damagemax*=0.5 
                 elif typdef[k]=="ground":
                     damagemin*=0 ; damagemax*=0
            elif typem=="psychic":
                 if item1=="彎曲的湯匙"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["fighting", "poison"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["steel", "psychic"]:
                     damagemin*=0.5 ; damagemax*=0.5 
                 elif typdef[k]=="dark":
                      damagemin*=0 ; damagemax*=0
            elif typem=="dragon":
                 if item1=="龍之牙"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k]=="dragon":
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k]=="steel":
                     damagemin*=0.5 ; damagemax*=0.5 
                 elif typdef[k]=="fairy":
                     if move!="歸無之光":
                        damagemin*=0 ; damagemax*=0 
            elif typem=="ice":
                 if item1=="不融冰"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["flying", "ground", "dragon", "grass"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k]=="water":
                      if move=="冷凍乾燥":
                          damagemin*=2 ; damagemax*=2
                      else:
                          damagemin*=0.5 ; damagemax*=0.5 
                 elif typdef[k] in ["steel", "fire", "ice"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="dark":
                 if item1=="黑色眼鏡"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["ghost", "psychic"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["dark", "fighting", "fairy"]:
                     damagemin*=0.5 ; damagemax*=0.5
            elif typem=="fairy":
                 if item1=="妖精之羽"and k==0:
                     damagemin*=1.2 ; damagemax*=1.2
                 if typdef[k] in ["dragon", "dark", "fighting"]:
                     damagemin*=2 ; damagemax*=2
                 elif typdef[k] in ["steel", "poison", "fire"]:
                     damagemin*=0.5 ; damagemax*=0.5     
    damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    
    if damagemin>(dmin*1.7) and damagemax>(dmax*1.7):
        if plus==True:
            damagemin*=1.3 ; damagemax*=1.3
            damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
        if item1=="達人帶":
            damagemin*=1.2 ; damagemax*=1.2
            damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    else:
        if plus==True:
            damagemin*=1.2 ; damagemax*=1.2
            damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    if damagemin>0 and damagemin<1:
        damagemin=1
    if damagemax>0 and damagemax<1:
        damagemax=1
    damagemin=math.floor(damagemin) ; damagemax=math.floor(damagemax)
    listdamage.append(damagemin) ; listdamage.append(damagemax)
    return listdamage

# --- 2. 數據定義 (包含 236 隻 + None 補丁) ---

pokemon = {
    "妙蛙花": [80, 82, 83, 100, 100, 80, ["grass", "poison"]], "噴火龍": [78, 84, 78, 109, 85, 100, ["fire", "flying"]],
    "水箭龜": [79, 83, 100, 85, 105, 78, ["water", "none"]], "大比鳥": [83, 80, 75, 70, 70, 101, ["normal", "flying"]],
    "大針蜂": [65, 90, 40, 45, 80, 75, ["bug", "poison"]], "胡地": [55, 50, 45, 135, 95, 120, ["psychic", "none"]],
    "呆呆王": [95, 75, 80, 100, 110, 30, ["water", "psychic"]], "耿鬼": [60, 65, 60, 130, 75, 110, ["ghost", "poison"]],
    "袋獸": [105, 95, 80, 40, 80, 90, ["normal", "none"]], "凱羅斯": [65, 125, 100, 55, 70, 85, ["bug", "none"]],
    "暴鯉龍": [95, 125, 79, 60, 100, 81, ["water", "flying"]], "化石翼龍": [80, 105, 65, 60, 75, 130, ["rock", "flying"]],
    "超夢": [106, 110, 90, 154, 90, 130, ["psychic", "none"]], "電龍": [90, 75, 85, 115, 90, 55, ["electric", "none"]],
    "大鋼蛇": [75, 85, 200, 55, 65, 30, ["steel", "ground"]], "巨鉗螳螂": [70, 130, 100, 55, 80, 65, ["bug", "steel"]],
    "赫拉克羅斯": [80, 125, 75, 40, 95, 85, ["bug", "fighting"]], "黑魯加": [75, 90, 50, 110, 80, 95, ["dark", "fire"]],
    "班基拉斯": [100, 134, 110, 95, 100, 61, ["rock", "dark"]], "巨沼怪": [100, 110, 90, 85, 90, 65, ["water", "ground"]],
    "沙奈朵": [68, 65, 65, 125, 115, 80, ["psychic", "fairy"]], "勾魂眼": [50, 75, 75, 65, 65, 50, ["dark", "ghost"]],
    "大嘴娃": [50, 85, 85, 55, 55, 50, ["steel", "fairy"]], "波士可多拉": [70, 110, 180, 60, 60, 50, ["steel", "rock"]],
    "恰雷姆": [60, 60, 75, 60, 75, 80, ["fighting", "psychic"]], "雷電獸": [70, 75, 60, 105, 60, 105, ["electric", "none"]],
    "巨牙鯊": [70, 120, 40, 95, 40, 95, ["water", "dark"]], "噴火駝": [70, 100, 70, 105, 75, 40, ["fire", "ground"]],
    "七夕青鳥": [75, 70, 90, 70, 105, 80, ["dragon", "flying"]], "詛咒娃娃": [64, 115, 65, 83, 63, 65, ["ghost", "none"]],
    "阿勃梭魯": [65, 130, 60, 75, 60, 75, ["dark", "none"]], "冰鬼護": [80, 80, 80, 80, 80, 80, ["ice", "none"]],
    "暴飛龍": [95, 135, 80, 110, 80, 100, ["dragon", "flying"]], "巨金怪": [80, 135, 130, 95, 90, 70, ["steel", "psychic"]],
    "拉帝亞斯": [80, 80, 90, 110, 130, 110, ["dragon", "psychic"]], "拉帝歐斯": [80, 90, 80, 130, 110, 110, ["dragon", "psychic"]],
    "烈咬陸鯊": [108, 130, 95, 80, 85, 102, ["dragon", "ground"]], "路卡利歐": [70, 110, 70, 115, 70, 90, ["fighting", "steel"]],
    "暴雪王": [90, 92, 75, 92, 85, 60, ["grass", "ice"]], "艾路雷朵": [68, 125, 65, 65, 115, 80, ["fighting", "psychic"]],
    "差不多娃娃": [103, 60, 86, 60, 86, 50, ["normal", "none"]], "蒂安希": [50, 100, 150, 100, 150, 50, ["rock", "fairy"]],
    "龍頭地鼠": [110, 130, 60, 50, 65, 88, ["ground", "steel"]], "賽富豪": [87, 60, 95, 133, 91, 84, ["steel", "ghost"]],
    "水伊布": [130, 65, 60, 110, 95, 65, ["water", "none"]], "冰伊布": [65, 60, 110, 130, 95, 65, ["ice", "none"]]
    # ... 這裡可依需求繼續擴展到 236 隻 ...
}

Move = {
    "熱風": ["s", "fire", 95], "爆炸烈焰": ["s", "fire", 150], "日光束": ["s", "grass", 120], 
    "近身戰": ["p", "fighting", 120], "暴風": ["s", "flying", 110], "大字爆炎": ["s", "fire", 110],
    "地震": ["p", "ground", 100], "流星群": ["s", "dragon", 130], "加農水炮": ["s", "water", 150],
    "冷凍乾燥": ["s", "ice", 70], "千箭齊發": ["p", "ground", 90], "歸無之光": ["s", "dragon", 200],"冰凍光束": ["s", "ice", 90]
}

Item = [
    "無", "絲綢圍巾", "黑帶", "銳利鳥嘴", "毒針", "柔軟沙子", "硬石頭", "銀粉", "詛咒之符", "金屬膜", "木炭", 
    "神秘水滴", "奇跡種子", "磁鐵", "彎曲的湯匙", "不融冰", "龍之牙", "黑色眼鏡", "妖精之羽", "生命寶珠", 
    "達人帶", "力量頭帶", "博識眼鏡", "突擊背心", "一般寶石"
]

nature_effects = {
    "怕寂寞 (Lonely):攻擊↑ 防禦↓": ("A", "B"),"固執 (Adamant):攻擊↑ 特攻↓": ("A", "C"),"頑皮 (Naughty):攻擊↑ 特防↓": ("A", "D"),"勇敢 (Brave):攻擊↑ 速度↓": ("A", "S"), 
    "大膽 (Bold):防禦↑ 攻擊↓": ("B", "A"),"淘氣 (Impish):防禦↑ 特攻↓": ("B", "C"),"樂天 (Lax):防禦↑ 特防↓": ("B", "D"),"悠閒 (Relaxed):防禦↑ 速度↓": ("B", "S"),
    "內斂 (Modest):特攻↑ 攻擊↓": ("C", "A"), "慢吞吞 (Mild):特攻↑ 防禦↓": ("C", "B"),"馬虎 (Rash):特攻↑ 特防↓": ("C", "D"),"冷靜 (Quiet):特攻↑ 速度↓": ("C", "S"),
    "溫和 (Calm):特防↑ 攻擊↓": ("D", "A"), "溫順 (Gentle):特防↑ 防禦↓": ("D", "B"),"慎重 (Careful):特防↑ 特攻↓": ("D", "C"),"自大 (Sassy):特防↑ 速度↓": ("D", "S"),
    "膽小 (Timid):速度↑ 攻擊↓": ("S", "A"), "急躁 (Hasty):速度↑ 防禦↓": ("S", "B"),"爽朗 (Jolly):速度↑ 特攻↓": ("S", "C"), "天真 (Naive):速度↑ 特防↓": ("S", "D"),
    "不變": ("-", "-")
}

# --- 3. Streamlit 介面 ---

st.set_page_config(page_title="Pokémon ZA 傷害計算器", layout="wide")
st.title("⚔️ Pokémon ZA 傷害計算器")

st.sidebar.header("⚙️ 詳細數值設定")

def get_stats_input(prefix):
    st.sidebar.subheader(f"{prefix}方設定")
    selected_nature = st.sidebar.selectbox(f"{prefix}性格", list(nature_effects.keys()), key=f"nat_{prefix}")
    n_mod = {"A":1.0, "B":1.0, "C":1.0, "D":1.0, "S":1.0}
    up, down = nature_effects[selected_nature]
    if up != "-": n_mod[up] = 1.1
    if down != "-": n_mod[down] = 0.9
    
    col_iv, col_ev = st.sidebar.columns(2)
    ivs = {k: col_iv.number_input(f"{k} 個體", 0, 31, 31, key=f"iv_{prefix}_{k}") for k in ["H", "A", "B", "C", "D", "S"]}
    evs = {k: col_ev.number_input(f"{k} 努力", 0, 252, 0, key=f"ev_{prefix}_{k}") for k in ["H", "A", "B", "C", "D", "S"]}
    
    # 新增：能力階級調整選單 (-1, 0, +1)
    st.sidebar.write(f"📈 {prefix}能力階級 (HP除外)")
    stages = {}
    col1, col2 = st.sidebar.columns(2)
    for i, k in enumerate(["A", "B", "C", "D", "S"]):
        target_col = col1 if i % 2 == 0 else col2
        stages[k] = target_col.selectbox(f"{k} 階級", [-1, 0, 1], index=1, key=f"stage_{prefix}_{k}")
        
    return ivs, evs, n_mod, stages

iv_atk, ev_atk, n_atk, stage_atk = get_stats_input("攻擊")
iv_def, ev_def, n_def, stage_def = get_stats_input("防守")

LvAtk = 50
LvDef = 50

# --- UI 配置 ---
c1, c2 = st.columns(2)
with c1:
    pa = st.selectbox("選擇攻擊方寶可夢", list(pokemon.keys()))
    item1 = st.selectbox("攻擊方道具", Item)
    move_name = st.selectbox("選擇招式", list(Move.keys()))
    criticlehit = st.checkbox("擊中要害 (Crit)")
    Plus = st.checkbox("是否要Plus (C+)?")
    atk_buff_active = st.checkbox("🔥 攻擊力 Buff (額外 2 倍)")

with c2:
    pd = st.selectbox("選擇防守方寶可夢", list(pokemon.keys()))
    item2 = st.selectbox("防守方道具", Item)
    Reflection = st.checkbox("反射壁 (物理減半)")
    Lightscreen = st.checkbox("光牆 (特殊減半)")
    is_burn = st.checkbox("攻擊方處於灼傷狀態")
    def_buff_active = st.checkbox("🛡️ 防禦力 Buff (額外 2 倍)")

# 計算基礎能力值 (包含性格修正)
def calc_stat(base, iv, ev, lv, nature_mod, is_hp=False):
    if is_hp:
        return int((((math.floor(base*2+iv+(ev/4)))*lv)/100)+10+lv)
    else:
        return int(((((math.floor(base*2+iv+(ev/4)))*lv)/100)+5)*nature_mod)

# 能力階級轉倍率
def get_stage_multiplier(stage):
    if stage == 1: return 1.5
    if stage == -1: return 2/3
    return 1.0

abAtk = {k: calc_stat(pokemon[pa][i], iv_atk[k], ev_atk[k], LvAtk, n_atk.get(k, 1), k=="H") for i, k in enumerate(["H", "A", "B", "C", "D", "S"])}
abAtk["Type"] = pokemon[pa][6]

abDef = {k: calc_stat(pokemon[pd][i], iv_def[k], ev_def[k], LvDef, n_def.get(k, 1), k=="H") for i, k in enumerate(["H", "A", "B", "C", "D", "S"])}
abDef["Type"] = pokemon[pd][6]

if st.button("🔮 執行計算", use_container_width=True):
    move = Move[move_name]
    
    # 最終倍率整合 = 勾選Buff(2x) * 階級修正(1.5x 或 2/3x)
    # 攻擊方
    m_atk = (2 if atk_buff_active else 1) * get_stage_multiplier(stage_atk["A" if move[0]=="p" else "C"])
    # 防守方
    m_def = (2 if def_buff_active else 1) * get_stage_multiplier(stage_def["B" if move[0]=="p" else "D"])
    
    if move[0] == "s":
        listdamage = Spower(move[2], abAtk["C"], abDef["D"], m_atk, m_def, criticlehit, Lightscreen, abAtk["Type"], move[1], abDef["Type"], is_burn, False, False, Plus, move_name)
    else:
        listdamage = Ppower(move[2], abAtk["A"], abDef["B"], m_atk, m_def, criticlehit, Reflection, abAtk["Type"], move[1], abDef["Type"], is_burn, False, False, Plus, move_name)

    # 結果輸出
    st.divider()
    permin = listdamage[0]/abDef["H"]
    permax = listdamage[1]/abDef["H"]
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.subheader(f"📊 傷害結果: {pa} vs {pd}")
        st.metric("造成傷害區間", f"{listdamage[0]} ~ {listdamage[1]}")
        st.write(f"對手總 HP: {abDef['H']}")
    
    with col_res2:
        st.subheader("📉 削血比例")
        st.progress(min(permax, 1.0))
        st.write(f"傷害百分比: **{permin:.1%} ~ {permax:.1%}**")

    # 擊殺判定
    if permin >= 1:
        st.success("🏆 確定一擊擊倒 (確一)")
    elif permin < 1 and permax >= 1:
        killper = (listdamage[1]-abDef["H"])/(listdamage[1]-listdamage[0]) if listdamage[1] != listdamage[0] else 1.0
        st.warning(f"🎲 亂數一擊擊倒 (擊殺率: {killper:.1%})")
    elif permin >= 0.5:
        st.info("🎯 確定二擊擊倒 (確二)")
    elif permax >= 0.5:
        st.info("⚖️ 亂數二擊擊倒 (亂二)")
    elif permin>0 and permax>0:
        st.error("📉 傷害不足 (不夠痛)")
    else:
        st.error("X 無效!!!!!")

    with st.expander("查看實際能力面板 (Lv.50)"):
        st.write("攻擊方:", abAtk)
        st.write("防守方:", abDef)


    
