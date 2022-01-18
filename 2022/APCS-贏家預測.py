class Player:
    def __init__(self, uid, attack, agile):
        self.uid = uid
        self.attack = attack
        self.agile = agile
        self.loss = 0


def cmp(p1: Player, p2: Player):
    if p1.attack * p1.agile >= p2.attack * p2.agile:
        return p1, p2
    else:
        return p2, p1


n, m = map(int, input().split())

attacks = list(map(int, input().split()))
agiles = list(map(int, input().split()))
orders = list(map(int, input().split()))

players = [None]
winners = []
losers = []

for i in range(n):
    player = Player(i + 1, attacks[i], agiles[i])
    players.append(player)

tmps = [None]

for i in range(n):
    order = orders[i]
    tmps.append(players[order])

players = tmps

while len(players) > 2:

    # for x in range(1, len(players)):
    #     p = players[x]
    #     print(p.uid, p.attack, p.agile)
    # print()

    for i in range(1, len(players)-1, 2):
        p1 = players[i]
        p2 = players[i + 1]
        win, loss = cmp(p1, p2)
        win.attack, win.agile, loss.attack, loss.agile = win.attack + loss.attack * loss.agile // (2 * win.agile), \
                                                         win.agile + loss.attack * loss.agile // (2 * win.attack),\
                                                         loss.attack + loss.attack // 2,\
                                                         loss.agile + loss.agile // 2

        loss.loss += 1

        winners.append(win)
        if loss.loss < m:
            losers.append(loss)

    if (len(players) + 1) % 2 == 1:
        winners.append(players[-1])

    players = [None] + winners + losers
    winners = []
    losers = []

print(players[-1].uid)
