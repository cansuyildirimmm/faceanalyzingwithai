from deepface import DeepFace
img_path = 'cansu.jpeg'
resp = DeepFace.analyze(img_path, ("emotion")) 
print(resp)



import cv2
from deepface import DeepFace

# Kamerayı başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı")
    exit()

while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()

    if not ret:
        print("Kare okunamadı")
        break

    try:
        # DeepFace ile duygu analizi yap
        result = DeepFace.analyze(frame, ('emotion'))
        dominant_emotion = ", ".join(map(lambda r: r["dominant_emotion"], result))
    except Exception as e:
        dominant_emotion = "Analiz yapilamadi"
        # print(f"Analiz hatası: {e}")

    # Sonuçları görüntüye yaz
    font = cv2.FONT_HERSHEY_SIMPLEX
    #cv2.putText(frame, dominant_emotion, (50, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    for res in result:
        x = res["region"]["x"]
        y = res["region"]["y"]
        w = res["region"]["w"]
        h = res["region"]["h"]

        x1 = x
        y1 = y
        x2 = x + w
        y2 = y + h
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), color=(255,0,0), thickness=2)
        dominant_emotion = res["dominant_emotion"]
        cv2.putText(frame, dominant_emotion, (x1, y1 - 10), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Görüntüyü göster
    cv2.imshow('Kamera', frame)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.getWindowProperty('Kamera', cv2.WND_PROP_VISIBLE) < 1:
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
