import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Define custom drawing specifications
node_spec = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2) # color of nodes in BGR format
lines_spec = mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2) # color of the lines in BGR format

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
        if hand_results.multi_handedness:
            for hand_handedness in hand_results.multi_handedness:
                RL_handness = hand_handedness.classification[0].label

        if hand_results.multi_hand_landmarks:
            if hand_results.multi_hand_landmarks:
                for hand_landmarks in hand_results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        blank_image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                        node_spec, lines_spec
                    )


            fingers_up = count_fingers(hand_results, RL_handness)


            # Display the count
            cv2.putText(image, f'Fingers Up: {fingers_up}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.putText(blank_image, f'Fingers Up: {fingers_up}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            if fingers_up == 9:
                import time
                time.sleep(2)
        cv2.putText(image, f'q to exit', (450, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow('Hand Tracking', image)
        cv2.imshow("hand track but fake stuff only", blank_image)
        if cv2.waitKey(5) & 0xFF == ord("q"):
            break

    cap.release()


def count_fingers(hand_results, RL_handness):
    finger_tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                   mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                   mp_hands.HandLandmark.RING_FINGER_TIP,
                   mp_hands.HandLandmark.PINKY_TIP,
                   mp_hands.HandLandmark.THUMB_TIP]  # Include thumb tip

    fingers_up = 0
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            # Count fingers
            for tip in finger_tips:
                if tip != mp_hands.HandLandmark.THUMB_TIP:
                    if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                        fingers_up += 1
                else:
                    if RL_handness == "Right":
                        if hand_landmarks.landmark[nodes["thumb"]["tip"]].x < hand_landmarks.landmark[nodes["thumb"]["middle"]].x:
                            fingers_up += 1
                    else:
                        if hand_landmarks.landmark[nodes["thumb"]["tip"]].x > hand_landmarks.landmark[nodes["thumb"]["middle"]].x:
                            fingers_up += 1

    return fingers_up


if __name__ == "__main__":
    main()
