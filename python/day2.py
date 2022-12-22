import util

outcome_score = {
    'win': 6,
    'lose': 0,
    'draw': 3
}

move_score = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

guide_move = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

def get_score_outcome(turn: list[str]) -> int:
    if turn == '':
        return 0
    turn_ary = turn.split(' ')
    their_move = guide_move[turn_ary[0]]
    my_move = guide_move[turn_ary[1]]

    outcome = None
    if their_move == my_move:
        outcome = 'draw'
    else:
        if my_move == 'rock':
            if their_move == 'scissors':
                outcome = 'win'
            elif their_move == 'paper':
                outcome = 'lose'
        elif my_move == 'paper':
            if their_move == 'scissors':
                outcome = 'lose'
            elif their_move == 'rock':
                outcome = 'win'
        elif my_move == 'scissors':
            if their_move == 'paper':
                outcome = 'win'
            elif their_move == 'rock':
                outcome = 'lose'

    return move_score[my_move] + outcome_score[outcome]


lines = util.get_day_input(2)
score = sum([get_score_outcome(turn) for turn in lines])
print(score)
