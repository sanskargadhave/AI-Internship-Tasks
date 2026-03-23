import cv2

# -------------------------------
# Step 1: Load Haar Cascade Model
# -------------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# -------------------------------
# Step 2: Start Webcam
# -------------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

print("Press ESC to exit")

# -------------------------------
# Step 3: Capture Frames
# -------------------------------
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # -------------------------------
    # Step 4: Detect Faces
    # -------------------------------
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    # -------------------------------
    # Step 5: Draw Rectangles
    # -------------------------------
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        

    # Show output
    cv2.imshow("Face Detection", frame)

    # Exit on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# -------------------------------
# Step 6: Release Resources
# -------------------------------
cap.release()
cv2.destroyAllWindows()