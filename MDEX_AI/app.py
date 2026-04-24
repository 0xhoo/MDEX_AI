import streamlit as st
import requests
from database import MEME_DATA

st.set_page_config(page_title="MDEX-AI", page_icon="🚀")

st.title("🚀 MDEX-AI: 지능형 밈 검색기")
st.write("궁금한 상황을 입력하면 어울리는 밈을 추천해드립니다.")

# 검색 입력
query = st.text_input(
    "궁금한 밈이나 상황을 입력하세요 (예: 집 가고 싶을 때):"
)

# AI 추천 버튼
if st.button("AI에게 물어보기"):
    if query:
        with st.spinner("AI가 밈을 분석 중입니다..."):
            try:
                response = requests.get(
                    f"http://127.0.0.1:8000/memes/ai-search?q={query}"
                )
                data = response.json()

                result = data.get("ai_recommendation")

                if result:
                    st.success("추천 결과")
                    st.info(result)
                else:
                    st.error("결과를 가져오지 못했습니다.")
                    st.write(data)

            except Exception as e:
                st.error(f"서버 연결 오류: {e}")
    else:
        st.warning("질문을 입력해주세요!")

st.divider()

# 밈 목록 보기 섹션
st.subheader("📚 밈 목록 보기")

# 카테고리 목록 생성
category_list = ["전체"] + sorted(
    list(set([m["category"] for m in MEME_DATA]))
)

selected_category = st.selectbox(
    "카테고리를 선택하세요",
    category_list
)

# 카테고리별 필터링
if selected_category == "전체":
    filtered_memes = MEME_DATA
else:
    filtered_memes = [
        meme for meme in MEME_DATA
        if meme["category"] == selected_category
    ]

st.write(f"총 {len(filtered_memes)}개의 밈이 있습니다.")

# 밈 목록 출력
for meme in filtered_memes:
    with st.expander(f"{meme['name']}"):
        st.write(f"**카테고리:** {meme['category']}")
        st.write(f"**설명:** {meme['description']}")