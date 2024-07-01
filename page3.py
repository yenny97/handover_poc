import streamlit as st
import pandas as pd
import pyperclip

def about_page():
    st.title("💰금리 예측 챗봇_소개")
    st.write("✔️뉴스 기사를 첨부하면, 금리 인상인지 금리 인하인지 예측하는 챗봇입니다.")
    st.write("✔️뉴스 페이지에서 한 개의 기사를 복사해서 챗봇에 넣어주시기 바랍니다.")
    st.write("✔️챗봇 작동 원리: 저희는 금리 상승 사전과 하락 사전을 만들었습니다. (한국은행 의사록, 뉴스기사, 채권 보고서를 기반으로 만들어진 사전입니다.) 뉴스 기사를 토큰화와 n그램을 하여, 뉴스 기사에 나오는 단어들이 금리 상승 사전에 나오는 단어가 더 많으면, 금리 상승이 예측된다는 결과를 냅니다. 금리 하락 사전에 나오는 단어가 더 많으면, 금리 하락이 예측된다는 결과를 냅니다.")

def chatbot_page():
    st.title("금리 인상, 인하 예측")

    # 세션 상태에서 메시지 히스토리 초기화
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 초기 인사 메시지 표시
    if not st.session_state.messages:
        with st.chat_message("assistant"):
            st.write("안녕하세요👋 금리를 예측하고 싶은 기사 본문을 붙여 넣어주세요!")

    # 앱이 다시 실행될 때 채팅 메시지 히스토리를 표시
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # 사용자 입력을 위한 텍스트 입력 박스
    prompt = st.chat_input("금리를 예측하고 싶은 기사 본문을 붙여 넣어주세요.")
    if prompt:
        # 사용자 메시지를 세션 상태에 추가
        st.session_state.messages.append({"role": "user", "content": prompt})

        # 사용자 입력 메시지 표시
        with st.chat_message("user"):
            st.write(prompt)
        
        # 금리 예측 메시지를 세션 상태에 추가 및 표시
        prediction_message = "입력하신 기사를 분석하고 금리를 예측 중입니다... 현재 금리 상승률 O%, 금리 하락률 O%로 예측됩니다."
        st.session_state.messages.append({"role": "assistant", "content": prediction_message})
        
        with st.chat_message("assistant"):
            st.write(prediction_message)

        # 새로운 입력을 유도하는 메시지 추가
        new_prompt_message = "금리를 예측하고 싶은 기사 본문을 붙여 넣어주세요!"
        st.session_state.messages.append({"role": "assistant", "content": new_prompt_message})
        
        with st.chat_message("assistant"):
            st.write(new_prompt_message)

