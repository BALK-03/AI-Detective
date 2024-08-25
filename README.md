![classify_ai_image_real](https://github.com/user-attachments/assets/d3d64a53-a507-482a-9c19-3ec1e43f66f4)

AI vs. Real Image Classification
---------------------
This project aims to distinguish between AI-generated images and real ones using convolutional neural networks techniques. The model was trained on a curated dataset of AI-generated and real images, and the goal is to classify whether a given image is AI-generated or real.




Model Performance
---------------------
- *Model's Accuracy*: 0.93
- *Model's Precision*: 0.93
- *Model's Recall*: 0.92
- *Model's F1 Score*: 0.92




Project Structure
---------------------
The project is organized as follows :

    ├── data
    │   │
    │   └── data.txt                <- File containing the data source
    │
    ├── models                      <- Folder containing trained model
    │
    ├── notebooks                   
    │   └── model.ipynb             <- Jupyter notebook used to train and evaluate the model                  
    │                         
    ├── requirements.txt            <- The requirements file for reproducing the analysis environment
    │                                  generated with `pip freeze > requirements.txt`
    │
    └── src                         <- Source code for use in this project
        ├── data                    
        │   └── preprocess_data.py  <- Script to preprocess data
        │   
        └── models                  
            └── make_prediction.py  <- Script to make predictions, add your example picture path and run




How to Run the Project
---------------------
1. *Open Command Prompt*<br>
2. *Navigate to your desired directory*<br>
`cd C:\Users\user\Desktop`
3. *Clone the project repository from GitHub*<br>
`git clone https://github.com/BALK-03/AI-Detective.git`
4. *Navigate to the project directory*<br>
`cd AI-Detective`
5. *Set up a virtual environment, python 3.11 required for package compatibility*<br>
`py -3.11 -m venv .venv`
6. *Activate the virtual environment*<br>
`".venv/scripts/activate"`
7. *Install project dependencies*<br>
`pip install -r requirements.txt`
8. *Run the model to make a prediction, replace "PATH/TO/YOUR/IMAGE.jpg" with the actual path to your image*<br>
`python src/models/make_prediction.py "PATH/TO/YOUR/IMAGE.jpg"`
