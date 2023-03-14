# RoboMaster AI Challenge Simulator 2D

RoboMaster AI Challenge Simulator 2D, or `RMAICS` for short, is a simulator designed for participation in the [ICRA 2019 RoboMaster AI Challenge](https://www.robomaster.com/zh-CN/resource/pages/ 980?type=announcementSub), the main purpose of the simulator is to provide a simulation environment for training neural networks for intelligent decision making groups

![demo](./demo.gif)

The game frame rate is around 200fps, but the frame rate for making the gif is only 60fps

## I. Dependencies

numpy

[pygame](https://www.pygame.org/) (useful only for visualisation)

## II. Guidelines for use

### 1. Basic information

The simulator consists of two layers.

> the top-level wrapper class `rmaics`  
> the actual execution class `kernel` at the bottom level

The user needs to define the `get_observation` and `get_reward` functions in the `rmaisc` class to define the observation and reward values; while the `kernel` class is only responsible for the physical environment and the simulation of the referee system. Therefore, when training the network, it is the `rmaisc` class that deals directly with the user

### 2. Content references

Please follow these links to find the content you need

Instructions for using `rmaics`: [rmaics_manual.md](./docs/rmaics_manual.md)

`kernel` usage notes: [kernel_manual.md](./docs/kernel_manual.md)

`record player` usage notes: [record_player.md](./docs/record_player.md)

Control command description: [operation.md](./docs/operation.md)

Parameter format description: [params.md](./docs/params.md)

`kernel` development guide: [develop.md](./docs/develop.md) 

### 3. Other

The original repository is [here](https://github.com/LoveThinkinghard/RoboMaster-AI-Challenge-Simulator-2D).

## III. Other works on this simulator

Here, we list some other works related to this simulator. These can be used as a starting point or a beseline for comparing our work.
Other works:
* [Repo 1](https://github.com/Yazhou-Z/ICRA-simulator): here, it has already been implemented the RL algorithm using [Stable_baselines3](https://stable-baselines3.readthedocs.io/en/master/).
* [Repo 2](https://github.com/cogito233/RoboMaster-AI-Challenge-Simulator-2D): [kernal_shortest_path.py](https://github.com/cogito233/RoboMaster-AI-Challenge-Simulator-2D/blob/master/kernal_shortest_path.py) seems interesting.

## IV. Possible ideas
* [@marcopra](https://github.com/marcopra): kenal_shortest_path.py can be used for RL training. 