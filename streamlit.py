#라이브러리 import
import requests
import pprint
import json
import pandas as pd
import streamlit as st
import altair as alt
file_path = "C:\\Users\hojin\Desktop\gwajea\python\gimal\simple.txt"
url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=백마로(마두역)&dataTerm=DAILY&pageNo=1&numOfRows=100&returnType=json&serviceKey=E6YZt5LknsrARD2OScTh1asLoxZEksRJ%2BmmqsJr0hvdlXM0RAex8fUJfQqFPNJ9JgUh4UmnP049AaTqXjFuf9w%3D%3D"

response = requests.get(url)

contents = response.text

# 데이터 결과값 예쁘게 출력해주는 코드
pp = pprint.PrettyPrinter(indent=4)
# print(pp.pprint(contents))

## json을 DataFrame으로 변환하기 ##

#문자열을 json으로 변경
json_ob = json.loads(contents)
# print(type(json_ob)) #json타입 확인

# 필요한 내용만 꺼내기
body = json_ob['response']['body']['items']
# print(body)

# # Dataframe으로 만들기
dataframe = pd.DataFrame(body)
# # key 값 int으로 만들기
dataframe['total'] = pd.to_numeric(dataframe['khaiValue'])
dataframe['dust'] = pd.to_numeric(dataframe['pm10Value'])
name = dataframe['stationName']
total = dataframe['total']
dust = dataframe['dust']
# # 바차트 올리기
st.title('공공데이터 분석하기')
st.write('한국환경공단_에어코리아_대기오염정보의 통합환경수치와 미세먼지를 불러와 분석을 진행합니다.')
st.write('파주시의 대기 상태를 실시간으로 불러와 시각화 하고있습니다.')
st.header("통합 환경 수치")
st.bar_chart(total)
#st.image(image2)
st.header("미세먼지")
st.bar_chart(dust)
#st.image(image)
