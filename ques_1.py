"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

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

# Problem 1a
def calc_prob(alice_wins, bob_wins):

    T = alice_wins + bob_wins
    dp = [[0 for i in range(T+1)] for j in range(T+1)]
    dp[1][1] = 1 #Base case for recursion
    for i in range(2, T+1): #Filling the first row of the dp matrix
        dp[i][1] = mod_multiply(dp[i-1][1], mod_divide(1,(i))) 
    for j in range(2, T+1): #Filling the first column of the dp matrix
        dp[1][j] = mod_multiply(dp[1][j-1], mod_divide(1,(j)))
    for i in range(2, T+1): 
        for j in range(2, T+1):
            dp[i][j] = mod_add(mod_multiply(dp[i-1][j], mod_divide(j,(i+j-1))), mod_multiply(dp[i][j-1], mod_divide(i, (i+j-1)))) #Recursive formula for rest of the elements
    return dp[alice_wins][bob_wins]
    pass
    
# Problem 1b (Expectation)      
def calc_expectation(t):
    
    T = t 
    dp = [[0 for i in range(T+1)] for j in range(T+1)]
    dp[0][1] = 0
    dp[1][1] = 1
    for i in range(2, T+1):
        dp[i][1] = mod_multiply(dp[i-1][1], mod_divide(1,(i)))
    for j in range(2, T+1):
        dp[1][j] = mod_multiply(dp[1][j-1], mod_divide(1,(j)))
    for i in range(2, T+1):
        for j in range(2, T+1):
            dp[i][j] = mod_add(mod_multiply(dp[i-1][j], mod_divide(j,(i+j-1))), mod_multiply(dp[i][j-1], mod_divide(i, (i+j-1)))) 
            
    exp = 0
    for i in range (1, t+1):
        exp = mod_add(exp, mod_multiply(dp[i][t-i], (mod_multiply(2,i)-t))) #Calculating the expectation from the derived formula
    return exp
    pass

# Problem 1b (Variance)
def calc_variance(t):

    T = t 
    
    dp = [[0 for i in range(T+1)] for j in range(T+1)]
    dp[0][1] = 0
    dp[1][1] = 1
    for i in range(2, T+1):
        dp[i][1] = mod_multiply(dp[i-1][1], mod_divide(1,(i)))
    for j in range(2, T+1):
        dp[1][j] = mod_multiply(dp[1][j-1], mod_divide(1,(j)))
    for i in range(2, T+1):
        for j in range(2, T+1):
            dp[i][j] = mod_add(mod_multiply(dp[i-1][j], mod_divide(j,(i+j-1))), mod_multiply(dp[i][j-1], mod_divide(i, (i+j-1))))
    
    var = 0
    for i in range (1, t+1):
        var = mod_add(var, mod_multiply(dp[i][t-i], mod_multiply((mod_multiply(2,i)-t), (mod_multiply(2,i)-t)))) #Calculating the variance from the derived formula
    return var
    
#By Puran Mayur
#2023MT1066