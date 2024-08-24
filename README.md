# Libaries:
<details>
<summary>opencv-python</summary>

### Open Computer Vision
A computer vision library used for all sorts of things
I use it to read the camera frame-by-frame

#### download command
```
pip install opencv-python
```
</details>

<details>
<summary>mediapipe</summary>

### mediapipe
Mediapipe provides pre-trained models for human posture estimation and when used with opencv it can be used for
live estimation.

#### download command
```
pip install mediapipe
```


</details>

<details>
<summary>numpy</summary>

### numpy
I don't know much about it but I used it to create empty windows I can put my mediapipe things in without the real stuff.

#### download command (but its one of the default libraries.)
```
pip install numpy
```

</details>

<details>
<summary>pynput</summary>

### Pynput
A python library used to simulate things like mouse and keyboard clicks

i used this for the hand_wasd.py file to simulate the WASD keys when a certain gesture is applied

#### download command
```
pip install pynput
```
</details>

<details>
<summary>keyboard</summary>

### Pynput
similar to pynput.

i used this for the volume.py program to simulate the volume up and down.

#### download command
```
pip install keyboard
```
</details>




# files:

<details>
<summary>normal_count.py</summary>

## normal_count.py:
it counts the ammount of fingers raised, works with both hands

</details>

<details>
<summary>binary_count.py</summary>

## binary_count.py:
counts the binary of fingers, if thumb and ring is up, the decimal value is 9.

#### If you do not know how to count binary on your fingers, here's a [video](https://www.youtube.com/watch?v=XKpWSKjdv4U).

</details>

<details>
<summary>hand_wasd.py</summary>

## hand_wasd.py
It uses hand gestures to play games that incorporate the WASD control scheme

#### the hand gestures of the left hand will appear right from the camera's prespective, so, keep that in mind.
</details>

<details>
<summary>volume.py</summary>

## volume.py:
it allows you to control the volume by moving your thumb and index finger.

move them close to decrease, and move them further to increase.

I used the keyboard library for simulating the volume controls.

</details>


# test files

<details>
<summary>face_hands_test.py</summary>

## face_hands_test.py
a test for face mesh with hand estimation

<details>
