# MacOS Training Guide

Welcome to **Mouse vs. AI: Robust Visual Foraging Challenge @ NeurIPS 2025**

This is a training guide for **MacOS**. For other operating systems, please check:
[Windows](https://github.com/robustforaging/mouse_vs_ai_windows?tab=readme-ov-file#windows-training-guide) and [Linux](https://github.com/robustforaging/mouse_vs_ai_linux/tree/main?tab=readme-ov-file#linux-training-guide)

# Create conda environment
Open Terminal and navigate to the directory where you want to download the project.

Clone the repository from GitHub:
```bash
git clone https://github.com/robustforaging/mouse_vs_ai_macOS.git
cd mouse_vs_ai_macOS
```

Then, create and activate the conda environment:
```bash
CONDA_SUBDIR=osx-64 conda env create -n mouse --file mouse.yml
conda activate mouse
```

#  Give Permission to a macOS App
```bash
# Make the app's binary executable
chmod +x ./Builds/RandomTrain/RandomTrain.app/Contents/MacOS/*

# Remove the 'quarantine' flag applied by macOS (for downloaded apps)
xattr -dr com.apple.quarantine ./Builds/RandomTrain/RandomTrain.app
```
❗ Important:
Replace ./Builds/RandomTrain/RandomTrain.app with the actual path to your .app bundle in both commands.
You need to run these commands for each app you intend to execute if macOS flags it.


# Modify file path
Open ```train.py``` and go to line 137 (where ```replace.replace_nature_visual_encoder``` is called).
Update the path to point to the location of ```encoders.py``` in your conda environment.

💡 Tip: The ```encoders.py``` file is usually located in your conda environment’s working directory. For example: ```/miniconda3/envs/mouse/lib/python3.8/site-packages/mlagents/trainers/torch```



# Run script
## Training
```text
Usage: python train.py [options]

Training options:
  --runs-per-network R    Number of runs per network (default: 5)
  --env ID                Run identifier (default: Normal) [defines type of environment]
  --network N1,N2,N3     Comma-separated list of networks to train
                         (default choices: ['fully_connected', 'nature_cnn', 'simple', 'resnet'])
```

Example command for training:
```bash
python train.py --runs-per-network 1 --env RandomTrain --network neurips,simple,fully_connected,resnet,alexnet
```
## Evaluating
```text
Usage: python evaluate.py [options]

Evaluation options:
  --model      Path to the trained ONNX model file
  --episodes   Number of episodes to run in inference(default: 50)
  --env        Build folder name under ./Builds/
  --log-name   Base name for the output log file
```

Example command for evaluation:
```bash
python evaluate.py --model "/Users/<your_username>/path/to/your_model.onnx" --log-name "example.txt" --episodes 10
```
❗ Important:
Replace ```/Users/<your_username>/path/to/your_model.onnx``` with the full path to your own ONNX model file on your machine.



