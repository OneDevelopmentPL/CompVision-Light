# Quickstart

## 1. Clone the repository

```bash
git clone https://github.com/OneDevelopmentPL/CompVision-Light.git
cd CompVision-Light```

## 2. Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
## 3. Install dependencies (CPU-only)
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install opencv-python-headless ultralytics```

## 4. Run
```bash
python compvisionlight-core.py
```
