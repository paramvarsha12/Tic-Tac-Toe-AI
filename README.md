# Tic-Tac-Toe-AI
Play against an AI which uses Q-learning that learns optimal moves over time (reinforced learning)

---
![](https://github.com/paramvarsha12/Tic-Tac-Toe-AI/blob/972d6175a7cf47f75c31e88722e832f8a7dba97a/image.png
)
![](https://github.com/paramvarsha12/Tic-Tac-Toe-AI/blob/972d6175a7cf47f75c31e88722e832f8a7dba97a/aiwinsimage.png)

# Working
1. This is a Tic Tac Toe game where you can play against a smart AI opponent trained using Reinforcement Learning (specifically Q-Learning).

2. The AI learns how to play by playing thousands of games against itself, it explores moves, receives rewards for winning, and penalties for losing.

3. The game board is a 3x3 NumPy array, and every board configuration becomes a “state” that the AI stores and assigns a Q-value (how good that state is for it)

4. Over time, the AI updates these Q values using an equation which i will provide at the bottom of the ReadMe file

5. Once trained, the AI stops exploring and only exploits the best moves using its Q-table (saved in .pkl files)

---
1. Train the AI Agent : python train.py

2. Run the code : streamlit run main.py



###  Clone the Repository
```bash
https://github.com/paramvarsha12/Tic-Tac-Toe-AI.git


