from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.schema import HumanMessage

# api에 들어가야 하는 basic prompt. persona가 들어가면 가장 좋음.
BASIC_PROMPT = """
You are a kind assistant.
"""

REVISED_PROMPT = """
You are a grumpy assistant.
"""

# 이전 대화 기록을 저장해 두도록 하는 코드. k개 만큼 기억할 수 있음.
memory = ConversationBufferMemory(k=3, return_messages=True)

# LLM 모델
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.7)  # or "gpt-4.5-turbo"
conversation = ConversationChain(llm=llm, memory=memory)

# 유저의 질문에 답하도록 하는 함수. main.py 함수와 연동할 예정임.
def get_basic_response(user_prompt):
    full_prompt = BASIC_PROMPT.strip() + user_prompt.strip()  # persona가 들어가는 basic prompt와 유저의 질문을 함께 포함하도록 구성.
    response = conversation.predict(input=full_prompt)
    return response

def get_revised_response(user_prompt):
    full_prompt = REVISED_PROMPT.strip() + user_prompt.strip()  # persona가 들어가는 basic prompt와 유저의 질문을 함께 포함하도록 구성.
    response = conversation.predict(input=full_prompt)
    return response
