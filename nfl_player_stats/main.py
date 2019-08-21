import nflgame


if __name__ == '__main__':
    print('enter main')
    games = nflgame.games(2018, week=1)
    plays = nflgame.combine_plays(games)
    for p in plays.sort('passing_yds').limit(5):
        print(p)