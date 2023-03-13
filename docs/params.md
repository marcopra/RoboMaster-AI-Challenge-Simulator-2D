# The parameter format is explained

Many of the parameters are represented as arrays and need to be referenced in order to know what each one represents, which is why this manual exists

Note: `kernel` and `rmaics` parameters are not named in exactly the same way

|rmaics|kernel|meaning|
|-|-|-|
|[state](#state)||total state|
|[agents](#agents)|[cars](#agents)||state of the car|
|[compet](#compet)|[compet_info](#compet)|race information|
|[detect](#detect)|[detect](#detect)|Lidar detectable cars|
|[vision](#vision)|[vision](#vision)|cars that can be seen by the camera|
|[actions](#actions)|[orders](#actions)| commands to control the car|
|[g_map](#g_map)|[g_map](#g_map)|map information|
|[areas](#areas)|[areas](#areas)|area information|
|[barriers](#barriers)|[barriers](#barriers)|obstacle information|
||[actors](#acts)| lower level actions|

## state

``state`` is a custom class, defined as follows.

```python
class state(object):
    def __init__(self, time, agents, compet_info, done=False, detect=None, vision=None):
        self.time = time
        self.agents = agents
        self.compet = compet_info
        self.done = done
        self.detect = detect
        self.vision = vision
```

| name              | type  | range | explanation                |
|-------------------|-------|-------|----------------------------|
| time              | int   | 0~180 | match time remaining       |
| [events](#agents) | float | array | state of the car           |
| [compet](#compet) | int   | array | race information           |
| done              | bool  | 0~1   | whether the race is over   |
| [detect](#detect) | int   | array | which cars can be detected |
| [vision](#vision) | int   | array | which cars can be seen     |

## agents

`agents` describes the state of a robot, expressed in `kernel` as `cars`, a two-dimensional array (numpy.array) of type `float`, `shape` as (car_mun, 15), `car_num` as the number of robots, the type in the table is theoretical and the actual is determined by the overall type of the array. The format of the state of an individual robot is as follows.

| citation | name        | type  | range    | explanation                                                                 |
|----------|-------------|-------|----------|-----------------------------------------------------------------------------|
| 0        | owner       | int   | 0~1      | team, 0: red side, 1: blue side                                             |
| 1        | x           | float | 0~800    | x coordinate[0]                                                             |
| 2        | y           | float | 0~500    | y-coordinates                                                               |
| 3        | angle       | float | -180~180 | the absolute angle of the chassis[1]                                        |
| 4        | yaw         | float | -90~90   | the angle of the head relative to the chassis                               |
| 5        | heat        | int   | 0~       | muzzle heat                                                                 |
| 6        | hp          | int   | 0~2000   | blood                                                                       |
| 7        | freeze_time | int   | 0~600    | recharge time remaining [2], takes 3s                                       |
| 8        | is_supply   | bool  | 0~1      | 0: in recharge, 1: not in recharge                                          |
| 9        | can_shoot   | bool  | 0~1      | The decision frequency is higher than the maximum outgoing frequency (10Hz) |
| 10       | bullet      | int   | 0~       | remaining bullet count                                                      |
| 11       | stay_time   | int   | 0~1000   | Time spent in defense bonus zone, takes 5s                                  |
| 12       | wheel_hit   | int   | 0~       | the number of times the wheel hits the wall                                 |
| 13       | armor_hit   | int   | 0~       | number of times the armor plate hit the wall                                |
| 14       | car_hit     | int   | 0~       | the number of times a wheel or armor plate hit a car                        |


[0] Take the starting corner of the car as the origin and make all of the map fall on the positive half-axis

[1] with the origin the same as above and the polar axis falling on the positive x-axis and rotating in the positive direction towards the y-axis

[2] Calculated in epoch units, 200 epoch = 1s

## compet

`compet` refers to competition information, full name `competition_information`, denoted by `compet_info` in `kernel`, two-dimensional array of type `int`, all parameters also of type `int`, `shape` is (2, 4), as follows.

| lead0 | lead1 | name                  | range  | explanation               | team |
|-------|-------|-----------------------|--------|---------------------------|------|
| 0     | 0     | supply                | 0~2    | supply remaining times    | red  |
| 0     | 1     | bonus                 | 0~1    | plus_count_remaining      | red  |
| 0     | 2     | stay_time(deprecated) | 0~1000 | discarded, go to `agents` | red  |
| 0     | 3     | bonus_time            | 0~6000 | additional time remaining | red  |
| 1     | 0     | supply                | 0~2    | supply_time_remaining     | blue |
| 1     | 1     | bonus                 | 0~1    | additional_time_remaining | blue |
| 1     | 2     | stay_time(deprecated) | 0~1000 | discard, go to `agents`   | blue |
| 1     | 3     | bonus_time            | 0~6000 | additional time remaining | blue |


## detect & vision


`detect` refers to cars visible to LiDAR, `vision` refers to cars visible to the camera, both are represented as two-dimensional arrays, `shape` is: (car_num, car_num), for example

```python
# 0 1 2 3
detect = [[0, 1, 0, 0], # 0
          [0, 0, 1, 1], # 1
          [0, 0, 0, 0], # 2
          [1, 0, 0, 0]] # 3
```

Indicates:

* Car 0 can detect car 1

* Car 1 can detect cars 2 and 3

* Car 2 does not detect any cars

* Car 3 detects car 0

## actions

`actions` are instructions passed to the robot, called `orders` in `kernel`, two-dimensional arrays of type `int`, all parameters also of type `int`, `shape` is (car_num, 8), individual instructions have the following format

| citation | name       | range | explanation                                           | hand control button |
|----------|------------|-------|-------------------------------------------------------|---------------------|
| 0        | x          | -1~1  | -1: backward, 0: no movement, 1: forward [3]          | s/w                 |
| 1        | y          | -1~1  | -1: move left, 0: don't move, 1: move right           | q/e                 |
| 2        | rotate     | -1~1  | chassis, -1: left turn, 0: no movement, 1: right turn | a/d                 |
| 3        | yaw        | -1~1  | head, -1: turn left, 0: don't move, 1: turn right     | b/m                 |
| 4        | shoot      | 0~1   | Whether to shoot, 0: no, 1: yes                       | space               |
| 5        | supply     | 0~1   | When to trigger resupply, 0: No, 1: Yes               | f                   |
| 6        | shoot_mode | 0~1   | Shoot mode, 0: single shot, 1: burst                  | r                   |
| 7        | auto_aim   | 0~1   | Whether to enable self-targeting, 0: No, 1: Yes       | n                   |


[3] will constantly accelerate, x max speed 3m/s, y max speed 2m/s, you can actually interpret these buttons as a throttle, controlling whether to accelerate or not

`serial multi-player mode`: you can change the operation object by pressing the number above the keyboard, please refer to [operation.md](. /operation.md)

## g_map

`g_map` is short for `game_map`, a custom class defined as follows

```python
class g_map(object):
    def __init__(self, length, width, areas, barriers):
        self.length = length
        self.width = width
        self.areas = areas
        self.barriers = barriers
```

| name                  | type  | range | explanation                                                 |
|-----------------------|-------|-------|-------------------------------------------------------------|
| length                | int   | 800   | map length                                                  |
| length                | int   | 800   | map length                                                  |
| width                 | int   | 500   | the width of the map                                        |
| [areas](#areas)       | float | array | replenishment, starting and bonus area location information |
| [barriers](#barriers) | float | array | Location information for obstacles                          |


## areas & barriers

The format of a single area or obstacle is as follows

| lead | name      | range | explanation   |
|------|-----------|-------|---------------|
| 0    | border_x0 | 0~800 | left border   |
| 1    | border_x1 | 0~800 | right_border  |
| 2    | border_y0 | 0~500 | upper border  |
| 3    | border_y1 | 0~500 | bottom border |


Using the top left corner of the map as the origin

### areas

`areas` is a 3D array, `shape` is (2, 4, 4)

| lead0 | lead1 | name   | type               | team     |
|-------|-------|--------|--------------------|----------|
| 0     | 0     | bonus  | defence-plus-zone  | red      |
| 0     | 1     | supply | supply zone        | red side |
| 0     | 2     | start0 | Start Zone         | Red      |
| 0     | 3     | start1 | Start Zone         | Red      |
| 1     | 0     | bonus  | defense bonus zone | blue     |
| 1     | 1     | supply | supply zone        | blue     |
| 1     | 2     | start0 | starting zone      | blue     |
| 1     | 3     | start1 | starting zone      | blue     |

### barriers

`barriers` is a two-dimensional array and `shape` is (7, 4)

| lead0 | type       |
|-------|------------|
| 0     | horizontal |
| 1     | level      |
| 2     | horizontal |
| 3     | vertical   |
| 4     | vertical   |
| 5     | vertical   |
| 6     | vertical   |

## acts

This `acts` is an action in `kernel`, unlike [`actions`](#actions) in `rmaics`, this `acts` is a lower-level action of type `float` with a `shape` of: (car_num, 8)

| citation1 | name          | explanation                 |
|-----------|---------------|-----------------------------|
| 0         | rotate_speed  | Chassis_rotation_speed      |
| 1         | yaw_speed     | head rotation speed         |
| 2         | x_speed       | forward-backward speed      |
| 3         | y_speed       | left/right pan speed        |
| 4         | shoot         | whether to fire             |
| 5         | shoot_mutiple | whether to fire a burst     |
| 6         | supply        | whether to trigger resupply |
| 7         | auto_aim      | whether to auto aim         |