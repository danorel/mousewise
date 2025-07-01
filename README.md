# macOS Training Guide

Welcome to **Mouse vs. AI: Robust Visual Foraging Challenge @ NeurIPS 2025**

This is a training guide for **macOS**. For other operating systems, please check:
[Windows](https://github.com/robustforaging/mouse_vs_ai_windows?tab=readme-ov-file#windows-training-guide) and [Linux](https://github.com/robustforaging/mouse_vs_ai_linux)

# Create conda environment
open command prompt and `cd` into your working directory:
```bash
CONDA_SUBDIR=osx-64 conda create -n mouselegacy --file mouse.yml
conda activate mouse
```
You might also need to install pandas manually:
```bash
pip install pandas
```

# Modify file path
Open ```train.py``` and go to line 137 (where ```replace.replace_nature_visual_encoder``` is called).
Update the path to point to the location of ```encoders.py``` in your conda environment.

💡 Tip: The ```encoders.py``` file is usually located in your conda environment’s working directory. For example: ```/miniconda3/envs/mouse/lib/python3.8/site-packages/mlagents/trainers/torch```



# Run script
## Training
```bash
python train.py --runs-per-network 1 --env RandomTrain --network neurips,simple,fully_connected,resnet,alexnet
```
## Evaluating
```bash
python evaluate.py --model "/Users/<your_username>/path/to/your_model.onnx" --log-name "example.txt" --episodes 10
```
❗ Important:
Replace ```/Users/<your_username>/path/to/your_model.onnx``` with the full path to your own ONNX model file on your machine.



