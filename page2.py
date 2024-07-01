import streamlit as st
import base64
# 페이지2 내용 정의
def run_page():
    st.title('Deciphering Monetary Policy Board Minutes through Text Mining Approach: The Case of Korea')


    # PDF 파일을 바이너리 데이터로 읽어옴 (예시용)
    with open("BOK.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # 다운로드 링크를 생성하는 함수
    def download_button(object_to_download, download_filename, button_text):
        """
        Generates a download link for a given object_to_download.
        
        object_to_download (str, bytes): The object to be downloaded.
        download_filename (str): The filename that should be used by default when saving the file.
        button_text (str): Label of the download button.
        """
        if isinstance(object_to_download, str):
            object_to_download = object_to_download.encode()
        b64 = base64.b64encode(object_to_download).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{button_text}</a>'
        return href

    # 다운로드 버튼 생성
    st.markdown(download_button(pdf_bytes, "BOK.pdf", "📁Click here to download PDF"), unsafe_allow_html=True)





# 페이지3 실행
if __name__ == '__main__':
    run_page()


















# 페이지2 실행
if __name__ == '__main__':
    run_page()