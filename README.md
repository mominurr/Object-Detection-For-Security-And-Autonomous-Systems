# Object Detection for Security and Autonomous Systems

## 📌 Overview
This project focuses on developing an **object detection model** using **Fastai**, capable of accurately classifying images into **11 distinct categories**. The model is designed to enhance security, surveillance, and autonomous systems, enabling object identification for critical decision-making.

## 🎯 Objectives
- Train a deep learning model for object classification.
- Improve accuracy and efficiency for object detection.
- Deploy the model using **Gradio** on **Hugging Face** for easy accessibility.

## 🚀 Use Cases
- **Security & Surveillance**: Detect humans, vehicles, and potential threats.
- **Autonomous Vehicles**: Identify obstacles such as cars, trucks, and pedestrians.
- **Aviation Safety**: Recognize aircraft and airborne hazards like birds.

## 🏷️ Categories for Detection
- **Human**
- **Airplane**
- **Automobile**
- **Bird**
- **Cat**
- **Deer**
- **Dog**
- **Frog**
- **Horse**
- **Ship**
- **Truck**

## ⚙️ Technologies Used
- **Python** 🐍
- **Fastai** 🏎️
- **Gradio** 🎛️
- **Hugging Face** 🤗
- **Jupyter Notebook** 📓
- **icrawler** 🌍 (for dataset downloading from Bing search engine crawling)

## 📊 Model Training & Evaluation
- **Dataset:** Custom dataset with images labeled into 11 categories. Dataset downloading from Bing search engine crawling.
- **Preprocessing:** Image augmentation, normalization, and dataset balancing.
- **Architecture:** Fastai-based transfer learning model for improved accuracy.
- **Training Strategy:** The model utilizes a **ResNet34 architecture** and undergoes fine-tuning with **three training epochs** to optimize accuracy.
- **Metrics:** error_rate, accuracy

### 3rd Time Training Result:
```
epoch	train_loss	valid_loss	error_rate	accuracy	time
0	    0.617954	0.029938	0.010135	0.989865	06:55
epoch	train_loss	valid_loss	error_rate	accuracy	time
0	    0.095386	0.070000	0.016892	0.983108	01:35
1	    0.089504	0.049305	0.013514	0.986486	01:35
2	    0.046270	0.043154	0.010135	0.989865	01:35
```

### Dependencies for All Notebooks:
```bash
!pip install -Uqq fastai fastbook nbdev icrawler
```

## 🌍 Deployment
The trained model is deployed using **Gradio** on **Hugging Face** for easy access and real-time testing.

🔗 **[HuggingFace Spaces App Live URL](https://huggingface.co/spaces/developermominur/Object-Detection-for-Security-and-Autonomous-Systems)**

### Deployed Model Testing Image Result
<p align="center">
  <img src="deployed_model_result\huggingface_deployed_project_detection_result.png" width="45%">
  <img src="deployed_model_result\huggingface_deployed_project.png"width="45%">
</p>

### API-Based Webpage
A **webpage** is being developed where users can **interact with the deployed model** through an **API**, allowing them to upload images and receive real-time classification results or detection outcomes..

🔗 **[Webpage Live URL](#)**


## 📝 Setup Instructions
### 1️⃣ Clone Repository
```bash
git clone https://github.com/mominurr/Object-Detection-for-Security-and-Autonomous-Systems.git
cd Object-Detection-for-Security-and-Autonomous-Systems
```

### 2️⃣ Install Dependencies
```bash
pip install -Uqq fastai fastbook nbdev icrawler
```

### 3️⃣ Run Model Inference
```bash
cd notebook
jupyter notebook
```
Open `inference.ipynb` and run all cells.

### 4️⃣ Deploy Model (Optional)
```bash
cd deployment
python app.py
```

## 🔬 Testing
- Use images from `test_images/` to validate model performance.
- Modify `test_download_dir/` for image downloading tests.
- Run `inference.ipynb` to evaluate real-world detection.

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

## 🛠️ Contributions
We welcome contributions! Feel free to fork the repository and submit a pull request.

## 📩 Contact
For any inquiries or collaborations:
- **Portfolio:** [mominur.dev](https://mominur.dev)
- **GitHub:** [github.com/mominurr](https://github.com/mominurr)
- **LinkedIn:** [linkedin.com/in/mominur--rahman](https://www.linkedin.com/in/mominur--rahman/)
- **Email:** mominurr518@gmail.com

🚀 **Star this repo** ⭐ if you find it useful!
