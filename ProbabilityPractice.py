from numpy import random
random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0}
totalPurchases = 0
for _ in range(100000):
    ageGroup = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = 0.4
    totals[ageGroup] += 1
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageGroup] += 1
PEF = float(purchases[30]) / float(totals[30])
print("P(purchase | 30s): " + str(PEF))
PE = float(totalPurchases) / 100000.0
print("P(Purchase):" + str(PE))
