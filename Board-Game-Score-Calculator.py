# 【1. 1vs1で勝ち負けのみ】
# winner: 勝者の名前 (str)
# loser: 敗者の名前 (str)

def calculate_score_1(winner, loser):
    scores = {winner: 75, loser: 25}
    return scores

# 【2. 1vs1で得点あり】
# player1: プレイヤー1の名前 (str)
# player2: プレイヤー2の名前 (str)
# score1: プレイヤー1の得点 (int)
# score2: プレイヤー2の得点 (int)

def calculate_score_2(player1, player2, score1, score2):
    total_score = score1 + score2
    if total_score == 0:
        scores = {player1: 50, player2: 50}
    else:
        scores = {player1: score1/total_score*100, player2: score2/total_score*100}
    return scores

# 【3. vs複数人で勝ち負けのみ】
# winners: 勝者の名前のリスト (list)
# losers: 敗者の名前のリスト (list)

def calculate_score_3(winners, losers):
    num_winners = len(winners)
    num_losers = len(losers)
    total_players = num_winners + num_losers
    winner_score = 50 + 50 * (num_losers / total_players)
    loser_score = 50 - 50 * (num_winners / total_players)
    scores = {}
    for winner in winners:
        scores[winner] = winner_score
    for loser in losers:
        scores[loser] = loser_score
    return scores

# 【4. vs複数人で得点あり】
# players: プレイヤー名のリスト (list)
# scores: 各プレイヤーの得点のリスト (list)

def calculate_score_4(players, scores):
    total_score = sum(scores)
    if total_score == 0:
        scores = {player: 100/len(players) for player in players}
    else:        
          scores = {player: score/total_score*100 for player, score in zip(players, scores)}
    return scores
