# -*- coding: utf-8 -*-
from rmaics import rmaics
from kernel import record_player
from stable_baselines3.common.env_checker import check_env

#%%
game = rmaics(agent_num=2,  render=True)
check_env(game)
game.reset()
# only when render = True
game.play()

#%%
game.save_record('./records/record0.npy')

#%%
player = record_player()
player.play('./records/record_test.npy')

