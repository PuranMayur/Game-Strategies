"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def payoff_matrix(na,nb, i=0, j=0, k=0):

    payoff_matrix = [[[0, 0, 0], [.7, 0, .3], [5/11, 0, 6/11]],
                    [[.3, 0, .7], [1/3, 1/3, 1/3], [.3, .5, .2]],
                    [[6/11, 0, 5/11], [.2, .5, .3], [.1, .8, .1]]]

    payoff_matrix[0][0][0] = nb/(na+nb)
    payoff_matrix[0][0][2] = na/(na+nb)

    return payoff_matrix[i][j][k]

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

# Problem 3b
def optimal_strategy(na, nb, tot_rounds):
    """
    Calculate the optimal strategy for Alice maximize her points in the future rounds
    given the current score of Alice(na) and Bob(nb) and the total number of rounds(tot_rounds).
    
    Return the answer in form of a list [p1, p2, p3],
    where p1 is the probability of playing Attacking
    p2 is the probability of playing Balanced
    p3 is the probability of playing Defensive
    """
    dp = [[0 for i in range(tot_rounds*2+1)] for j in range(tot_rounds*2+1)]
    
    c = tot_rounds*2-1
    while c>=0:
        i = 0
        j = c
        while i<tot_rounds*2:
            a = b = c = 0
            if i+2 <= tot_rounds*2:
                a = (dp[i+2][j] + 1)*(payoff_matrix(0,0,0,0,0) + payoff_matrix(0,0,0,1,0) + payoff_matrix(0,0,0,2,0))/3
            if i+1 <= tot_rounds*2 and j+1 <= tot_rounds*2:
                b = (dp[i+1][j+1] + 0.5)*(payoff_matrix(i/2, j/2, 0) + payoff_matrix(i/2, j/2, 1) + payoff_matrix(i/2, j/2, 2))/3
            if j+2 <= tot_rounds*2:
                c = (dp[i][j+2] + 0)*(payoff_matrix(i/2, j/2, 0) + payoff_matrix(i/2, j/2, 1) + payoff_matrix(i/2, j/2, 2))/3
            
            dp[i][j] = max(a, b, c)
            j -= 1
            i += 1
        c -= 1

def expected_points(tot_rounds):
    """
    Given the total number of rounds(tot_rounds), calculate the expected points that Alice can score after the tot_rounds,
    assuming that Alice plays optimally.

    Return : The expected points that Alice can score after the tot_rounds.
    """
    
    pass

print(optimal_strategy(2,2,5))

#By Puran Mayur
#2023MT10366