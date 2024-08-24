import cv2
import mediapipe as mp
import numpy as np
from math import sqrt
import keyboard


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils
last_input_key = None


# Define custom drawing specifications
node_spec = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2) # color of nodes in BGR format
lines_spec = mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=4) # color of the lines in BGR format

# Finger tip landmarks
finger_tips = [mp_hands.HandLandmark.THUMB_TIP, mp_hands.HandLandmark.INDEX_FINGER_TIP,
               mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP,
               mp_hands.HandLandmark.PINKY_TIP]


nodes = {
    "wrist": 0,
    "thumb": {"root": 1,"knuckle": 2,"middle": 3,"tip": 4,},
    "index": {"root": 5,"knuckle": 6,"middle": 7,"tip": 8,},
    "middle": {"root": 9,"knuckle": 10,"middle": 11,"tip": 12,},
    "ring": {"root": 13,"knuckle": 14,"middle": 15,"tip": 16,},
    "pinky": {"root": 17,"knuckle": 18,"middle": 19,"tip": 20,},
}


def main():
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        blank_image = np.zeros_like(image_bgr)

        hand_results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        images = [image, blank_image]
        if hand_results.multi_handedness:
            for hand_handedness in hand_results.multi_handedness:
                RL_handness = hand_handedness.classification[0].label

        if hand_results.multi_hand_landmarks:
            if hand_results.multi_hand_landmarks:
                for hand_landmarks in hand_results.multi_hand_landmarks:
                    for img in images:
                        mp_drawing.draw_landmarks(
                            img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                            node_spec, lines_spec
                        )

            blank_image, d = add_lines(blank_image, hand_landmarks.landmark)
            # image, d = add_lines(image, hand_landmarks.landmark)
            change_volume(d)


            # Display the count
            cv2.putText(blank_image, f'dist: {d}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        # cv2.imshow('Hand Tracking', image)
        cv2.imshow("hand track but fake stuff only", blank_image)
        if cv2.waitKey(5) & 0xFF == ord("q"):
            break

    cap.release()


def change_volume(d):
    global last_input_key
    input_key = None
    if d > 0.08:
        input_key = 'volume up'
    elif d < 0.08:
        input_key = 'volume down'

    if input_key != None:
        for _ in range(10):
            keyboard.press(input_key)


def add_lines(image, hand_landmark):
    thumb_tip = hand_landmark[nodes["thumb"]["tip"]]
    index_tip = hand_landmark[nodes["index"]["tip"]]

    # Convert landmarks to pixel coordinates
    x1, y1 = int(thumb_tip.x * image.shape[1]), int(thumb_tip.y * image.shape[0])
    x2, y2 = int(index_tip.x * image.shape[1]), int(index_tip.y * image.shape[0])

    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) / 1000

    # Draw a line from thumb tip to index tip
    return cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 4), d


if __name__ == "__main__":
    main()
