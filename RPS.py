# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    history_len = len(opponent_history)

    guess = "R"

    if history_len > 2:
      next_moves = []
      
      for i in range(len(opponent_history)):
        if opponent_history[i] == prev_play:
          if i + 1 < history_len and opponent_history[i-1] == opponent_history[-2] and opponent_history[i-2] == opponent_history[-3]:
            next_moves.append(opponent_history[i+1])

      max_move = ["R", next_moves.count("R")]
      for m in next_moves:
        if m == max_move[0]:
          continue
        m_count = next_moves.count(m)
        if m_count > max_move[1]:
          max_move[0] = m
          max_move[1] = m_count
          guess = m
    
    return counter_move(guess)



def counter_move(move):
  return {
    "R": "P",
    "P": "S",
    "S": "R"
  }[move]


