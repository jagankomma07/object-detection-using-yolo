# Object Detection with YOLOv11

<img src='./images/object-detection-examples.avif' alt="Object Detection Examples" style="max-width:100%; height:auto;">

## YOLOv11n Model

To get started, download the YOLOv11 model from the following link: [Download YOLOv11](https://huggingface.co/Ultralytics/YOLO11/tree/main).

## Project Folder Structure (Post-Setup) 📁

This section outlines the directory structure of the project after setup, providing a clear overview of the organization of files and folders.

📁 object-detection  
│── 📁 images <span style="opacity: 0.3;"># Contains server images (Used in README.md)</span>  
│── 📁 models <span style="opacity: 0.3;"># Directory for trained CNN models</span>  
│── 📁 detection <span style="opacity: 0.3;"># Contains modular code files.</span>  
│── 📁 venv/ <span style="opacity: 0.3;"># Virtual environment (excluded from version control)</span>  
│── 📁 output/ <span style="opacity: 0.3;"># Contains results after detection</span>  
│── 📜 .gitignore <span style="opacity: 0.3;"># Specifies files and directories to ignore in Git</span>  
│── 📜 README.md <span style="opacity: 0.3;"># Comprehensive project documentation</span>  
│── 📜 requirements.txt <span style="opacity: 0.3;"># Lists all project dependencies</span>  
│── 📜 server.py <span style="opacity: 0.3;"># Streamlit application for glaucoma detection</span>

### YOLOv11 Models: Performance and Statistics

| Model                                                                                | Size<br><sup>(pixels)</sup> | mAP<sup>val<br>50-95</sup> | Speed<br><sup>CPU ONNX<br>(ms)</sup> | Speed<br><sup>T4 TensorRT10<br>(ms)</sup> | Parameters<br><sup>(M)</sup> | FLOPs<br><sup>(B)</sup> |
| ------------------------------------------------------------------------------------ | --------------------------- | -------------------------- | ------------------------------------ | ----------------------------------------- | ---------------------------- | ----------------------- |
| [YOLO11n](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt) | 640                         | 39.5                       | 56.1 ± 0.8                           | 1.5 ± 0.0                                 | 2.6                          | 6.5                     |
| [YOLO11s](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11s.pt) | 640                         | 47.0                       | 90.0 ± 1.2                           | 2.5 ± 0.0                                 | 9.4                          | 21.5                    |
| [YOLO11m](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11m.pt) | 640                         | 51.5                       | 183.2 ± 2.0                          | 4.7 ± 0.1                                 | 20.1                         | 68.0                    |
| [YOLO11l](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11l.pt) | 640                         | 53.4                       | 238.6 ± 1.4                          | 6.2 ± 0.1                                 | 25.3                         | 86.9                    |
| [YOLO11x](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11x.pt) | 640                         | 54.7                       | 462.8 ± 6.7                          | 11.3 ± 0.2                                | 56.9                         | 194.9                   |

## 🛠️ How to Set Up This Project

This guide will help you set up the project's environment seamlessly.

**<u>1. Install Python</u> 🐍**

If you haven't installed Python yet, visit the official download page: [Python Download Guide](https://wiki.python.org/moin/BeginnersGuide/Download) and follow the instructions for your operating system (Windows, macOS, or Linux).

**<u>2. Create a Virtual Environment</u>**

1. Creating a virtual environment:

   - In the terminal, run this command:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - To activate the virtual environment, use:

   ```bash
   .\venv\Scripts\activate
   ```

**3. Clone the Repository 📥**

1. Open your Git client or terminal.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command, replacing `<repository_url>` with the actual URL of the project's repository:

```bash
git clone <repository_url>
```

**3. Install required Dependencies 📦**

1. Open terminal/cmd.
2. Navigate to repo directory
3. Run the following command to install dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

**4. Host the project Locally 🌐**

- After installing the required dependencies, run the following command to start the project locally:

```bash
streamlit run ./server.py
```
