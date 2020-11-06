import gym
import numpy as np
import sys

def new_reset(env,state=None):
    env.reset()
    if state is not None:
        env.env.s = state


def learn(gamma,k=99):
    env = gym.make('Taxi-v3')

    state_size=env.observation_space.n
    action_size=env.action_space.n
    value_func=np.zeros(state_size)
    action_table=checkEnv(env)
    np.set_printoptions(threshold=sys.maxsize)



def checkEnv(env):
    state_size = env.observation_space.n
    action_size = env.action_space.n
    action_table=[[0 for x in range(action_size)] for y in range(state_size)]
    for state in range (state_size):
        for action in range(action_size):
            new_reset(env,state)
            next_state, reward, done,info=env.step(action)
            action_table[state][action]= (next_state,reward,done)
    return action_table

def simulate(env,policy_arr):
    env.reset()
    env.render()
    done = False
    iter = 0
    reward = 0
    while (not done and iter < 30):
        iter += 1
        state = env.s
        next_state, r, done, info = env.step(int(policy_arr[state]))
        reward += r
        env.render()

    print(f"the total reward for this run is: {reward}")

def print_check_state(value_arr):
    sum=0
    for state in range(len(value_arr)):
        print(f"[{state}]: {value_arr[state]}")
        sum+=value_arr[state]
    print(f"average value: {sum/500} ")
