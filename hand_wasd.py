#import dope libs
import cv2
import mediapipe as mp
import numpy as np
from pynput.keyboard import Key, Controller


# set some dope global variables
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
keyboard = Controller()
last_input_key = None


node_spec = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2) # color of nodes in BGR format
lines_spec = mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2) # color of the lines in BGR format


finger_tips = [mp_hands.HandLandmark.THUMB_TIP, mp_hands.HandLandmark.INDEX_FINGER_TIP,
               mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP,
               mp_hands.HandLandmark.PINKY_TIP]


# initialising the nodes for the finger stuff (see the readme for the image, you'll get what i mean.)
nodes = {
    "wrist": 0,
    "thumb": {"root": 1, "knuckle": 2, "middle": 3, "tip": 4},
    "index": {"root": 5, "knuckle": 6, "middle": 7, "tip": 8},
    "middle": {"root": 9, "knuckle": 10, "middle": 11, "tip": 12},
    "ring": {"root": 13, "knuckle": 14, "middle": 15, "tip": 16},
    "pinky": {"root": 17, "knuckle": 18, "middle": 19, "tip": 20},
}

def main():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image_bgr, blank_image = process_frame(image)

        cv2.putText(blank_image, 'q to exit', (450, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # window with real stuff
        # cv2.imshow('Hand Tracking', image_bgr)

        #window with fake stuff only
        cv2.imshow('Hand Nodes and Text', blank_image)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


def process_frame(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)
    blank_image = np.zeros_like(image_bgr)


    # i was gonna use this to detect left or right hand.
    if results.multi_handedness:
        for hand_handedness in results.multi_handedness:
            RL_handness = hand_handedness.classification[0].label


    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_drawing.draw_landmarks(
            blank_image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
            node_spec, lines_spec
        )

        # this commented code applies the fake hand on the real image window
        mp_drawing.draw_landmarks(
            image_bgr, hand_landmarks, mp_hands.HAND_CONNECTIONS,
            node_spec, lines_spec
        )

        input_key = get_input(hand_landmarks.landmark, RL_handness)
        cv2.putText(blank_image, f'Fingers Up: {input_key}', (255, 355), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(image_bgr, f'Fingers Up: {input_key}', (255, 355), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    return image_bgr, blank_image


def get_input(hand_landmarks, handness):
    global last_input_key
    input_key = None

    if handness == "Right":
        if hand_landmarks[nodes["thumb"]["tip"]].x < hand_landmarks[nodes["thumb"]["middle"]].x:
            input_key = Key.right
        elif hand_landmarks[nodes["index"]["tip"]].y < hand_landmarks[nodes["index"]["middle"]].y:
            input_key = Key.up
        elif hand_landmarks[nodes["pinky"]["tip"]].y < hand_landmarks[nodes["pinky"]["middle"]].y:
            input_key = Key.left
        elif hand_landmarks[nodes["index"]["tip"]].y > hand_landmarks[nodes["index"]["root"]].y:
            input_key = Key.down
    else:
        if hand_landmarks[nodes["thumb"]["tip"]].x > hand_landmarks[nodes["thumb"]["middle"]].x:
            input_key = Key.left
        elif hand_landmarks[nodes["index"]["tip"]].y < hand_landmarks[nodes["index"]["middle"]].y:
            input_key = Key.up
        elif hand_landmarks[nodes["pinky"]["tip"]].y < hand_landmarks[nodes["pinky"]["middle"]].y:
            input_key = Key.right
        elif hand_landmarks[nodes["index"]["tip"]].y > hand_landmarks[nodes["index"]["root"]].y:
            input_key = Key.down



    # Only press the key if it has changed
    if input_key != last_input_key:
        if last_input_key is not None:
            keyboard.release(last_input_key)
        if input_key is not None:
            keyboard.press(input_key)
        last_input_key = input_key

    return input_key

if __name__ == "__main__":
    main()
