import streamlit as st

math_works = [
    {"title": "A Beautiful Mind", "type": "영화", "genre": "드라마", "topic": "수학자 전기"},
    {"title": "The Imitation Game", "type": "영화", "genre": "역사 드라마", "topic": "암호학"},
    {"title": "Hidden Figures", "type": "영화", "genre": "드라마", "topic": "여성과 수학"},
    {"title": "Good Will Hunting", "type": "영화", "genre": "드라마", "topic": "천재성 / 교육"},
    {"title": "Fermat's Last Theorem", "type": "책", "genre": "논픽션", "topic": "정리의 역사"},
    {"title": "Flatland", "type": "책", "genre": "공상과학", "topic": "기하학 / 차원"},
    {"title": "The Man Who Knew Infinity", "type": "책", "genre": "전기", "topic": "수학자 전기"},
    {"title": "The Man Who Knew Infinity", "type": "영화", "genre": "전기", "topic": "수학자 전기"},
]

def recommend_math_works(works, preferred_type=None, topic_keyword=None):
    recommendations = []
    for work in works:
        if preferred_type and preferred_type != work["type"]:
            continue
        if topic_keyword and topic_keyword not in work["topic"]:
            continue
        recommendations.append(work["title"])
    return recommendations

st.title("수학 관련 영화 & 책 추천")

preferred_type = st.selectbox("선호하는 형태를 선택하세요:", options=["영화", "책"])
topic_keyword = st.text_input("관심 있는 수학 주제 (예: 전기, 암호학, 교육, 기하학 등)")

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

if st.button("추천 받기"):
    st.session_state.recommendations = recommend_math_works(
        math_works,
        preferred_type=preferred_type,
        topic_keyword=topic_keyword.strip()
    )

if st.session_state.recommendations:
    st.write("### 추천 작품:")
    for title in st.session_state.recommendations:
        st.write(f"- {title}")
else:
    st.write("조건에 맞는 추천 작품이 없습니다. 다른 키워드를 입력해 보세요.")
