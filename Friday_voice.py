# pip install optimum
# scipy
# torch
# transformers
# IPython
# # noisereduce

from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
import os, torch
from transformers import BarkModel
from playsound import playsound
# os.environ["SUNO_USE_SMALL_MODELS"] = "True"
# os.environ["SUNO_OFFLOAD_CPU"] = "True"
device = "cuda" if torch.cuda.is_available() else "cpu"

from bark import SAMPLE_RATE, generate_audio, preload_models


# download and load all models
preload_models(
    )
def gen_audio(text_prompt, iter):
# generate audio from text
    audio_array = generate_audio(text_prompt, history_prompt='v2/en_speaker_8')

    # save audio to disk

    from scipy.io import wavfile
    import noisereduce as nr
    # load data
    # rate, data = wavfile.read("bark_generation.wav")
    # perform noise reduction
    reduced_noise = nr.reduce_noise(y=audio_array, sr=SAMPLE_RATE)
    wavfile.write("bark_generation" + str(iter) + ".wav", SAMPLE_RATE, reduced_noise)
    playsound("bark_generation" + str(iter) + ".wav")