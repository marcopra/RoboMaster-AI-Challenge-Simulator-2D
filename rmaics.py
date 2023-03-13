# -*- coding: utf-8 -*-
# RoboMaster AI Challenge Simulator (RMAICS)

from kernel import kernel
import gym
from gym import spaces
import numpy as np

class rmaics(gym.Env):

    def __init__(self, agent_num, render=True):
        super(rmaics, self).__init__()
        self.game = kernel(car_num=agent_num, render=render)
        self.g_map = self.game.get_map()
        self.memory = []

        # Creation of the upper and the lower bound for the custom gym environment (in this case `rmaics`)
        low = np.array([-1, -1, -1, -1, 0, 0, 0, 0])
        high= np.array([1, 1, 1, 1, 1, 1, 1, 1])
        low_bound = np.array([-1, -1, -1, -1, 0, 0, 0, 0])
        high_bound = np.array([1, 1, 1, 1, 1, 1, 1, 1])

        for _ in range(agent_num - 1):
            low_bound = np.vstack((low_bound, low))
            high_bound = np.vstack((high_bound, high))
                   

        self.action_space = spaces.Box(low = low_bound, high= high_bound, shape = (agent_num, 8), dtype=np.float32)


        # The observation space MUST be changed accordingly to the personalized observation

        low = np.array([0, 0, 0, -180, -90, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0])
        high = np.array([1, 800, 500, 180, 90, np.inf, 2000, 600, 1, 1, np.inf, 1000, np.inf , np.inf , np.inf])
        low_bound= np.array([0, 0, 0, -180, -90, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0])
        high_bound = np.array([1, 800, 500, 180, 90, np.inf, 2000, 600, 1, 1, np.inf, 1000, np.inf , np.inf , np.inf])

        for _ in range(agent_num - 1):
            low_bound = np.vstack((low_bound, low))
            high_bound = np.vstack((high_bound, high))

        
        self.observation_space = spaces.Box(low = low_bound, high= high_bound, shape = (agent_num, 15), dtype= np.float32)

    def reset(self):
        self.state = self.game.reset()
        # state, object
        self.obs = self.get_observation(self.state)
        
        return self.obs

    def step(self, actions):
        state = self.game.step(actions)
        obs = self.get_observation(state)
        rewards = self.get_reward(state)

        self.memory.append([self.obs, actions, rewards])
        self.state = state

        info = {}
        return obs, rewards, state.done, info
    
    def get_observation(self, state):

        time, events, compet_info, done, detect, vision = state.get_params()
    
        # personalize your observation here
        # Temporary observation set -> remeber to modify self.observation_space when changing the observations here
        obs = events
        return obs
    
    def get_reward(self, state):
        # personalize your reward here
        rewards = 0
        return rewards

    def play(self):
        self.game.play()

    def save_record(self, file):
        self.game.save_record(file)