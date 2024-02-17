from huggingface_hub import hf_hub_download, snapshot_download, list_files_info
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description='Download model from HF.')
parser.add_argument('model', metavar='MODEL', type=str, nargs='?',
                    help='model to download in format PUBLISHER/REPO')
parser.add_argument('--model_dir', default='./models',
        help='Directory to store models in. Default: ./models')
parser.add_argument('--gguf_quant', help='quant to retrieve, like Q6_K')
parser.add_argument('--branch', help='branch to download')

args = parser.parse_args()

if args.model_dir is not None:
    base_dir = args.model_dir
else:
    base_dir = "./models"

model_dict = args.model.split('/')
publisher = model_dict[0]
repo = model_dict[1]

publisher_path = Path(publisher)
repo_path = Path(repo)
base_path = Path(base_dir)

model_path = base_path / publisher_path / repo_path

if not base_path.is_dir():
    base_path.mkdir()

if not model_path.is_dir():
    model_path.mkdir(parents=True)

if args.gguf_quant is not None:
    files_info = [info.path for info in list_files_info(args.model)]

    for file in files_info:
        filetype = file.split('.')[-1]
        if not filetype == 'gguf':
            hf_hub_download(repo_id=args.model, filename=file, local_dir=model_path, local_dir_use_symlinks=False)
        elif args.gguf_quant.lower() in file.lower():
            hf_hub_download(repo_id=args.model, filename=file, local_dir=model_path, local_dir_use_symlinks=False)
else:
    snapshot_download(repo_id=args.model, local_dir=model_path, revision=args.branch, local_dir_use_symlinks=False)
