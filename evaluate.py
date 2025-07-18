# evaluate.py

import argparse
import subprocess
from pathlib import Path
from train import summarize_log
import os
import sys


def parse_args():
    p = argparse.ArgumentParser(description="Evaluate an ONNX model on MouseVsAI")
    p.add_argument("--model", required=True,
                   help="Path to the trained ONNX model file")
    p.add_argument("--episodes", type=int, default=50,
                   help="Number of episodes to run in inference")
    p.add_argument("--env", type=str, default="RandomTest",
                   help="Build folder name under ./Builds/")
    p.add_argument("--log-name", required=True,
                   help="Base name for the output log file")
    return p.parse_args()

def main():
    
    args = parse_args()
    args.model = os.path.abspath(args.model)
    model_path = Path(args.model)

    if not model_path.is_file():
        print(f"[ERROR] Model file not found: {model_path}  \n"
              "        Please pass a valid path with --model.")
        sys.exit(1)   

    env_path = Path(f"./Builds/{args.env}")
    exe = os.path.join(env_path,f"{args.env}.app/Contents/MacOS/2D go to target v1")

    if not Path(exe).is_file():
        print(f"[ERROR] Unity executable not found: {exe}")
        sys.exit(1)
    
    # Prepare the Unity log filename
    log_fn = f"{args.log_name}_test.txt"
    #sa = env_path / "2D go to target v1_Data" / "StreamingAssets" / "currentLog.txt"

    sa = os.path.join(env_path,
                    f"{args.env}.app",
                    "Contents",
                    "Resources",
                    "Data",
                    "StreamingAssets",
                    "currentLog.txt")
    
    with open(sa, "w") as f:
        f.write(log_fn)
    # Run in inference-only mode
    cmd = [
        str(exe),
        f"--model={args.model}",
        f"--episodes={args.episodes}",
        # you can also add "-batchmode", "-nographics" here if desired
    ]
    print("[EVAL] Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)

    # Now summarize
    logs_dir = Path(f"./Builds/{args.env}/logfiles")
    logs_dir.mkdir(exist_ok=True)
    summary_path = logs_dir / log_fn
    print(f"\n=== Evaluation Summary ({log_fn}) ===")
    summarize_log(str(summary_path))

if __name__ == "__main__":
    main()
