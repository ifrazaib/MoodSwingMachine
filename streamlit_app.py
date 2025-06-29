import streamlit as st
import random

st.set_page_config(page_title="😂 Mood Swing Machine", page_icon="🎭")
st.title("🎭 Mood Swing Machine")
st.markdown("Welcome to the most unpredictable app you'll ever use!")

moods = ["😄 Happy", "😢 Sad", "😡 Angry", "😴 Sleepy", "🤪 Crazy", "🤖 Robot Mode"]
mood = st.selectbox("What's your current vibe?", moods)

jokes = {
    "😄 Happy": [
        "You're so bright, even the sun wears shades around you 😎",
        "Happiness is contagious—stay away, I’m not insured!"
    ],
    "😢 Sad": [
        "Don't cry... even onions feel bad when you cry 😢",
        "If life gives you lemons, squirt them back in its eye!"
    ],
    "😡 Angry": [
        "Take a deep breath... now scream into a pillow. Feel better? No? Good. 😂",
        "Smash something! (Preferably the like button 👍)"
    ],
    "😴 Sleepy": [
        "Coffee won’t help. But dreaming about coffee might ☕💤",
        "Nap hard, nap proud 💤💪"
    ],
    "🤪 Crazy": [
        "You clicked this on purpose, didn't you? Seek help. 😂",
        "Bananas called. They want their crazy back 🍌"
    ],
    "🤖 Robot Mode": [
        "Beep boop. Emotions not found. Restarting... 🤖",
        "00101010010 = 'You're awesome' in binary!"
    ]
}

gifs = {
    "😄 Happy": "https://media.giphy.com/media/3orieUXfR0ytJz8zIY/giphy.gif",
    "😢 Sad": "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif",
    "😡 Angry": "https://media.giphy.com/media/11tTNkNy1SdXGg/giphy.gif",
    "😴 Sleepy": "https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif",
    "🤪 Crazy": "https://media.giphy.com/media/3ohs7KViF7YBqsrxt6/giphy.gif",
    "🤖 Robot Mode": "https://media.giphy.com/media/3oEjHOEqD9G4F3kXZu/giphy.gif"
}

if 'history' not in st.session_state:
    st.session_state.history = []

if mood:
    st.subheader("💬 Here's something for your mood:")
    st.image(gifs[mood], width=300)
    st.info(random.choice(jokes[mood]))
    st.session_state.history.append(mood)

if st.button("🎲 Give me a surprise mood"):
    surprise = random.choice(moods)
    st.toast("Mood upgraded! 🎉", icon="🎭")
    st.success(f"🎉 Surprise! You're now feeling {surprise}")
    st.image(gifs[surprise], width=300)
    st.success(random.choice(jokes[surprise]))
    st.session_state.history.append(surprise)

st.sidebar.title("📜 Mood Memory")
if st.session_state.history:
    st.sidebar.write("You've felt:")
    st.sidebar.write(", ".join(st.session_state.history))
else:
    st.sidebar.write("No moods recorded yet.")
