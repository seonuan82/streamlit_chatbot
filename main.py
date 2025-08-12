import streamlit as st
from utility.llm import get_basic_response, get_revised_response   # GPT 호출을 위해 우리가 제작한 라이브러리. prompt 등이 포함됨.


# ─────────────────────────────────────────
# 대화 기록 저장 및 새로운 대화 생성 함수
# 이전 메시지 저장해 두는 함수
if "messages" not in st.session_state:
    st.session_state.messages = []

# 프롬프트 버전을 저장하는 변수
if "version" not in st.session_state:
    st.session_state.version = 'Default'

# 새로운 메시지 시작 함수
def reset_chat():
    st.session_state.messages = []

# ─────────────────────────────────────────
# UI
st.title("Chatbot")  # 챗봇 상단에 나올 이름.

# 새로운 대화
_, version, button = st.columns([2, 1, 1])   # 한 행 구성 (한 행을 4줄로 나눠서 2줄은 빈칸_으로, 1줄에는 version 정보와 button을 넣기.)
with version:
    st.markdown(st.session_state.version)
with button:
    st.button("새 대화", on_click=reset_chat, use_container_width=True)   # use_container_width : 할당된 공간에 최대한 채우기.

# 기존 메시지 렌더링 (Streamlit 예시와 동일)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 질문 입력창
input = st.chat_input("질문")

# 사용자 메시지 저장 및 표시
if input:
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.markdown(input)

    # API persona 변경하며 output 만들기
    if input == 'password':
      st.session_state.version = 'Revised'
      try:
          assistant_text = get_basic_response(input)
      except TypeError:   # API 오류가 난 경우, default로 출력
          assistant_text = "질문을 잘 이해하지 못했어요. 다시 입력해 주세요."
    else:
      st.session_state.version = 'Default'
      try:
          assistant_text = '새로운 버전의 답변이에요.' + get_revised_response(input)
      except TypeError:   # API 오류가 난 경우, default로 출력
          assistant_text = "질문을 잘 이해하지 못했어요. 다시 입력해 주세요."

    # 어시스턴트 메시지 저장/표시
    with st.chat_message("assistant"):
        st.markdown(assistant_text)
    st.session_state.messages.append({"role": "assistant", "content": assistant_text})
