import streamlit as st

st.set_page_config(
page_title="MBTI 음악 스타일 추천",
page_icon="🎵",
layout="centered"
)

st.title("🎵 MBTI 음악 스타일 추천기")
st.write("MBTI를 선택하면 너와 잘 어울리는 음악 스타일을 추천해줄게! 😎")

music_data = {
"INTJ": [
{
"genre": "🎻 클래식",
"personality": "깊이 생각하는 걸 좋아하고, 차분하게 집중하는 사람에게 잘 어울려!"
},
{
"genre": "🌌 앰비언트",
"personality": "혼자만의 시간을 즐기고 상상력이 풍부한 사람에게 추천!"
}
],
"INTP": [
{
"genre": "🎹 재즈",
"personality": "호기심이 많고 새로운 아이디어를 탐구하는 사람에게 딱!"
},
{
"genre": "🎧 로파이",
"personality": "편안한 분위기에서 공부하거나 생각 정리하는 걸 좋아하는 사람!"
}
],
"ENTJ": [
{
"genre": "⚡ EDM",
"personality": "에너지가 넘치고 목표를 향해 달려가는 사람에게 추천!"
},
{
"genre": "🔥 힙합",
"personality": "자신감이 넘치고 리더십이 강한 사람과 잘 맞아."
}
],
"ENTP": [
{
"genre": "🎸 얼터너티브 록",
"personality": "개성이 강하고 새로운 도전을 즐기는 사람에게 추천!"
},
{
"genre": "🎤 랩",
"personality": "재치 있고 창의적인 생각을 많이 하는 사람에게 잘 어울려."
}
],
"INFJ": [
{
"genre": "🌙 인디 발라드",
"personality": "감성이 풍부하고 깊은 생각을 자주 하는 사람에게 추천!"
},
{
"genre": "🎻 뉴에이지",
"personality": "평화로운 분위기와 감성적인 음악을 좋아하는 사람!"
}
],
"INFP": [
{
"genre": "🌸 인디 음악",
"personality": "상상력이 풍부하고 감수성이 뛰어난 사람에게 딱!"
},
{
"genre": "🎼 어쿠스틱",
"personality": "따뜻하고 편안한 분위기를 좋아하는 사람에게 추천!"
}
],
"ENFJ": [
{
"genre": "💖 R&B",
"personality": "감정을 잘 표현하고 공감 능력이 높은 사람에게 잘 맞아."
},
{
"genre": "🎤 팝",
"personality": "사람들과 함께 즐기는 걸 좋아하는 사람에게 추천!"
}
],
"ENFP": [
{
"genre": "🌈 K-POP",
"personality": "밝고 긍정적인 에너지가 넘치는 사람에게 딱!"
},
{
"genre": "🎉 댄스 팝",
"personality": "신나는 분위기와 새로운 경험을 좋아하는 사람!"
}
],
"ISTJ": [
{
"genre": "🎼 클래식",
"personality": "성실하고 꼼꼼하며 집중력이 높은 사람에게 추천!"
},
{
"genre": "🎹 피아노 연주곡",
"personality": "차분하고 안정적인 분위기를 좋아하는 사람!"
}
],
"ISFJ": [
{
"genre": "💝 발라드",
"personality": "따뜻한 마음을 가지고 있고 배려심이 많은 사람에게 추천!"
},
{
"genre": "🎻 OST",
"personality": "추억과 감성을 소중하게 생각하는 사람에게 잘 맞아."
}
],
"ESTJ": [
{
"genre": "🥁 팝 록",
"personality": "활동적이고 추진력이 강한 사람에게 추천!"
},
{
"genre": "⚡ EDM",
"personality": "목표를 향해 힘차게 나아가는 사람에게 잘 어울려."
}
],
"ESFJ": [
{
"genre": "🎤 K-POP",
"personality": "친구들과 함께 즐기는 걸 좋아하는 사람에게 추천!"
},
{
"genre": "💃 댄스 음악",
"personality": "밝고 긍정적인 에너지를 가진 사람에게 딱!"
}
],
"ISTP": [
{
"genre": "🎸 록",
"personality": "독립적이고 자유로운 성향을 가진 사람에게 추천!"
},
{
"genre": "🏍️ 메탈",
"personality": "도전 정신이 강하고 강렬한 분위기를 좋아하는 사람!"
}
],
"ISFP": [
{
"genre": "🎨 인디 팝",
"personality": "예술적 감각이 뛰어나고 감성이 풍부한 사람에게 추천!"
},
{
"genre": "🌅 어쿠스틱",
"personality": "편안하고 따뜻한 분위기를 좋아하는 사람에게 딱!"
}
],
"ESTP": [
{
"genre": "🔥 힙합",
"personality": "자신감 넘치고 활동적인 사람에게 추천!"
},
{
"genre": "🎉 EDM",
"personality": "신나는 분위기와 에너지를 즐기는 사람에게 잘 맞아."
}
],
"ESFP": [
{
"genre": "🕺 댄스 팝",
"personality": "흥이 많고 사람들과 어울리는 걸 좋아하는 사람에게 추천!"
},
{
"genre": "🎤 K-POP",
"personality": "밝고 즐거운 분위기를 좋아하는 사람에게 딱!"
}
]
}

selected_mbti = st.selectbox(
"✨ MBTI를 선택해줘!",
list(music_data.keys())
)

if st.button("🎧 음악 추천 받기"):
st.success(f"{selected_mbti} 유형에게 추천하는 음악 스타일이야! 🎶")

```
for idx, music in enumerate(music_data[selected_mbti], start=1):
    st.markdown(f"## {idx}. {music['genre']}")
    st.markdown(
        f"😊 **이런 성격의 사람에게 추천!**\n\n{music['personality']}"
    )
    st.divider()

st.balloons()
```

st.caption("🎵 음악 취향은 사람마다 다를 수 있어! 재미로 참고해보자 😄")
