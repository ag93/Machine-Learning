# -*- coding: utf-8 -*-
"""
Q-Learning on the MountainCar-v0 Environment
"""

import gym
import numpy as np
env = gym.make('MountainCar-v0')
env.reset()

print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space)

#Normalize the values to reduce the size of the Q-Table
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE #Calculating the size of window for every step

print(discrete_os_win_size)

q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n])) #Initializing the Q-Table of size 20x20x3
print(q_table.shape)
    