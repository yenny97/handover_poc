import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import altair as alt
def run_page():
    st.title("텍스트마이닝을 활용한 금리예측")
    
    # 데이터 로딩
    news = pd.read_csv('newscallrate_content.csv')
    news['date'] = pd.to_datetime(news['date'])
    
    # 날짜 필터링을 위한 입력
    sdt = st.date_input("조회 시작일을 선택해 주세요", datetime.datetime(2024, 1, 1))
    edt = st.date_input("조회 종료일을 선택해 주세요", datetime.datetime(2024, 1, 1))

    # 날짜 필터링 및 데이터프레임 표시
    filtered_news = news[(news['date'] >= pd.to_datetime(sdt)) & (news['date'] <= pd.to_datetime(edt))]
    filtered_news['date'] = filtered_news['date'].dt.strftime('%Y-%m-%d')

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
    # 데이터 로드
    pos = pd.read_csv('posdic.csv')
    neg = pd.read_csv('negdic.csv')
    tone = pd.read_csv('tone_rate_df1.csv')

    # 컬럼 나누기
    col1, col2 = st.columns(2)
    col1.dataframe(pos) 
    col2.dataframe(neg) 

    # 날짜 형식으로 변환
    tone['date'] = pd.to_datetime(tone['date'])

    # 왼쪽 축 (doc_tone) 차트
    doc_tone_chart = alt.Chart(tone).mark_line(color='red').encode(
        x=alt.X('date:T', axis=alt.Axis(title='date')),
        y=alt.Y('doc_tone:Q', axis=alt.Axis(title='minutes_tone', titleColor='black'))
    )

    # 오른쪽 축 (base_rate) 차트
    base_rate_chart = alt.Chart(tone).mark_line(color='blue').encode(
        x=alt.X('date:T', axis=alt.Axis(title='date')),
        y=alt.Y('base_rate:Q', axis=alt.Axis(title='base_rate', titleColor='black'))
    ).transform_calculate(
        base_rate_scaled="datum.base_rate * 1"  # 기본적으로 오른쪽 축으로 스케일 변환
    )

    # 차트 결합
    combined_chart = alt.layer(
        doc_tone_chart, base_rate_chart
    ).resolve_scale(
        y='independent'  # y 축을 독립적으로 유지
    ).properties(
        width=800,
        height=400,
        title='금통위 의사록 어조와 기준금리'
    )

    # Streamlit에 차트 표시
    st.altair_chart(combined_chart, use_container_width=True)
    