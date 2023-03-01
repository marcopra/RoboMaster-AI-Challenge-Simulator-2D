## Description of control commands

## Robot action instructions

Individual commands are one-dimensional arrays of type: `int`, as follows

|fuse|name|range|explanation|hand control button|
|-|-|-|-|-|
|0|x|-1~1|-1: backward, 0: no movement, 1: forward|s/w|
|1|y|-1~1|-1: move left, 0: don't move, 1: move right|q/e|
|2|rotate|-1~1|chassis, -1: left turn, 0: no movement, 1: right turn|a/d|
|3|yaw|-1~1|head, -1: turn left, 0: don't move, 1: turn right|b/m|
|4|shoot|0~1|Whether to shoot, 0: no, 1: yes|space|
|5|supply|0~1|When to trigger resupply, 0: No, 1: Yes|f|
|6|shoot_mode|0~1|Shoot mode, 0: single shot, 1: burst|r|
|7|auto_aim|0~1|Whether to enable self-targeting, 0: No, 1: Yes|n|

## Auxiliary Keys

|key|explanation|example|
|-|-|-|
|Number above keyboard|switch operation object|for example, press `2` to control `car2`|
|Tab|shows more information|-|

## Record Player's keys

`Record Player` can be used to replay previous games, for more information see [record_player.md](. /record_player.md)

|keys|explain|
|-|-|
|Tab|Show more information|
|←|Back|
|→|fast-forward|
|space|pause|