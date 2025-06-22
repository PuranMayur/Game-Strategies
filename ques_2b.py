import numpy as np
import random

payoff_matrix = [[[0, 0, 0], [.7, 0, .3], [5/11, 0, 6/11]],
                [[.3, 0, .7], [1/3, 1/3, 1/3], [.3, .5, .2]],
                [[6/11, 0, 5/11], [.2, .5, .3], [.1, .8, .1]]]

class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1
        self.bob_points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        #Implementing Alice's moves
        if self.results[-1] == 1:
            if ((self.bob_points/(self.points+self.bob_points)) > (6/11)):
                return 0
            else:
                return 2
        elif self.results[-1] == 0.5:
            return 0
        else:
            return 1
        pass
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.results = np.append(self.results, result)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.points += result
        self.bob_points += 1-result
        pass

class Bob:
    def __init__(self):
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """ 
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.results = np.append(self.results, result)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.points += result


def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.

    Args:
        alice: An instance of Alice class.
        bob: An instance of Bob class.
        payoff_matrix: The matrix of probabilities for each strategy combination.
    
    Returns:
        None
    """
    # Alice and Bob decide their play styles
    alice_move = alice.play_move()
    bob_move = bob.play_move()

    # Get the probabilities from the payoff matrix
    if alice_move == 0 and bob_move == 0:  # if both attack
        nA = alice.points
        nB = bob.points
        p_alice_win, p_draw, p_bob_win = [nB/(nA+nB), 0, nA/(nA+nB)]
    else:
        p_alice_win, p_draw, p_bob_win = payoff_matrix[alice_move][bob_move]

    # Simulate the result of the round
    outcome = random.choices(['Alice win', 'Draw', 'Bob win'], 
                             [p_alice_win, p_draw, p_bob_win])[0]

    # Update results based on the outcome
    if outcome == 'Alice win':
        alice.observe_result(alice_move, bob_move, 1)
        bob.observe_result(bob_move, alice_move, 0)
    elif outcome == 'Draw':
        alice.observe_result(alice_move, bob_move, 0.5)
        bob.observe_result(bob_move, alice_move, 0.5)
    else:
        alice.observe_result(alice_move, bob_move, 0)
        bob.observe_result(bob_move, alice_move, 1)

    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Args:
        num_rounds: Number of rounds to simulate.
    
    Returns:
        None
    """
    alice = Alice()
    bob = Bob()
    
    for _ in range(num_rounds):
        simulate_round(alice, bob, payoff_matrix)

# Running Monte Carlo simulation with 10^5 rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10**5)

#By Puran Mayur
#2023MT1066