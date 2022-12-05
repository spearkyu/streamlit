#라이브러리 import
import requests
import pprint
import json
import pandas as pd
import streamlit as st
import altair as alt
file_path = "C:\\Users\hojin\Desktop\gwajea\python\gimal\simple.txt"
url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=백마로(마두역)&dataTerm=DAILY&pageNo=1&numOfRows=100&returnType=json&serviceKey=E6YZt5LknsrARD2OScTh1asLoxZEksRJ%2BmmqsJr0hvdlXM0RAex8fUJfQqFPNJ9JgUh4UmnP049AaTqXjFuf9w%3D%3D"
image1 = "https://github.com/spearkyu/streamlit/blob/main/dust_v.jpg?raw=true"
image2 = "https://github.com/spearkyu/streamlit/blob/main/o3.png?raw=true"
image3 = "https://github.com/spearkyu/streamlit/blob/main/total.jpg?raw=true"
image4 = "https://github.com/spearkyu/streamlit/blob/main/co.jpg?raw=true"

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
dataframe['dust_v'] = pd.to_numeric(dataframe['pm10Value'])
dataframe['dust_g'] = pd.to_numeric(dataframe['pm10Grade'])
dataframe['co'] = pd.to_numeric(dataframe['coValue'])
dataframe['o3'] = pd.to_numeric(dataframe['o3Value'])
total = dataframe['total']
dust_v = dataframe['dust_v']
dust_g = dataframe['dust_g']
co = dataframe['co']
o3 = dataframe['o3']
# # 바차트 올리기
st.title('공공데이터 시각화')
st.write('공공데이터에 있는 에어코리아 대기오염정보에서 백마로(마두역)의 통합오염수치와 미세먼지농도/지수, 오존농도, 일산화탄소농도를 불러와 자료로 사용했습니다.')
st.write('일산 백마로의 대기오염상태를 시각화하여 실시간으로 상태를 나타내 줍니다.')
st.header("미세먼지농도")
st.bar_chart(dust_v)
st.image(image1)
st.header("미세먼지지수")
st.bar_chart(dust_g)
st.header("오존농도")
st.bar_chart(o3)
st.image(image2)
st.header("일산화탄소농도")
st.bar_chart(co)
st.image(image4)
st.header("통합오염지수")
st.bar_chart(total)
st.image(image3)
