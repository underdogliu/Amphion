#!/usr/bin/env python3
import os
import sys
import site
import setuptools
from distutils.core import setup



# Editable install in user site directory can be allowed with this hack:
# https://github.com/pypa/pip/issues/7953.
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]

with open("README.md") as f:
    long_description = f.read()

# with open(os.path.join("speechbrain", "version.txt")) as f:
#     version = f.read().strip()


setup(
    name="amphion",
    version='0.1.0',
    description="An Open-Source Audio, Music, and Speech Generation Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Xueyao Zhang & Others",
    author_email="speechbrain@gmail.com",
    classifiers=[ 
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(),
    package_data={"speechbrain": ["version.txt", "log-config.yaml"]},
    install_requires=[
        "torch==2.0.1",
        "torchaudio==2.0.2",
        "torchvision==0.15.2",
        "accelerate==0.24.1",
        "ruamel.yaml",
        "tqdm",
        "colorama",
        "easydict",
        "tabulate",
        "loguru",
        "json5",
        "Cython",
        "unidecode",
        "inflect",
        "argparse",
        "g2p_en",
        "tgt",
        "librosa==0.9.1",
        "matplotlib",
        "typeguard",
        "einops",
        "omegaconf",
        "hydra-core",
        "humanfriendly",
        "pandas",
        "tensorboard",
        "transformers",
        "diffusers",
        "praat-parselmouth",
        "audiomentations",
        "pedalboard",
        "ffmpeg-python==0.2.0",
        "pyworld",
        "diffsptk==1.0.1",
        "nnAudio",
        "unidecode",
        "inflect",
        "ptwt",
        "torchmetrics",
        "pymcd",
        "openai-whisper",
        "frechet_audio_distance",
        "asteroid",
        "resemblyzer",
        "vector-quantize-pytorch==1.12.5",
    ],
    python_requires=">=3.9",
    url='https://github.com/open-mmlab/Amphion',  # URL to your package's repository
)
