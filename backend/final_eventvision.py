import cv2
import numpy as np
from brian2 import *
import requests

# -----------------------------
# Camera setup
# -----------------------------

cap = cv2.VideoCapture(0)

ret, prev_frame = cap.read()

prev_gray = cv2.cvtColor(
    prev_frame,
    cv2.COLOR_BGR2GRAY
)


SPIKE_THRESHOLD = 25



# -----------------------------
# SNN setup
# -----------------------------

start_scope()


input_neurons = NeuronGroup(
    100,
    '''
    dv/dt = -v/(10*ms) : 1
    ''',
    threshold='v>=1',
    reset='v=0'
)



output_neuron = NeuronGroup(
    1,
    '''
    dv/dt = -v/(10*ms) : 1
    ''',
    threshold='v>=1',
    reset='v=0'
)



# STDP Synapse

synapse = Synapses(
    input_neurons,
    output_neuron,

    '''
    w : 1
    ''',

    on_pre='''
    v_post += w
    w = clip(w+0.01,0,1)
    '''
)



synapse.connect()

synapse.w = 0.5



spike_monitor = SpikeMonitor(output_neuron)



# -----------------------------
# Main loop
# -----------------------------

print("EventVision Running - Press Q")


while True:


    ret, frame = cap.read()

    if not ret:
        break



    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


    # Event generation

    difference = cv2.absdiff(
        gray,
        prev_gray
    )



    _, events = cv2.threshold(
        difference,
        SPIKE_THRESHOLD,
        255,
        cv2.THRESH_BINARY
    )



    # Convert pixels into neuron spikes

    locations = np.argwhere(events > 0)
    activity = len(locations)
    print("activity:", activity)

    # Data efficiency calculation

    total_pixels = events.size

    processed_events = len(locations)


    data_saved = 100 * (
        1 - processed_events / total_pixels
    )


    # Send live data to FastAPI

    if activity > 500:
       status = "Movement Detected"
    else:
       status = "No Activity"


    requests.post(
         "http://127.0.0.1:8000/update",
    json={
        "status": status,
        "spikes": activity,
        "saved": round(data_saved,2)
    }
)
        
    

    cv2.putText(
    events,
    f"Data Saved: {data_saved:.2f}%",
    (10,90),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255,255,255),
    2
)


    if activity > 500:
        status = "Movement Detected"
    else:
        status = "No Activity"


    cv2.putText(
    events,
    status,
    (10,50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255,255,255),
    2
)



    for y,x in locations:


        neuron_id = (x+y)%100


        



    # Run small neural step

    



    # Display

    cv2.imshow(
        "Neuromorphic Spike Stream",
        events
    )



    prev_gray = gray



    if cv2.waitKey(1) & 0xff == ord('q'):
        break




cap.release()

cv2.destroyAllWindows()



print(
"Neuron firing count:",
len(spike_monitor.i)
)


print(
"Final learned weights:",
synapse.w[:5]
)