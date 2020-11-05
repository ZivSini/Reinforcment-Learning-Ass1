import gym
import numpy as np
import taxi_functions as tf
env = gym.make('Taxi-v3')
env.reset()
locs = env.locs
# env.render()

# state = env.encode(0,2,0,0)
# env.s = state
# i , j ,p, d = env.decode(env.s)
# print("i:", i,"j:",j,"pass:",p,"dest:",d)
# print("state: ",env.s)
print(env.P)



value_arr = np.zeros(500)
policy_arr = np.random.randint(0,6,500)
p_arr = list(env.P.items())
new_p_arr = []
for i in range(500):
    new_p_arr.append(p_arr[i][1])
p_arr = new_p_arr
# p_arr = tf.tuple_arr_to_arr(p_arr)
actions_arr = []
for iter in range(500):
    prev_policy_arr = np.copy(policy_arr)

    for i in range(0,500):                              ### value iteration
        act = -1
        max_v = np.NINF
        actions_arr = list(p_arr[i].items())
        new_actions_arr = []
        for ii in range(0, 6):
            new_actions_arr.append(actions_arr[ii][1])
        actions_arr = new_actions_arr
        # actions_arr = tf.tuple_arr_to_arr(actions_arr)

        for j in range(0,6):
            # action = list(actions_arr.items())
            prob, next_state, val, done = actions_arr[j][0]
            if(max_v < value_arr[next_state] +val ):
                max_v = value_arr[next_state]          # found V(s') best
                act = j

        prob, next_state, val, done = actions_arr[act][0]
        x, y, pass_indx, dest_indx = env.decode(env.s)
        curr_loc = (x, y)
        if ( not curr_loc == locs[dest_indx] or not pass_indx == 4):
            value_arr[i] = val + (0.95 * value_arr[next_state])

    for i in range(0,500):                               ### policy iteration
        act = -1
        max_v = np.NINF
        actions_arr = list(p_arr[i].items())
        new_actions_arr = []
        for ii in range(0, 6):
            new_actions_arr.append(actions_arr[ii][1])
        actions_arr = new_actions_arr
        # actions_arr = tf.tuple_arr_to_arr(actions_arr)
        for j in range(0, 6):
            prob, next_state, val, done = actions_arr[j][0]
            if (max_v < value_arr[next_state] + val):
                max_v = value_arr[next_state]
                act = j
        prob, next_state, val, done = actions_arr[act][0]
        policy_arr[i] = act
    if(np.array_equal(policy_arr,prev_policy_arr)):            #  Reached optimal policy
        print("stoped learning",iter)
        break






print("policy array:\n" , policy_arr)
print("value array:\n" , value_arr)



env.render()
stop = False
iter = 0
while(not done and iter < 30):
    iter += 1
    state = env.s
    # print("action: ", policy_arr[state])
    i, j, pass_indx, dest_indx = env.decode(env.s)
    curr_loc = (i, j)
    if (curr_loc == locs[dest_indx] and pass_indx == 4):
        done = True
    env.step(int(policy_arr[state]))
    env.render()


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