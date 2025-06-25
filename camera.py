import cv2
import mediapipe as mp
import os
import sys
import time

# El takibi
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def start_hand_tracking():
    hands = mp_hands.Hands(min_detection_confidence=0.7)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Yumruk kontrolü: Başparmak ve işaret parmağı ucu yakın mı?
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                h, w, _ = frame.shape
                x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
                x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

                distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

                if distance < 30:  # Mesafe çok küçükse yumruk say
                    print("✊ Yumruk algılandı! Sistem yeniden başlatılıyor...")
                    time.sleep(1)
                    cap.release()
                    cv2.destroyAllWindows()
                    restart_program()

        cv2.imshow("El Takip Sistemi", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def restart_program():
    print("🔁 Yeniden başlatılıyor...\n")
    python = sys.executable
    os.execl(python, python, *sys.argv)

if __name__ == "__main__":
    start_hand_tracking()
