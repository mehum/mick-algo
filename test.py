import random
import numpy as np
import matplotlib.pyplot as plt

# game settings
chance_to_win = 0.5
payout = 2.1

# player settings
no_of_tries = 1000
initial_money = 100
wager = 0.05

money = initial_money

# arrays for plot
bets = np.array([])
moneys = np.array([])
profits = np.array([])

for i in range(no_of_tries):
    bet = money * wager
    money = money - bet
    chance = random.random()
    profit = 100*((money-initial_money)/initial_money)
    moneys = np.append(moneys,money)
    bets = np.append(bets,bet)
    profits = np.append(profits, profit)
    if (chance < chance_to_win):
        money = money + bet * payout
        moneys = np.append(moneys,money)
        bets = np.append(bets,bet)
        profits = np.append(profits, profit)
#     print('Round: {0}    Bet {1:.3f}    Money {2:.3f}'.format(i, bet, money))

plt.plot(profits, label="% Profit")
plt.plot(moneys, label="Money")
plt.plot(bets, label="Bet")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
