
import streamlit as st

# 페이지 설정
st.set_page_config(page_title='텍스트마이닝을 활용한 금리예측', layout='wide', page_icon=':moneybag:')

# 사이드바에서 선택된 페이지에 따라 외부 파일 로드
page = st.sidebar.selectbox(
    '메뉴',
    ['논문구현','논문분석', '논문활용']
)

# 선택된 페이지에 따라 외부 Python 파일 로드 및 실행
if page == '논문분석':
    import page2
    page2.run_page()
elif page == '논문구현':
    import page1
    page1.run_page()
elif page == '논문활용':
    import page3
    page3.main()

    