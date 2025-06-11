import os
import shutil
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")
    data_yaml = r"data.yaml" #put your data.yml path file

    # === Entraînement ===
    results = model.train(
        data=data_yaml,
        epochs=25,
        imgsz=320,
        batch=64,
        device='cpu',
        workers=0,
        verbose=True
    )

    # trained model
    trained_model_path = model.ckpt_path if hasattr(model, 'ckpt_path') else 'runs/detect/train/weights/best.pt'

    # add here your path for model saving
    destination_path = r"C:\Users\21654\Desktop\animals_detection\animal_detection\yolo_data\yolo_animal_model.pt"
    
    # copy your saved model
    if os.path.exists(trained_model_path):
        shutil.copy(trained_model_path, destination_path)
        print(f"[INFO] Modèle entraîné sauvegardé dans : {destination_path}")
    else:
        print(f"[ERREUR] Modèle introuvable à : {trained_model_path}")

if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()
    main()
