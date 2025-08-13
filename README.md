# Training Guide

Welcome to **Mouse vs. AI: Robust Visual Foraging Challenge @ NeurIPS 2025**

## Linux

### Install conda

Open command prompt:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Press ```ENTER``` or type ```yes``` when prompted

### Create conda environment

Open command prompt and navigate to the directory where you want to download the project.

Clone the repository from GitHub:

```bash
git clone https://github.com/danorel/mousewise.git
cd mousewise
```

Then, create and activate the conda environment:

```bash
conda env create -n mouse -f environment/linux/mouse.yml
conda activate mouse
``` 

💡 Troubleshooting: if the CUDA version isn’t compatible with your GPU, please try: 

```bash
pip install torch==1.8.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
```

### Set executable permissions for Linux binariesPermalink

To make the Linux executable files executable:
```bash
chmod +x ./builds/linux/RandomTrain/LinuxHeadless.x86_64

# If you have other build directories, make their executables executable too. For example:
# chmod +x ./builds/linux/RandomTest/LinuxHeadless.x86_64
```

### Modify file path

Open ```train.py``` and go to where ```replace.replace_nature_visual_encoder``` is called.
Update the path to point to the location of ```encoders.py``` in your conda environment.

📝 Note: The ```encoders.py``` file is usually located in your conda environment’s working directory. For example: ```~/miniconda3/env/mouse2/Lib/site-packages/mlagents/trainers/torch/encoders.py```

### Run script

#### Training

```text
Usage:  [options]

Training options:
  --runs-per-network R    Number of runs per network (default: 5)
  --env ID                Run identifier (default: Normal) [defines type of environment]
  --network N1,N2,N3     Comma-separated list of networks to train
                         (default choices: ['fully_connected', 
                         'nature_cnn', 'simple', 'resnet'])
                          You can specify your own custom networks here as 
                          well. Just list their names, separated by commas.
```

Example command for training:

```bash
python train.py --runs-per-network 1 --env RandomTrain --network MyNetwork1, MyNetwork2
```

- 💡 Troubleshooting: If training only proceeds after pressing ```ENTER```, try running the command with unbuffered output mode:  ```python -u train.py [options]``` 
- If the issue persists, stop the current training episode and train again

#### Evaluating

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
python evaluate.py --model "/path/to/your_model.onnx" --log-name "example.txt" --episodes 10
```

### Customize the model

- To add architecture: 
  - Add your model (e.g., `MyNetwork1.py`) to the `/mouse_vs_ai_linux/Encoders` directory
  - To train your custom network, run ```python train.py --network MyNetwork1 [options]```
- To adjust hyperparamters: 
  - Edit parameters in `/mouse_vs_ai_linux/Encoders/nature.yaml` file
  - 📝 Note: Please do not change the name of this file or the parameter `vis_encode_type` in this file. Only modify other configuration values as needed.

After making your changes, run the Python training script as described above.

## MacOS

### Install conda

Open command prompt:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p $HOME/miniconda
```

In order to initialize after the installation process is done, first run ```source <path to conda>/bin/activate``` and then run ```conda init --all```.

### Create conda environment

Open Terminal and navigate to the directory where you want to download the project.

Clone the repository from GitHub:

```bash
git clone https://github.com/danorel/mousewise.git
cd mousewise
```

Then, create and activate the conda environment:

```bash
CONDA_SUBDIR=osx-64 conda env create -n mouse --file environment/macos/mouse.yml
conda activate mouse
```

You may also need to install pandas separately: ```pip install pandas```

### Give permission to a MacOS app

```bash
# Make the app's binary executable
chmod +x ./builds/macos/RandomTrain/RandomTrain.app/Contents/MacOS/*

# Remove the 'quarantine' flag applied by macOS (for downloaded apps)
xattr -dr com.apple.quarantine ./builds/macos/RandomTrain/RandomTrain.app
```

❗ Important:
Replace ```./builds/macos/RandomTrain/RandomTrain.app``` with the actual path to your .app bundle in both commands.

You need to run these commands for each app you intend to execute if macOS flags it.

### Modify file path

Open ```train.py``` and go to line 137 (where ```replace.replace_nature_visual_encoder``` is called).

Update the path to point to the location of ```encoders.py``` in your conda environment.

📝 Note: The ```encoders.py``` file is usually located in your conda environment’s working directory. For example: ```/miniconda3/envs/mouse/lib/python3.8/site-packages/mlagents/trainers/torch```

### Run script

#### Training

```text
Usage: python train.py [options]

Training options:
  --runs-per-network R    Number of runs per network (default: 5)
  --env ID                Run identifier (default: Normal) [defines 
                          type of environment]
  --network N1,N2,N3      Comma-separated list of networks to train
                          (default choices: ['fully_connected', 
                          'nature_cnn', 'simple', 'resnet'])
                          You can specify your own custom networks here as 
                          well. Just list their names, separated by commas.
```

Example command for training:

```bash
python train.py --runs-per-network 1 --env RandomTrain --network nature_cnn
```

#### Evaluating

```text
Usage: python evaluate.py [options]

Evaluation options:
  --model      Path to the trained ONNX model file
  --episodes   Number of episodes to run in inference(default: 50)
  --env        Build folder name under ./builds/
  --log-name   Base name for the output log file
```

Example command for evaluation:

```bash
python evaluate.py --model "/path/to/your_model.onnx" --log-name "example.txt" --episodes 10
```

❗ Important:
Replace ```/path/to/your_model.onnx``` with the full path to your own ONNX model file on your machine.

### Customize the model

- To add architecture: 
  - Add your model (e.g., `MyNetwork1.py`) to the `./encoders` directory
  - To train your custom network, run ```python train.py --network nature_cnn [options]```
- To adjust hyperparamters: 
  - Edit parameters in `./encoders/nature.yaml` file
  - 📝 Note: Please do not change the name of this file or the parameter `vis_encode_type` in this file. Only modify other configuration values as needed.

After making your changes, run the Python training script as described above.
