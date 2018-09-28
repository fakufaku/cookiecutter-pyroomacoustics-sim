import numpy as np
import pyroomacoustics as pra
import matplotlib.pyplot as plt

# Simulation parameters
fs = {{ cookiecutter.samplerate }}
absorption = {{ cookiecutter.absorption }}
max_order = {{ cookiecutter.max_order }}

# Geometry of the room and location of sources and microphones
{%- if cookiecutter.room_type == "shoebox" %}
{%- if cookiecutter.dimension == "2D" %}
room_dim = np.array([10, 7.5])
source_loc = np.array([2.51, 3.57])
mic_loc = np.c_[[7, 6.7]]
{%- else %}
room_dim = np.array([10, 7.5, 3])
source_loc = np.array([2.51, 3.57, 1.7])
mic_loc = np.c_[[7, 6.7, 1.3]]
{%- endif %}
{%- else %}
corners = np.c_[[0,0], [0,4], [8,4], [8,2], [4,2], [4,0]]
{%- if cookiecutter.dimension == "2D" %}
source_loc = np.array([2.51, 2.57])
mic_loc = np.c_[[6.7, 3.1]]
{%- else %}
height = 3
source_loc = np.array([2.51, 2.57, 1.7])
mic_loc = np.c_[[6.7, 3.1, 1.3]]
{%- endif %}
{%- endif %}

# Create the room itself
{%- if cookiecutter.room_type == "shoebox" %}
room = pra.ShoeBox(room_dim, fs=fs, absorption=absorption, max_order=max_order)
{%- else %}
room = pra.Room.from_corners(corners, fs=fs, absorption=absorption, max_order=max_order)
{%- if cookiecutter.dimension == "3D" %}
room.extrude(height)
{%- endif %}
{%- endif %}

# Place the source
room.add_source(source_loc)

# Place the microphone array
room.add_microphone_array(
        pra.MicrophoneArray(mic_loc, fs=room.fs)
        )

# Now the setup is finished, start doing whatever you like
# As an example, we compute the RIR and plot a few images sources
room.compute_rir()
room.plot(img_order=4)

plt.figure()
room.plot_rir()

plt.show()
