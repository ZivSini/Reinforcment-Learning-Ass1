import gym
import numpy as np
env = gym.make('Taxi-v3')
env.reset()
env.render()

# state = env.encode(0,2,0,0)
# env.s = state
i , j ,p, d = env.decode(env.s)
print("i:", i,"j:",j,"pass:",p,"dest:",d)
print("state: ",env.s)
print(env.P)



value_arr = np.zeros(500)
policy_arr = np.zeros(500)
p_arr = list(env.P.items())
new_p_arr=[]
for i in range (500):
    new_p_arr.append(p_arr[i][1])
p_arr=new_p_arr
actions_arr=[]
for iter in range(20):
    prev_policy_arr = np.copy(policy_arr)

    for i in range(0,500):
        max_v = np.NINF
        actions_arr = list(p_arr[i].items())
        new_actions_arr = []
        for ii in range(6):
            new_actions_arr.append(actions_arr[ii][1])
        actions_arr = new_actions_arr

        for j in range(0,6):
            # action = list(actions_arr.items())
            a, b, val, d = actions_arr[j][0]
            if(max_v < val):
                max_v = val

        value_arr[i] += 0.99 * max_v

    for i in range(0,500):
        act = -1
        max_v = np.NINF
        actions_arr = list(p_arr[i].items())
        new_actions_arr = []
        for iii in range(6):
            new_actions_arr.append(actions_arr[iii][1])
        actions_arr = new_actions_arr
        for j in range(0,6):
            a, b, val, d = actions_arr[j][0]
            if (max_v < val):
                max_v = val
                act = j

        policy_arr[i] = act
print("policy array:",policy_arr)
print("value array:",value_arr)
    # if(np.equal(policy_arr,prev_policy_arr)):
    #     break



# state = env.encode(0, 0, 0, 0) # (taxi row, taxi column, passenger index, destination index)
# print("State:", state)

# p_arr = np.zeros(500)
# env.decode(state)



# for i in range(100):
#     env.step(env.action_space.sample())
#
#     env.render()

# if __name__ == '__main__':


# import gym
# # import taxi env
# from gym.envs.toy_text import taxi
# # import tabular q agent
# import Policy_Iteration_Agent
#
# env = taxi.TaxiEnv()  # make TaxiEnv
#
# agent = Policy_Iteration_Agent.PolicyIterationAgent(env.observation_space, env.action_space)
#
# print("BEGIN THE POLICY ITERATION")
# for i in range(5):
#     agent.learn(env, i + 1)  # learn best choices and act on the env i=1 on first iteration
#     print("trial number: %d" % i)
#
# agent.LogUpdate()