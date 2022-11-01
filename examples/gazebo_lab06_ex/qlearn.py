import random
import pickle


class QLearn:
    def __init__(self, actions, epsilon, alpha, gamma):
        self.q = {}             # dictionary
        self.epsilon = epsilon  # exploration constant
        self.alpha = alpha      # discount constant
        self.gamma = gamma      # discount factor
        self.actions = actions

    def loadQ(self, filename):
        '''
        Load the Q state-action values from a pickle file.
        '''
        
        # TODO: Implement loading Q values from pickle file.
        in_pickle =  open(filename+".pickle", "rb")
        self.q = pickle.load(in_pickle)
        in_pickle.close()

        print("Loaded file: {}".format(filename+".pickle"))

    def saveQ(self, filename):
        '''
        Save the Q state-action values in a pickle file.
        '''
        # TODO: Implement saving Q values to pickle and CSV files.
        out_pickle = open(filename+".pickle", "wb")
        pickle.dump(self.q, out_pickle)
        out_pickle.close()

        print("Wrote to file: {}".format(filename+".pickle"))

    def getQ(self, state, action):
        '''
        @brief returns the state, action Q value or 0.0 if the value is 
            missing
        '''
        return self.q.get((state, action), 0.0)

    def chooseAction(self, state, return_q=False):
        '''
        @brief returns a random action epsilon % of the time or the action 
            associated with the largest Q value in (1-epsilon)% of the time
        '''
        # TODO: Implement exploration vs exploitation
        #    if we need to take a random action:
        #       * return a random action
        #    else:
        #       * determine which action has the highest Q value for the state 
        #          we are in.
        #       * address edge cases - what if 2 actions have the same max Q 
        #          value?
        #       * return the action with highest Q value
        #
        # NOTE: if return_q is set to True return (action, q) instead of
        #       just action
        
        action_taken = 0

        if (random.random() >= self.epsilon):
            max_Q = 0
            for action in self.actions:
                if (self.getQ(state, action) > max_Q):
                    action_taken = action
                    max_Q = self.getQ(state, action)
        else:
            action_taken = self.actions[random.randint(0,len(self.actions)-1)]

        if (return_q ==True):
            return(action_taken, self.q)
        else:
            return action_taken

    def learn(self, state1, action1, reward, state2):
        '''
        @brief updates the Q(state,value) dictionary using the bellman update
            equation
        '''
        # TODO: Implement the Bellman update function:
        #     Q(s1, a1) += alpha * [reward + gamma* max(Q(s2)) - Q(s1,a1)]
        # 
        # NOTE: address edge cases: i.e. 
        # 
        # Find Q for current (state1, action1)
        # Address edge cases what do we want to do if the [state, action]
        #       is not in our dictionary?
        # Find max(Q) for state2
        # Update Q for (state1, action1) (use discount factor gamma for future 
        #   rewards)
        curr_Q = self.getQ(state1, action1) 

        qs = [self.getQ(state2, action) for action in self.actions]
        max_Q2=max(qs)
    
        self.q[state1, action1] = curr_Q + self.alpha * (reward + self.gamma* max_Q2 - self.getQ(state1,action1))

    
