Project Organization
---------------------

├── data
│   │
│   ├── train-real.csv          <- CSV file for real training data
│   ├── train-fakes.csv         <- CSV file for fake training data
│   ├── test-real.csv           <- CSV file for real test data
│   └── test-fake.csv           <- CSV file for fake test data
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