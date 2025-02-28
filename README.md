
# Face Parts and Mask Detection
![Python](https://img.shields.io/badge/Python-3.7%2B-blue) 
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green) 
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)

This Python project detects facial features (eyes, nose, mouth) and determines whether a person is wearing a face mask. It uses **OpenCV** for face detection and **Haar Cascades** or **DNN models** for facial feature detection. For mask detection, a pre-trained deep learning model (e.g., TensorFlow/Keras) is used.

---

## Features

- **Face Detection**: Detects faces in real-time using a webcam or from an image.
- **Facial Feature Detection**: Identifies key facial features such as eyes, nose, and mouth.
- **Face Mask Detection**: Classifies whether a person is wearing a mask or not.
- **Real-Time Support**: Works with live video streams or static images.

---

## Requirements

To run this project, you need the following dependencies:

- Python 3.7 or higher
- OpenCV (`opencv-python`)
- TensorFlow (for mask detection)
- NumPy
- Matplotlib (optional, for visualization)

You can install the required libraries using:

```bash
pip install opencv-python tensorflow numpy matplotlib
```

---

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/face-parts-mask-detection.git
   cd face-parts-mask-detection
   ```

2. **Run the Script**:
   - For face parts detection:
     ```bash
     python face_parts_detection.py
     ```
   - For face mask detection:
     ```bash
     python mask_detection.py
     ```

3. **Input Options**:
   - Use a webcam for real-time detection.
   - Provide an image path for static image detection.

---

## How It Works

1. **Face Detection**:
   - The system uses OpenCV's Haar Cascade or a pre-trained DNN model to detect faces in the input.

2. **Facial Feature Detection**:
   - Facial landmarks (eyes, nose, mouth) are detected using Haar Cascades or a facial landmark detection model.

3. **Mask Detection**:
   - A pre-trained deep learning model (e.g., MobileNetV2) is used to classify whether the detected face is wearing a mask.

---

## Project Structure

```
face-parts-mask-detection/
├── models/                  # Pre-trained models for mask detection
├── haarcascades/            # Haar Cascade files for face and feature detection
├── face_parts_detection.py  # Script for detecting facial features
├── mask_detection.py        # Script for mask detection
├── README.md                # Project documentation
└── requirements.txt         # List of dependencies
```

---

## Results

- **Face Parts Detection**:
  ![Face Parts Detection](Outputs)

- **Mask Detection**:
  ![Mask Detection](Outputs)

---

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

 Acknowledgments
- OpenCV for face detection and feature extraction.
- TensorFlow/Keras for the mask detection model.
- Pre-trained models and datasets used in this project.
