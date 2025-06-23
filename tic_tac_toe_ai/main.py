import streamlit as st
import numpy as np
import pickle
from env import TicTacToe
from agent_model import Agent


with open("policy_p1.pkl", "rb") as f:
    q_values = pickle.load(f)


st.set_page_config(page_title="Tic Tac Toe AI", layout="centered")
st.title(" Tic Tac Toe: Play Against AI")


def symbol_to_emoji(val):
    if val == 1:
        return "❌"  
    elif val == -1:
        return "⭕"  
    else:
        return " "


if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.turn = 1  
    st.session_state.game = TicTacToe()
    st.session_state.game.board = st.session_state.board
    st.session_state.isEnd = False


st.markdown("You're ❌. AI is ⭕. Click a box to make your move!")


cols = st.columns(3)
for i in range(3):
    for j in range(3):
        cell_val = st.session_state.board[i][j]
        if cell_val == 0 and not st.session_state.isEnd:
            if cols[j].button(" ", key=f"{i}-{j}"):
                if st.session_state.turn == 1:
                    st.session_state.board[i][j] = 1
                    st.session_state.game.board = st.session_state.board
                    st.session_state.turn = -1
        else:
            cols[j].write(f"**{symbol_to_emoji(cell_val)}**")

    cols = st.columns(3)


if st.session_state.turn == -1 and not st.session_state.isEnd:
    state_hash = st.session_state.game.getHash()
    available = st.session_state.game.availablePositions()

    max_val = -999
    best_action = None

    for action in available:
        next_board = st.session_state.board.copy()
        next_board[action] = -1
        next_hash = str(next_board.reshape(9))
        val = q_values.get(next_hash, 0)
        if val >= max_val:
            max_val = val
            best_action = action

    if best_action:
        st.session_state.board[best_action] = -1
        st.session_state.game.board = st.session_state.board
        st.session_state.turn = 1

# Check winner
winner = st.session_state.game.winner()
if winner is not None and not st.session_state.isEnd:
    st.session_state.isEnd = True
    if winner == 1:
        st.success(" You win!")
    elif winner == -1:
        st.error(" AI wins!")
    else:
        st.info("It's a draw!")

# Restart button
if st.button("Play Again"):
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.turn = 1
    st.session_state.isEnd = False
    st.session_state.game = TicTacToe()
    st.session_state.game.board = st.session_state.board
