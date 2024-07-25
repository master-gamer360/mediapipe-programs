#import dope libs
import cv2
import mediapipe as mp
import numpy as np


# set some dope global variables
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

node_spec = mp_drawing.DrawingSpec(color=(208, 253, 255), thickness=2, circle_radius=2) # color of nodes in BGR format
lines_spec = mp_drawing.DrawingSpec(color=(130, 0, 75), thickness=2) # color of the lines in BGR format


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
        cv2.imshow('Hand Tracking', image_bgr)

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

        decimal_up = count_decimal_up(hand_landmarks, RL_handness)
        cv2.putText(blank_image, f'Fingers Up: {decimal_up}', (255, 355), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    return image_bgr, blank_image

def count_decimal_up(hand_landmarks, handness):

    # this is a terrible idea, but it was my only idea.
    decimal_up = 0
    # if true is printed, it means its facing the camera
    print(hand_landmarks.landmark[nodes["index"]["tip"]].z <= hand_landmarks.landmark[nodes["index"]["middle"]].z)

    if handness == "Right":
        if hand_landmarks.landmark[nodes["thumb"]["tip"]].x <= hand_landmarks.landmark[nodes["thumb"]["middle"]].x:
            decimal_up += 1
    elif handness == "Left":
        if hand_landmarks.landmark[nodes["thumb"]["tip"]].x >= hand_landmarks.landmark[nodes["thumb"]["middle"]].x:
            decimal_up += 1

    if hand_landmarks.landmark[nodes["index"]["tip"]].y <= hand_landmarks.landmark[nodes["index"]["knuckle"]].y:
        decimal_up += 2
    if hand_landmarks.landmark[nodes["middle"]["tip"]].y <= hand_landmarks.landmark[nodes["middle"]["knuckle"]].y:
        decimal_up += 4
    if hand_landmarks.landmark[nodes["ring"]["tip"]].y <= hand_landmarks.landmark[nodes["ring"]["root"]].y:
        decimal_up += 8
    if hand_landmarks.landmark[nodes["pinky"]["tip"]].y <= hand_landmarks.landmark[nodes["pinky"]["root"]].y:
        decimal_up += 16
    return decimal_up


if __name__ == "__main__":
    main()
