# hfdl
Hugging Face Downloader in Python using HF Hub

A dirty simple downloader with a few command line args.  Default download dir is ./models, if it's not there it'll create it.  

I spit this code out in about 15 mins including reading HF docs, I'll try to clean it up soon. 

-------
# Install
  `pip install argparse huggingface_hub`

# Run
 `python hfdl.py`

# Usage
    `hfdl.py [-h] [--model_dir MODEL_DIR] [--gguf_quant GGUF_QUANT] [--branch BRANCH] [MODEL]
    
    Download model from HF.
    
    positional arguments:
      MODEL                 model to download in format PUBLISHER/REPO
    
    options:
      -h, --help            show this help message and exit
      --model_dir MODEL_DIR
                            Directory to store models in. Default: ./models
      --gguf_quant GGUF_QUANT
                            quant to retrieve, like Q6_K
      --branch BRANCH       branch to download`

-------

Download TheBloke/neural-chat-7B-v3-3-GGUF with Q8_0 quantization

python3 hfdl.py TheBloke/neural-chat-7B-v3-3-GGUF --gguf_quant Q8_0

-------

Download the whole argilla/notux-8x7b-v1 repo snapshot

python3 hfdl.py argilla/notux-8x7b-v1

-------

Download the gptq-8bit-32g-actorder_True branch of TheBloke/OpenHermes-2.5-Mistral-7B-GPTQ

python3 hfdl.py TheBloke/OpenHermes-2.5-Mistral-7B-GPTQ --branch gptq-8bit-32g-actorder_True

-------

Download microsoft/phi-2 to a given directory /home/user/models (will create directory)

python3 hfdl.py microsoft/phi-2 --model_dir /home/user/models
