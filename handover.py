# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:17:07 2021

@author: Andi5
"""
import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import datetime

st.set_page_config(page_title='텍스트마이닝을 활용한 금리예측',  layout='wide', page_icon=':💸:')

#this is the header
 

t1, t2 = st.columns((0.07,1)) 

t1.image('images/index1.png', width = 100)
t2.title("텍스트 마이닝을 활용한 금리예측")


## Data

with st.spinner('Updating Report...'):
    
    # Date input for filtering
    sdt = st.date_input(
        "조회 시작일을 선택해 주세요",
        datetime.datetime(2024, 1, 1)
    )

    edt = st.date_input(
        "조회 종료일을 선택해 주세요",
        datetime.datetime(2024, 1, 1)
    )

    # Reading the CSV file
     # CSV 파일 읽기
       # CSV 파일 읽기
    news = pd.read_csv('newscallrate.csv')

    # 날짜 필터링
    news['date'] = pd.to_datetime(news['date'])
    filtered_news = news[(news['date'] >= pd.to_datetime(sdt)) & (news['date'] <= pd.to_datetime(edt))]

    # 날짜를 문자열로 변환하여 날짜만 포함
    filtered_news['date'] = filtered_news['date'].dt.strftime('%Y-%m-%d')

    # 메트릭 계산 및 표시
    m1, m2, m3, m4, m5 = st.columns((1, 1, 1, 1, 1))
    total_articles = filtered_news.shape[0]
    avg_call_rate = filtered_news['call_rate'].mean()
    max_call_rate = filtered_news['call_rate'].max()
    min_call_rate = filtered_news['call_rate'].min()
    
    m1.metric("Total Articles", total_articles)
    m2.metric("Average Call Rate", f"{avg_call_rate:.2f}")
    m3.metric("Max Call Rate", f"{max_call_rate:.2f}")
    m4.metric("Min Call Rate", f"{min_call_rate:.2f}")

    # 두 개의 열을 생성하여 데이터프레임과 그래프를 나란히 표시
    col1, col2 = st.columns(2)

    # 필터링된 데이터프레임 표시
    with col1:
        st.dataframe(filtered_news)

    # 날짜별 call_rate 그래프 생성 및 시각화
    with col2:
        fig = px.line(filtered_news, x='date', y='call_rate', title='날짜별 콜금리', labels={'date': '날짜', 'call_rate': 'callrate'})
        fig.update_layout(margin=dict(l=0, r=10, b=10, t=30))
        st.plotly_chart(fig, use_container_width=True)
    # Predicted Number of Arrivals
    
    