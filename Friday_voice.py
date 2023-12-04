# scipy
# torch
# transformers
# IPython
# noisereduce

import torch
from playsound import playsound
from scipy.io import wavfile
import noisereduce as nr
from bark import SAMPLE_RATE, generate_audio, preload_models

device = "cuda" if torch.cuda.is_available() else "cpu"
# download and load all models
preload_models(
    )
def gen_audio(text_prompt, iter):
# generate audio from text
    audio_array = generate_audio(text_prompt, history_prompt='v2/en_speaker_8')
    # save audio to disk
    reduced_noise = nr.reduce_noise(y=audio_array, sr=SAMPLE_RATE)
    wavfile.write("bark_generation" + str(iter) + ".wav", SAMPLE_RATE, reduced_noise)
    playsound("bark_generation" + str(iter) + ".wav")
