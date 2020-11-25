import taxi_policy as tp
import gym
import numpy as np

env = gym.make('Taxi-v3')
env.reset()
action_table = tp.checkEnv(env)

value_arr = np.zeros(500)
policy_arr = np.random.randint(0, 6, 500)
gamma = 0.95
for iter in range(99):
    prev_policy_arr = np.copy(policy_arr)
    for i in range(0, 500):    ### value iteration
        act = -1
        max_v = np.NINF

        for j in range(0, 6):
            next_state, reward, done = action_table[i][j]
            if (max_v < value_arr[next_state] + reward):
                max_v = value_arr[next_state] + reward  # found V(s') best
                act = j

        next_state, reward, done = action_table[i][act]
        if not done:
            value_arr[i] = reward + (gamma * value_arr[next_state])
        else:
            value_arr[i] = 20

    for i in range(0, 500):  ### policy iteration
        act = -1
        max_v = np.NINF
        for j in range(0, 6):
            next_state, reward, done = action_table[i][j]
            if (max_v < value_arr[next_state] + reward):
                max_v = value_arr[next_state]
                act = j
        policy_arr[i] = act
    if (np.array_equal(policy_arr, prev_policy_arr)):  # Reached optimal policy
        print("stoped learning", iter)
        break

tp.simulate(env, policy_arr)
tp.print_check_state(value_arr)

# print("policy array:\n" , policy_arr)
# print("value array:\n" , value_arr)
