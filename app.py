import streamlit as st
import random

st.set_page_config(page_title="AI Content Generator", layout="wide")

# CSS
st.markdown("""
<style>
.main { background-color: #0f172a; color: white; }
.card {
    background: #1e293b;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 15px;
    border: 1px solid #334155;
}
.hash {
    background: #334155;
    padding: 6px 12px;
    border-radius: 20px;
    margin: 4px;
    display: inline-block;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

st.title(" AI Content Generator")
st.write("Generate posts, captions & hashtags instantly")

platform = st.selectbox("Platform", ["Instagram", "Twitter/X", "LinkedIn"])
tone = st.selectbox("Tone", ["Engaging", "Professional", "Funny", "Inspirational", "Casual"])
topic = st.text_input("Enter Topic")

#  Better Content Variations
def generate_posts(topic):
    variations = [
        f"{topic} is changing the game  From automation to smart decision-making, it's everywhere. Are you ready to adapt?",
        f"The rise of {topic} is unstoppable. Businesses, students, and creators — everyone is leveraging it for growth ",
        f"If you're not learning {topic} today, you're already falling behind. The future belongs to those who adapt fast "
    ]
    return random.sample(variations, 3)

def generate_caption(topic):
    captions = [
        f"{topic} is the future ",
        f"Stay ahead with {topic} ",
        f"Level up your skills with {topic} "
    ]
    return random.choice(captions)

def generate_hashtags(topic):
    words = topic.split()
    clean_words = [w.capitalize() for w in words if len(w) > 2]

    base_tags = [f"#{w}" for w in clean_words]

    extra_tags = ["#AI", "#Tech", "#Innovation", "#Future", "#Growth"]
    return base_tags + random.sample(extra_tags, 3)

# Button
if st.button(" Generate Content"):
    if topic == "":
        st.warning("Please enter a topic")
    else:
        with st.spinner("Generating..."):

            posts = generate_posts(topic)
            caption = generate_caption(topic)
            hashtags = generate_hashtags(topic)

        st.markdown("##  Generated Content")

        # Posts
        for i, p in enumerate(posts):
            st.markdown(f'<div class="card"><b>Post {i+1}</b><br>{p}</div>', unsafe_allow_html=True)

        # Caption
        st.markdown(f'<div class="card"><b>Caption</b><br>{caption}</div>', unsafe_allow_html=True)

        # Hashtags
        hash_html = " ".join([f'<span class="hash">{h}</span>' for h in hashtags])
        st.markdown(f'<div class="card"><b>Hashtags</b><br>{hash_html}</div>', unsafe_allow_html=True)

        # Copy section
        st.markdown("###  Copy Content")
        st.code("\n\n".join(posts) + "\n\n" + caption + "\n\n" + " ".join(hashtags))