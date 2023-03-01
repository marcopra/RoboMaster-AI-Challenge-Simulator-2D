# Recorder Manual

The "Recorder" can be used to replay previous games

## I. Saving game memories

```python
from rmaics import rmaics
game = rmaics(agent_num=4, render=True)
game.reset()
# Only if render=True
game.play()

game.save_record('. /records/record0.npy')
```

Note: Clicking with the mouse on the close icon in the game window, the red "x" under "Windows" in the top right corner, will end the game normally and the game's memory will not be emptied.

## II. Re-create the game

```python
from kernal import record_player
player = record_player()
player.play('. /records/record0.npy')
```

You can use the '←' and '→' keys to control the playback progress and the 'space' key to pause, see [operation.md](. /operation.md)