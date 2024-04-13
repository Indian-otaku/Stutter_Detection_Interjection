import os
import pathlib

class Config:

    CWD : str = os.getcwd()
    AUDIO_FOLDER_WD : str = os.path.join(CWD, pathlib.Path("AudioFolder"))
    SAVED_CHECKPOINT_PATH = os.path.join(CWD, "utils", "saved_model", "w2v2-interjection-epoch=27-val_f1=0.678-2024-04-12_15-38-39.ckpt")
    SAVED_W2V2_PATH = os.path.join(CWD, "utils", "saved_model", "w2v2_architecture")

    SAMPLE_RATE = 16000