# 수학 관련 작품 DB
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

# 추천 함수
def recommend_math_works(works, preferred_type=None, topic_keyword=None):
    recommendations = []
    for work in works:
        if preferred_type and preferred_type not in work["type"]:
            continue
        if topic_keyword and topic_keyword not in work["topic"]:
            continue
        recommendations.append(work["title"])
    return recommendations

# 예시: 추천 사용
preferred_type = input("책 또는 영화 중 어떤 걸 원하시나요? (책/영화): ").strip()
topic_keyword = input("관심 있는 수학 주제를 입력하세요 (예: 전기, 암호학, 교육, 기하학 등): ").strip()

results = recommend_math_works(math_works, preferred_type=preferred_type, topic_keyword=topic_keyword)

# 결과 출력
if results:
    print("\n추천 작품:")
    for title in results:
        print(f" - {title}")
else:
    print("조건에 맞는 추천이 없습니다. 다른 키워드를 시도해보세요.")
