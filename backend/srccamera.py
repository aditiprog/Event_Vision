import cv2
import numpy as np

# Initialize webcam
cap = cv2.VideoCapture(0)

# Read the first frame as baseline
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Threshold for what constitutes an "event spike"
SPIKE_THRESHOLD = 25 

print("Simulating Event-Driven Sensor... Press 'q' to exit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
        
    # Convert current frame to grayscale
    current_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate absolute difference between consecutive frames
    frame_delta = cv2.absdiff(current_gray, prev_gray)
    
    # Create a binary map: 1 if pixel changed significantly (Spike), else 0
    _, spike_events = cv2.threshold(frame_delta, SPIKE_THRESHOLD, 255, cv2.THRESH_BINARY)
    
    # Calculate "Power Saved" metric for presentation
    total_pixels = spike_events.size
    active_spikes = np.count_nonzero(spike_events)
    bandwidth_reduction = 100.0 * (1.0 - (active_spikes / total_pixels))
    
    # Visualizing the asynchronous spikes
    cv2.putText(spike_events, f"Bandwidth Reduction: {bandwidth_reduction:.2f}%", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.imshow("Asynchronous Spike Stream", spike_events)
    
    # Update baseline to current frame
    prev_gray = current_gray
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()