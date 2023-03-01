# RMAICS Manual

## I. Designing the observation and reward functions

First complete the `get_observation` and `get_reward` parts of the wrapper class `rmaics`, i.e. the following two parts, according to your needs

```python
    def get_observation(self, state):
        # personalize your observations here
        obs = None
        return obs
    def get_reward(self, state):
        # personalize your observation here
        rewards = None
        return rewards
```

To use the map information, call the `get_map` function of `kernal`, which will return the map information in the format [params.md](. /params.md). For example

```python
game = kernal(car_num=1, render=True)
g_map = game.get_map()
```

## II. Getting Started

`rmaics` is used in a similar way to [gym](https://github.com/openai/gym) in [openai](https://openai.com/)

### 1. Initialization

Import, declare and initialize, display the session screen when `render` is `True` and you can use keyboard operations, not vice versa

```python
from rmaics import rmaics
car_num = 4
game = rmaics(agent_num=car_num, render=True)
game.reset()
```

### 2. Execution step

Pass in decisions to get observations, rewards, whether to end, and other information, see the specific format of the parameters: [params.md](. /params.md)

```python
# action format (int, np.array): [['x', 'y', 'rotate', 'yaw', 'shoot', 'supply', 'shoot_mode', 'auto_aim'], ...]
# action.shape = (car_num, 8)
actions = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
obs, reward, done, _ = game.step(actions)
```

### 3. Using keyboard control

If you use keyboard control manually, call the following function, note: only `render` is `True` can be called, click on the close icon of the window with the mouse to stop the game normally

```python
game.play()
```

### 4. Saving memory

The memory here refers to `kernal` memory, which will be saved as a [npy](https://stackoverflow.com/questions/4090080/what-is-the-way-data-is-stored-in-npy) file containing the information needed to reproduce the game. Please refer to [record_player](. /record_player.md), which is saved as follows

```python
game.save_record(file='. /records/record.npy')
```