import cv2
import mediapipe as mp
import numpy as np

def main():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils

    # Define custom drawing specifications
    drawing_spec = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2) # color of nodes in BGR format
    connection_spec = mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2) # color of the lines in BGR format

    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)  # Set max_num_faces to 1 for single face tracking
    cap = cv2.VideoCapture(0)  # Open the default camera (usually webcam)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR frame to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        blank_image = np.zeros_like(rgb_frame)

        face_results = face_mesh.process(rgb_frame)
        hand_results = hands.process(rgb_frame)

        if face_results.multi_face_landmarks:
            for face_landmarks in face_results.multi_face_landmarks:
                # Draw face landmarks on the frame
                for landmark in face_landmarks.landmark:
                    x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])

                    # draw the spots and add color
                    cv2.circle(blank_image, (x, y), 2,  (0, 255, 0), -1)

        if hand_results.multi_hand_landmarks:
            for hand_landmarks in hand_results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    blank_image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    drawing_spec, connection_spec
                )



        cv2.imshow("Face Mesh", frame)
        cv2.imshow("fake stuff", blank_image)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