def news_page():
    st.title("뉴스 기사")

    # 뉴스 기사 A
    article_a = """더 혹독한 금리 고통이 기다린다=문제는 금리 인상이 이제 막 시작이라는 점이다. 은행 대출 상품의 금리는 금융채, 자금조달지수(코픽스)에 따라 움직인다. 금융채는 한미 중앙은행의 금리 인상 기대 심리 및 전 세계 채권금리와 연동되는데, 25일 이주열 한국은행 총재가 내년 초 추가 금리 인상을 시사하고 미국도 긴축 속도를 빠르게 가져갈 것으로 보여 상승할 가능성이 높다. 한은 기준금리는 내년에 1.75%까지 오를 것이라는 전망도 있다. 코픽스는 시중금리, 은행의 예금 금리와 같이 움직인다. 최근 금융 당국이 은행의 예금 금리가 너무 낮다는 점을 공개적으로 지적해 앞으로 예금 금리가 오르면 코픽스 역시 올라 대출금리를 밀어올리게 된다."""
    
    st.subheader("뉴스 기사 A")
    st.write(article_a)
    
    # 뉴스 기사 B
    article_b = """우에다 가즈오(가운데) 일본은행 총재가 지난달 7일 도쿄 총리 관저에서 기시다 후미오 총리와 만난 뒤 기자들에게 발언하고 있다. (사진=연합뉴스/EPA)27일 외신 등에 따르면 일본 은행은 지난 23일 올해 첫 금융정책결정회의에서 단기금리를 -0.1%, 장기금리를 '10년물 국채금리 0% 정도'로 유지한다고 발표했다. YCC 정책도 '장기 국채금리 상단 1%를 목표로 하는 수준'으로 유지하기로 했다. 물가안정을 목표로 필요한 시점까지 양적·질적 금융완화정책을 이어갈 계획도 유지했다. 다만, 이 같은 회의 결과에도 일본 은행의 금융정책 정상화 의지는 여전하다는 분석이 나온다. 우에다 가즈오 일본 은행 총재가 기자회견을 통해 궁극적으로 금융정책을 정상화하고자 하는 의지를 나타내서다. 금융정책 정상화 부작용이 나타날 수 있으나 목표로 했던 물가상승률에 도달하면 조치에 나서겠다는 표현도 사용했다. 최보원 한국투자증권 연구원은 "우에다 총재는 실질 임금이 당장 마이너스여도 플러스로 전환될 가능성이 보이면 대응에 나설 수 있다는 견해를 드러냈다"며 "1월 경제·물가 전망 리포트와 기자회견에서 물가상승률 2% 실현 가능성을 기존보다 크게 평가하는 단어를 사용했다는 점에서도 금융정책 정상화 의지를 확인할 수 있었다"고 설명했다. 이에 최 연구원은 일본 은행의 연중 금융정책 정상화 가능성이 여전히 크다고 판단했다. 그는 "이달 일본 은행 회의에선 완화적인 조치가 유지됐으나 오는 4월 정책 변경 가능성을 여전히 크게 평가한다"며 "3~4월은 일본 중소기업 임금 인상 상황 보고와 대부분의 일본 기업 회계 연도가 마무리되는 시기이기 때문"이라고 설명했다. 또 4월엔 전망 리포트도 함께 공개되는 만큼 정책을 변경할 수 있는 명분도 확보할 수 있다는 게 최 연구원의 의견이다. 일본 자민당 파벌 해체 등 정치적 이슈로 3월 일본 은행 회의 전에도 정상화 가능성에 대한 경계는 높아지겠으나 우에다 총재가 4월에는 참고할 수 있는 정보가 많다는 표현을 사용했다는 점에 더욱 주목했다. (표=한국투자증권)최 연구원은 일본 은행의 연중 금융정책 정상화 가능성이 큰 만큼 일본 정부 차원에서 발표되는 정책과 예상보다 더딜 엔·달러 환율 하락 속도에 대응하는 전략이 필요하다고 판단했다. 또 현재 닛케이 지수가 12개월 선행 주가수익비율(12MF PER)이 20배를 넘어선 만큼 단기 되돌림이 나타날 가능성에 유의할 필요가 있다는 점도 강조했다. 우선 최 연구원은 신소액투자 비과세 제도(NISA) 정책에 주목했다. 이는 예금에만 집중된 자금을 주식 시장으로 유입하기 위해 비과세 제도를 강화한 정책이다. 최 연구원은 "신 NISA 정책이 도입되면 배당주가 재평가될 것으로 예상한다"며 "대표적인 기업으로는 대형은행·통신·상사 등이 있다"고 말했다. 그는 이어 "금융정책 정상화 부담을 상쇄하고 공급망 재편에 대응하기 위해 친기업 정책도 이어지고 있어 반도체·소재·장비 기업도 주목받을 전망"이라며 "엔·달러 환율이 하락하는 시기엔 은행·식품·내수주가 재평가받을 수 있다"고 말했다."""
    
    st.subheader("뉴스 기사 B")
    st.write(article_b)

    # 클립보드에 복사하는 함수
    def copy_to_clipboard(text):
        pyperclip.copy(text)
        st.success("뉴스 기사가 클립보드에 복사되었습니다!")

    # 버튼 클릭 시 클립보드에 복사
    if st.button("뉴스 기사 A 복사하기"):
        copy_to_clipboard(article_a)
    
    if st.button("뉴스 기사 B 복사하기"):
        copy_to_clipboard(article_b)

# 페이지 딕셔너리
PAGES = {
    "✅소개 페이지": about_page,
    "📰뉴스 페이지": news_page,
    "🤖챗봇 페이지": chatbot_page
}

def main():
    st.sidebar.title("메뉴")
    selection = st.sidebar.selectbox("페이지를 선택하세요", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()

