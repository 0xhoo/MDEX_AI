# ai_engine.py

import os
from dotenv import load_dotenv
from groq import Groq
from database import MEME_DATA

# .env 불러오기
load_dotenv()

# API KEY 불러오기
api_key = os.getenv("GROQ_API_KEY")


def get_meme_recommendation(user_input: str):
    try:
        client = Groq(api_key=api_key)

        # 밈 데이터 문자열로 변환
        context = "\n".join(
            [
                f"- {m['name']}: {m['description']}"
                for m in MEME_DATA
            ]
        )

        prompt = f"""
너는 대한민국 인터넷 밈 전문가야.

사용자의 질문 의도를 파악해서
아래 [밈 데이터] 중에서 가장 잘 어울리는 밈 1개를 추천해줘.

반드시 아래 형식으로만 답변해:

추천 밈: [밈 이름]
이유: [짧고 재미있게 설명]

[밈 데이터]
{context}

사용자 질문:
{user_input}
"""

        response = client.chat.completions.create(
            # 기존 llama3-8b-8192 → 서비스 종료됨
            # 최신 안정 모델로 변경
            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.7,
            max_tokens=512
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI 추천 생성 중 오류 발생: {str(e)}"