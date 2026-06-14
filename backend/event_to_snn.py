import cv2
import numpy as np
from brian2 import *


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
# Create neurons
# -----------------------------

start_scope()


# Create 100 input neurons
input_neurons = NeuronGroup(
    100,
    '''
    dv/dt = -v/(10*ms) : 1
    ''',
    threshold='v>1',
    reset='v=0'
)


output_neuron = NeuronGroup(
    1,
    '''
    dv/dt = -v/(10*ms) : 1
    ''',
    threshold='v>1',
    reset='v=0'
)


synapse = Synapses(
    input_neurons,
    output_neuron,
    on_pre='''
    v_post += 0.2
    '''
)


synapse.connect()


monitor = SpikeMonitor(output_neuron)


# -----------------------------
# Camera loop
# -----------------------------

while True:


    ret, frame = cap.read()

    if not ret:
        break


    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


    # Detect change
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


    # Get spike locations
    locations = np.argwhere(events > 0)
    for y, x in locations:

        neuron_id = (x + y) % 100

    input_neurons.v[neuron_id] += 0.5



    # Show events
    cv2.imshow(
        "Spike Stream",
        events
    )


    prev_gray = gray


    if cv2.waitKey(1) & 0xff == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()


run(100*ms)


print(
    "Neuron firing:",
    monitor.i
)