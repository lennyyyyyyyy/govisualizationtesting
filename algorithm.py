#filler for actual algorithm that just generates a random distribution

import sente
import random

class Info:
    def __init__(self, pDist, passProb, value):
        # normalize
        sum=passProb
        for row in pDist:
            for val in row:
                sum+=val
        for i in range(19):
            for j in range(19):
                pDist[i][j]/=sum
        passProb/=sum
        self.pDist = pDist
        self.passProb = passProb
        self.value = value
        

def sgEvaluate(board: sente.Board19) -> Info:
    ans = [[0 for _ in range(19)] for _ in range(19)]
    for i in range(20):
        ans[random.randint(0, 18)][random.randint(0, 18)] = random.random()
    return Info(ans, random.random(), random.random())
def adversaryEvaluate(board: sente.Board19) -> Info:
    ans = [[0 for _ in range(19)] for _ in range(19)]
    for i in range(20):
        ans[random.randint(0, 18)][random.randint(0, 18)] = random.random()
    return Info(ans, random.random(), random.random())