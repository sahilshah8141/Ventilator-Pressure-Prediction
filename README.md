<h1 align="center">
    <p>Ventilator-Pressure-Prediction</p>
</h1>

<p align="center">
    <a href="" alt="License">
        <img src="https://img.shields.io/badge/license-MIT-blue" />
    </a>
    <a href="" alt="Python Version">
        <img src="https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-blue?logo=python" />
    </a>
</p> 

## 📝 Description
- In this project, I have used the **Random Forest** model for ventilator pressure prediction.
- You can check out the deployed web application on the  http://ventilatorpressure.herokuapp.com/

## ⏳ Dataset
- For the training, I have used the dataset of the Kaggle competition hosted by Google brains.
- You can check out the competition by below-mentioned link: https://www.kaggle.com/c/ventilator-pressure-prediction/data

## :desktop_computer: Download Pre-trained Model
I have uploaded the whole model on github with git lfs and you just have to run below command :-
```bash
$  git lfs pull --include=models/random_forest_model_lower_data.joblib

```

## :gear: Setup
There are two requirements files for the specific web-application deployment and one for the Model training Notebook.
 
1. Install the dependencies for the web application:-
```bash
$ pip install -r requirements.txt

```
2. Install the dependencies for the training notebook:-
```bash
$ pip install -r notebook-requirements.txt

```
