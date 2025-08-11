import streamlit as st
from utility.llm import get_response   # GPT 호출을 위해 우리가 제작한 라이브러리. prompt 등이 포함됨.

APP_TITLE = "Chatbot"

# ─────────────────────────────────────────
# 대화 기록 저장 및 새로운 대화 생성 함수
# ─────────────────────────────────────────
# 이전 메시지 저장해 두는 함수
if "messages" not in st.session_state:
    st.session_state.messages = []

# 새로운 메시지 시작 함수 
def reset_chat():
    st.session_state.messages = []


# ─────────────────────────────────────────
# UI
# ─────────────────────────────────────────

st.title(APP_TITLE)

# 새로운 대화
_, btn_col = st.columns([3, 1])
with btn_col:
    st.button("새 대화", on_click=reset_chat, use_container_width=True)

# 기존 메시지 렌더링 (Streamlit 예시와 동일)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"]) 

# 질문 입력창
prompt = st.chat_input("질문")

# 사용자 메시지 저장 및 표시
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 모델 응답 호출 
    try:
        assistant_text = get_response(prompt)
    except TypeError:
        assistant_text = "질문을 잘 이해하지 못했어요. 다시 입력해 주세요."

    # 어시스턴트 메시지 저장/표시
    with st.chat_message("assistant"):
        st.markdown(assistant_text)
    st.session_state.messages.append({"role": "assistant", "content": assistant_text})
