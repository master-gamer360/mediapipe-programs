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

<details>
<summary>pictures of hand gestures</summary>


- left hand right
![](https://cdn.discordapp.com/attachments/1265341827930652703/1266058606298796136/image.png?ex=66a3c475&is=66a272f5&hm=0cb50f742432dff2b35b2b10b461032deea0f359e9c709bf2648d94046551cc3&)
- left hand up
![](https://cdn.discordapp.com/attachments/1265341827930652703/1266058759604797450/image.png?ex=66a3c49a&is=66a2731a&hm=d770bfc5f89329e8be07b5fd44d0025bb3caa71128bfb36fdd2c7d3295bf3fd7&)
- left hand left
![](https://cdn.discordapp.com/attachments/1265341827930652703/1266058850306363472/image.png?ex=66a3c4b0&is=66a27330&hm=4ea4da6379ca7dc2054b14af1f65400a19768180ccf4010859733f5d047785fb&)
- left hand down
![](https://cdn.discordapp.com/attachments/1265341827930652703/1266058944229412934/image.png?ex=66a3c4c6&is=66a27346&hm=9fe1e6003cc1ba7048836fc4a3a68f7aadbaaf76b933a6130a1e3a6b43caddf8&)

###  \\/\\/\\/\\/\\/

## for the right hand, the thumb and the pinky is switched

- right hand left
![](https://cdn.discordapp.com/attachments/1265341827930652703/1266059157975601384/image.png?ex=66a3c4f9&is=66a27379&hm=ed7974f495b65cf43fe5b265c97b2b5ce3421b9c965eb3cb3818c26d87c59c2d&)
- right hand right
![](https://cdn.discordapp.com/attachments/1265341827930652703/1266059279165816842/image.png?ex=66a3c516&is=66a27396&hm=e964b27732770f9626966751c5468fc987b5f2299a85530a8c97c9ff5853b0fd&)

</details>
</details>

# test files

<details>
<summary>face_hands_test.py</summary>

## face_hands_test.py
a test for face mesh with hand estimation

<details>
