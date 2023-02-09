import requests
import json
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Multipage App",
    page_icon="😊",
    layout="wide",
)

st.title("Market_Test")
st.header("웹페이지를 만들어보자")
st.subheader("Streamlit을 활용하기")

# json_token = eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAwODc4NTYifQ.Kz1Q31XCxpow-7vQUhjx8sejfVuQHi0T7BLfVoIXd4LErYMYJZ82oc9PX3Ls19rVxgvnNrwnpu2a2Ctg3vX8qO0214NgAh1Ab8M2hPPEksai7LY2enjhBGu7nvs8Ic9eq43p4DiGlpHQ68zZBbTo1WFbumayIrWkVAD-m7AHbkuguM0pMuXv8qL7ar6ZR-vVUsOetOuAannv6OpFhss3db1n4PuJM6S1TPyo2-Uo6T2FTp5Ue9C8TmIFnj97ZESorEU5KttbZ9qkL8yYnsK1A6glbYQksGMkCS0zQCp87BRQPccKAw41WlybHWcdjU3Zz3iDtMmQ5zv0GI_s0tzEmQ

with st.sidebar :
    st.text_input("Json Key 를 복사 붙여넣기 하세요.",key="json_token")
    if "json_token" not in st.session_state:
         st.session_state["json_token"] = ''
     
       

tab1, tab2, tab3 = st.tabs(['재련재료','배틀아이템','생활'])

def market(option):
    market_name = []
    market_price = []
    dic = {tab1:50000,tab2:60000,tab3:90000}
    headers = {
         'accept': 'application/json',
        'authorization': 'bearer ' + st.session_state["json_token"] ,
        'Content-Type': 'application/json',
        }

    for t in range(1,10) :
        json_data_upload = {
        'Sort': '',
        'CategoryCode': dic[option],
        'CharacterClass': '',
        'ItemTier': 0,
        'ItemGrade': '',
        'ItemName': '' ,
        'PageNo': t,
        'SortCondition': 'ASC',
        }
        try:
            response =requests.post('https://developer-lostark.game.onstove.com/markets/items', headers=headers, json=json_data_upload)
            content = response.json()
            item = json.dumps(content["Items"]).replace("[","").replace("]","").replace("}, {","}${")
          
            for i in range(len(item.split('$'))):
                market_name.append(json.loads(item.split('$')[i])["Name"])
                market_price.append(json.loads(item.split('$')[i])["RecentPrice"])
        except :
            pass
    dataframe = pd.DataFrame({'이름':market_name,'최근 가격':market_price})
    return dataframe

with tab1:
    st.dataframe(market(tab1),width=500)

with tab2:
    st.dataframe(market(tab2),width=500)

with tab3:
    st.dataframe(market(tab1),width=500)

    