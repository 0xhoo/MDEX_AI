# database.py

MEME_DATA = [
    # ㄱ
    {"id": 1, "category": "ㄱ", "name": "곽철용 밈", "description": "묻고 더블로가!, 마포대교는 무너졌냐?, 젊은 친구, 신사답게 행동해"},
    {"id": 2, "category": "ㄱ", "name": "꽁꽁 얼어붙은 한강 위로 고양이가 걸어다닙니다", "description": "뉴스 나레이션의 묘한 리듬감과 귀여운 영상으로 인기를 끈 챌린지성 밈"},
    {"id": 3, "category": "ㄱ", "name": "그런데 그것이 실제로 일어났습니다", "description": "루리웹 이벤트 당첨 해명 과정에서 유래된, 말도 안 되는 일이 벌어졌을 때 쓰는 표현"},
    {"id": 4, "category": "ㄱ", "name": "그게 뭔데 씹덕아", "description": "본인들만 아는 주제로 대화할 때나 쓸데없는 정보가 올라올 때 풍자하는 용도"},
    {"id": 5, "category": "ㄱ", "name": "그건 원작을 경험해 보신 분들의 기준인 거고요", "description": "카트라이더 디렉터의 발언으로, 유저와의 괴리를 나타낼 때 쓰임"},

    # ㄴ
    {"id": 6, "category": "ㄴ", "name": "뉴진스의 하입보이요", "description": "무슨 노래 듣냐는 질문에 뜬금없이 답변하며 춤을 추는 밈"},
    {"id": 7, "category": "ㄴ", "name": "나는 이 이야기를 무척 좋아한다", "description": "죽은 반려동물이 마중 나온다는 감동적인 이야기에서 유래된 문구"},
    {"id": 8, "category": "ㄴ", "name": "나 사람 됐다 짱이지", "description": "웹툰 '마루는 강쥐'에서 강아지가 사람이 된 후 자랑하는 귀여운 장면"},

    # ㄷ
    {"id": 9, "category": "ㄷ", "name": "7호선 단소 살인마", "description": "지하철에서 단소를 휘두르며 난동을 부린 사건에서 유래"},
    {"id": 10, "category": "ㄷ", "name": "다 해줬잖아", "description": "메이플스토리 '신창섭' AI 노래 가사 중 하나로, 정상화 밈의 핵심 문구"},
    {"id": 11, "category": "ㄷ", "name": "돌리랑 도트가 제일 좋아", "description": "월드 오브 워크래프트에 등장하는 중독성 있는 노래"},
    {"id": 12, "category": "ㄷ", "name": "너 때문에 흥이 다 깨져버렸으니까 책임져", "description": "만화로 보는 그리스 로마 신화의 디오니소스 명대사"},

    # ㄹ
    {"id": 13, "category": "ㄹ", "name": "라고 할 뻔", "description": "하고 싶은 말을 다 하고 마지막에 붙여서 책임을 회피하거나 상대를 약 올리는 드립"},
    {"id": 14, "category": "ㄹ", "name": "러시아식 유머", "description": "A가 B를 합니다가 아닌 '러시아에서는 B가 A를 합니다' 식의 주객전도 유머"},

    # ㅁ
    {"id": 15, "category": "ㅁ", "name": "마라탕후루", "description": "마라탕과 탕후루를 합친 신조어 및 틱톡 챌린지 노래"},
    {"id": 16, "category": "ㅁ", "name": "미룬이 사태", "description": "개그맨 이제규의 '나는 미룬이니까' 발언에서 유래된 상황"},
    {"id": 17, "category": "ㅁ", "name": "무대를 뒤집어 놓으셨다", "description": "가수 박미경의 리액션에서 유래된 극찬 혹은 풍자적 표현"},

    # ㅂ
    {"id": 18, "category": "ㅂ", "name": "불 좀 꺼줄래?", "description": "페이커의 광고 대사 '불 좀 꺼줄래? 내 램 좀 보게'에서 유래"},
    {"id": 19, "category": "ㅂ", "name": "빅맥송", "description": "맥도날드 광고 CM송 가사 전체 (참깨빵 위에 순 쇠고기...)"},
    {"id": 20, "category": "ㅂ", "name": "빵꾸똥꾸", "description": "지붕뚫고 하이킥 정해리의 유행어"},

    # ㅅ
    {"id": 21, "category": "ㅅ", "name": "사랑했나봐(윤도현)", "description": "곰돌이 푸 댄스 영상에 합성되어 유행한 중독성 있는 밈"},
    {"id": 22, "category": "ㅅ", "name": "슈슉 슈숙 시발럼아", "description": "제주도 돌하르방 사진과 함께 유행한 거친 리듬감의 텍스트 밈"},
    {"id": 23, "category": "ㅅ", "name": "시그마(Sigma)", "description": "고독하지만 자기 주관이 뚜렷하고 멋진 상태를 나타내는 표정과 밈"},
    {"id": 24, "category": "ㅅ", "name": "신창섭", "description": "메이플스토리 디렉터를 신격화하거나 풍자하는 AI 노래 및 영상 시리즈"},

    # ㅇ
    {"id": 25, "category": "ㅇ", "name": "아임뚜렛", "description": "투렛 증후군 연기 논란으로 커진 사건과 그에 따른 풍자"},
    {"id": 26, "category": "ㅇ", "name": "안아줘요", "description": "부드라미 캐릭터가 팔을 벌리고 있는 귀여운 이미지와 문구"},
    {"id": 27, "category": "ㅇ", "name": "오징어 게임 깐부", "description": "우리는 깐부잖아, 네 거 내 거가 없는 거야"},

    # ㅈ
    {"id": 28, "category": "ㅈ", "name": "작은 하마 이야기", "description": "누구든 작은 하마를 건드리면 아주 X되는 거야"},
    {"id": 29, "category": "ㅈ", "name": "장충동왕족발보쌈", "description": "말왕의 중독성 있는 CM송 낭독에서 시작된 밈"},

    # ㅌ
    {"id": 30, "category": "ㅌ", "name": "티라미수 케익", "description": "헌터X헌터 곤 프릭스 댄스와 함께 유행한 노래 밈"},
    {"id": 31, "category": "ㅌ", "name": "탈룰라", "description": "의도치 않게 패드립을 쳤을 때 급히 태세를 전환하는 상황"},

    # ㅍ
    {"id": 32, "category": "ㅍ", "name": "포기하면 편해", "description": "슬램덩크 안한수 감독 대사 왜곡 밈"},
    {"id": 33, "category": "ㅍ", "name": "판사님 저는 웃지 않았습니다", "description": "위험한 유머를 보고 고소당할까 봐 방어적으로 쓰는 댓글"},
    {"id": 34, "category": "ㅍ", "name": "폼 미쳤다", "description": "어떤 대상의 실력이 대단할 때 쓰는 극찬 드립"},

    # ㅎ
    {"id": 35, "category": "ㅎ", "name": "ㅎㅎ즐거우세요?", "description": "방시혁의 메시지에서 유래된 비꼬거나 질문하는 용도의 밈"},
    {"id": 36, "category": "ㅎ", "name": "하지만 빨랐죠", "description": "결과는 엉망이지만 속도만큼은 빨랐을 때 자조적으로 쓰는 말"},

    # 외국어 및 기타
    {"id": 37, "category": "외국어", "name": "I am 신뢰에요", "description": "전청조 사기 사건 카톡에서 유래된 보노보노식 영어 섞어 쓰기"},
    {"id": 38, "category": "외국어", "name": "Young한데? 완전 MZ인데요?", "description": "억지로 젊은 세대 문화를 맞추려는 기성세대를 풍자하는 밈"},
    {"id": 39, "category": "숫자나 특수문자", "name": "11미터 모형탑 훈련", "description": "인간이 가장 공포를 느낀다는 11미터, 제가 직접 한번 해보겠습니다"}
]