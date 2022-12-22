import util

outcome_score = {
    'win': 6,
    'draw': 3,
    'lose': 0
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
}

outcome_map = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

move_outcome = {
    'rock': {
        'lose': 'scissors',
        'win': 'paper',
        'draw': 'rock'
    },
    'paper': {
        'lose': 'rock',
        'win': 'scissors',
        'draw': 'paper'
    },
    'scissors': {
        'lose': 'paper',
        'win': 'rock',
        'draw': 'scissors'
    }
}

def get_score_outcome(turn: list[str]) -> int:
    if turn == '':
        return 0
    turn_ary = turn.split(' ')
    their_move = guide_move[turn_ary[0]]
    outcome = outcome_map[turn_ary[1]]
    my_move = move_outcome[their_move][outcome]

    return move_score[my_move] + outcome_score[outcome]


lines = util.get_day_input(2)
score = sum([get_score_outcome(turn) for turn in lines])
print(score)
