# Kernal Manual

## I. Basic information

### 1. Basic parameters

|Item|Value|Description|
|-|-|-|
|Game running frequency|200Hz|one cycle is called an epoch, i.e. 200 epoch/s|
|Decision (operation) maximum frequency|20Hz|i.e. 20 times/s|
|Size ratio|10mm/pixel|i.e. an 8m×5m map corresponds to an 800p×500p game screen|
|Car size|60p×45p|i.e. 600mm×450mm|
|Maximum speed of car forward and backward|1.5p/epoch|i.e. 3m/s|
|Maximum speed of car pan left/right|1p/epoch|i.e. 2m/s|
|maximum speed of chassis rotation|200°/s|not yet accurately measured, to be determined|
|maximum speed of gimbal rotation|600°/s|not yet accurately measured, to be determined|
|Bullet flight speed|12.5p/epoch|i.e. 25m/s, can be set|
|Muzzle heat settlement and the frequency of the blood deduction it causes|10Hz||

### 2. Notes

a. The speed of the chassis and gimbal will gradually increase to the maximum after pressing the corresponding command, and will gradually decrease after the command stops. For specific control commands, please refer to [operation.md](. /operation.md)

b. The default team divisions are red: car1, car3, blue: car2, car4. The reason for this design is that you can change the match mode simply by changing the number of cars. For example, when car_num = 3, the match mode is: 2v1

c. The role of `pygame` is only visual, i.e. the logic operations do not rely on `pygame` and the network does not need to rely on `pygame` when training

d. In manual operation, the game time is not based on the actual time, but on the game time

e. In manual operation, only one car can be controlled at a time

f. There is a bounce effect, but it does not fully comply with the laws of physics

g. You cannot trigger a recharge until you are within a certain distance of the recharge point, and you cannot control the recharge for 3s after triggering it

h. When the centre of the vehicle is within the square area of the defence bonus zone, the defence bonus will be timed

## II. Changeable parameters

In the `__init__` function of the `kernal` class, there are a number of quantities that can be changed depending on the environment such as the field, as follows

```python
        self.bullet_speed = 12.5 # bullet speed in pixel
        self.motion = 6 # the size of the inertia of the movement
        self.rotate_motion = 4 # inertial sense size for chassis rotation
        self.yaw_motion = 1 # inertia of rotation of the head
        self.camera_angle = 75 / 2 # the field of view of the camera
        self.lidar_angle = 120 / 2 # the field of view of the lidar
        self.move_discount = 0.6 # size of the strength of the bounce after hitting a wall
```

## III. Minor functions

### 1. Call map information

`kernal.get_map()`, returns `g_map`, see the parameter format: [params.md](. /params.md/#g_map)

### 2. Set the coordinates of the car

`kernal.set_car_loc(n, loc)`, `n` is the number of the car, 0~3, `loc` is the coordinates of the car, 2-dimensional array, no return
