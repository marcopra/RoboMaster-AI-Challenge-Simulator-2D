# Kernal Development Guide

## I. Notes on development

When developing, note the parameter format description: [params.md](./params.md)

## II. Introduction to the structure

The core function of `kernal` is: `one_epoch`, which means it will run for one cycle, and in one cycle it will call: `move_car`, `move_bullet`, and at the same time it will update the view information, race information, etc., and update the game screen (if the screen is displayed)

There are two functions that can be called on `one_epoch`: `step` and `play`. What `step` does is to get the instructions `orders` passed in by the user, convert `orders` to `acts` and then run for 10 cycles; the only difference with `play` is that it will keep running and then get `orders` from the keyboard once every 10 cycles. Note: `acts` in `kernal` is different from `actions` in `rmaics`, while `orders` in `kernal` is the same as `actions` in `rmaics`

## III. Areas for improvement

### 1. Speed of operation

The following are the results of the current test without visualisation on.

|number of cars|action instructions|simulation time|program run time|
|-|-|-|-|
|1|full|3min|8.2s|
|2|full|3min|17.1s|
|3|full|3min|25.5s|
|4|full|3min|51.2s|

Testing environment: Windows 10, octa-core i5-8250U CPU 1.60GHz; CPU usage: ~20%, note that the CPU usage is around 20% no matter what program is running, this is just an indication of the actual CPU power used during the test

Test code.

```python
from rmaics import rmaics
import numpy as np
import time

game = rmaics(agent_num=2, render=True)
game.reset()
actions = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]])

t1 = time.time()
for _ in range(3600): # 3600epoch = 180s
    obs = game.step(actions)
t2 = time.time()
print(t2 - t1)
```

#### Some possible implementations

Use numba or Cython

### 2. Parallel matches

Multiple simultaneous matches at the ``kernal'' level, so that you don't have to dedicate multiple processes, which can improve learning speed

### 3. Online matchmaking

It is not very convenient for a computer to operate four cars at the same time, so if human and human want to play against each other, they need to operate online, and the purpose of achieving human-human confrontation is to enable imitation learning, the idea of imitation learning comes from [AlphaStar](https://www.deepmind.com/blog/alphastar-mastering-the-real-time-strategy-game-starcraft-ii) by [DeepMind](https://deepmind.com/) 

#### Operating Instructions

The other parts are basically untouched, change the method of getting instructions to network access, and also change the way the head is controlled to be controlled with the mouse in the `get_order` function

### 4. Increase the random error

The simulator is not the real world after all, adding some randomness can help improve the ability to migrate from simulation to reality, the idea comes from the [OpenAI](https://openai.com/) study [Generalizing from Simulation](https://blog.openai.com/generalizing-from-simulation/)

#### Operating Instructions

Add some errors to `self.acts` at the beginning of the function `move_car`; for details on `acts`, see [params.md](./params.md), note that it is the `acts` in `kernal`

### 5. Field of view

The LIDAR and camera field of view is used to indicate that a car can be detected and when a car is in the camera field of view, this car can be targeted automatically. The field of view algorithm used now is: firstly to check if the angle matches and then to check if there is an obstruction (obstacle or car) in the centre line of the two cars. The problem with this is that at somewhat tricky angles, an unreasonable field of view can occur

