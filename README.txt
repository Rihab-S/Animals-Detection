
🐾 Animal Detection with YOLOv8n
================================

This project uses the Ultralytics YOLOv8n model to detect and classify animals in images using a custom dataset.

📁 Dataset
----------
The training dataset is hosted on Hugging Face:
## 📦 Dataset Download (Hosted on Hugging Face)

- [animals_train.zip](https://huggingface.co/datasets/Rihab-s/animals_data_set/resolve/main/animals_train.zip)
- [animals_val.zip](https://huggingface.co/datasets/Rihab-s/animals_data_set/resolve/main/animals_val.zip)
The dataset follows the YOLO format and is described in the data.yaml file.

📦 Requirements
---------------
- Python 3.8+
- Git
- Ultralytics YOLOv8
- Optionally: Git LFS (if handling large files)

Install the dependencies:

    pip install ultralytics

🚀 Training with YOLOv8n
------------------------
The script 'train_yolo.py' trains the yolov8n.pt (nano) model on your custom dataset.

▶️ Run training

    python train_yolo.py

Training parameters:
- Model: yolov8n.pt (lightweight, CPU-friendly)
- Epochs: 25
- Image size: 320x320
- Batch size: 64
- Device: CPU

At the end of training, the best model weights are automatically copied to:

    C:\Users\21654\Desktop\animals_detection\animal_detection\yolo_data\yolo_animal_model.pt

📝 Project Structure
--------------------
    train_yolo.py                  # Training script
    data.yaml                      # YOLO dataset config
    yolo_animal_model.pt           # Trained model (output)
    yolo_data/
        ├── images/
        └── labels/

💡 Notes
--------
- This project is configured for CPU-only training. For GPU training, change device='cpu' to device=0.
- To use large files (>100 MB), consider using Git LFS.
- For large datasets or trained models, you can also use Hugging Face to store them.

📬 Author
---------
Rihab Souissi
PhD in Information and Communication Technologies
Freelance Data Scientist & ML Engineer
GitHub: https://github.com/Rihab-S
Hugging Face: https://huggingface.co/Rihab-s

📖 References
-------------
- https://docs.ultralytics.com/
- https://docs.ultralytics.com/datasets/detect/
- https://git-lfs.com/
- https://huggingface.co/docs/datasets




