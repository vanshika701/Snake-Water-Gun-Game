import streamlit as st
import random

st.title("🐍 Snake - Water - Gun Game")

# Choices dictionary
userdict = {"Snake": -1, "Water": 0, "Gun": 1}
revdict = {-1: "Snake", 0: "Water", 1: "Gun"}

# Streamlit select box for user input
user_choice = st.selectbox("Choose your option:", ["Snake", "Water", "Gun"])

# Play button
if st.button("Play"):
    computer_choice = random.choice([-1, 0, 1])
    you = userdict[user_choice]

    st.write(f"### 🤖 Computer Chose: `{revdict[computer_choice]}`")
    st.write(f"### 🙋 You Chose: `{revdict[you]}`")

    # Determine the winner
    if you == computer_choice:
        st.success("It's a Tie!")
    elif (you == 1 and computer_choice == -1) or \
         (you == -1 and computer_choice == 0) or \
         (you == 0 and computer_choice == 1):
        st.balloons()
        st.success("🎉 You Win!")
    else:
        st.error("😞 You Lose!")
