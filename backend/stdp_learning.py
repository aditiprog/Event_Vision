from brian2 import *

start_scope()


# Input neurons (camera spikes)
input_neurons = SpikeGeneratorGroup(
    3,
    indices=[0,1,2],
    times=[10,20,30]*ms
)


# Output neuron
output_neuron = NeuronGroup(
    1,
    '''
    dv/dt = -v/(10*ms) : 1
    ''',
    threshold='v>=1',
    reset='v=0'
)


# Synapse with learning
synapse = Synapses(
    input_neurons,
    output_neuron,

    '''
    w : 1
    ''',

    on_pre='''
    v_post += w

    w = clip(w + 0.05,0,1)
    '''
)


synapse.connect()


# Initial connection strength

synapse.w = 0.5


# Monitor neuron firing

monitor = SpikeMonitor(output_neuron)


run(100*ms)


print("Neuron fired:")
print(monitor.i)


print("Learned weights:")
print(synapse.w[:])