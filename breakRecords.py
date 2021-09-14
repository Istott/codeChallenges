# record basketh games scores and compare to previous games.
# we want a value for number of games
# value for score of the game (which is the value that is being passed in)
# we want to store the highest score and the lowest score
# and we want a count for everytime she breaks a low or high score

def breakRecords(gameScore):
    gameObj = {
        'gameNum': 0,
        'scoreCard': [],
        'highScore': 0,
        'lowScore': 0,
        'highCounter': 0,
        'lowCounter': 0,
    }

    for x in gameScore:
        if gameObj['gameNum'] == 0:
            gameObj['gameNum'] += 1
            gameObj['scoreCard'].append(x)
            gameObj['highScore'] = x
            gameObj['lowScore'] = x
        elif x > gameObj['highScore']:
            gameObj['gameNum'] += 1
            gameObj['scoreCard'].append(x)
            gameObj['highScore'] = x
            gameObj['highCounter'] += 1
        elif x < gameObj['lowScore']:
            gameObj['gameNum'] += 1
            gameObj['scoreCard'].append(x)
            gameObj['lowScore'] = x
            gameObj['lowCounter'] += 1
        else:
            gameObj['gameNum'] += 1
            gameObj['scoreCard'].append(x)

    return gameObj      


games = [12,3,345,35,5,7,1,7,6,65,5,8000,90000,-1]
game1 = 4

print(breakRecords(games))