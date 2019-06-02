# -*- coding: utf-8 -*-
"""
A car is on a one-dimensional track, positioned between two "mountains". 
The goal is to drive up the mountain on the right; however, the car's engine is not strong enough to scale the mountain in a single pass. 
Therefore, the only way to succeed is to drive back and forth to build up momentum.
"""
import gym

env = gym.make("MountainCar-v0")
state = env.reset()

done = False
while not done:
    action = 2  #Move right
    new_state, reward, done, _ = env.step(action)
    env.render()
    print(reward, new_state, done)

env.close()