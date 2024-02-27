from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
 
from predictor.forms import HeartDiseaseForm

def heart(request):
    # Read the heart disease training data from a CSV file
    df = pd.read_csv('static/Heart_train_dataset.csv')
    data = df.values
    X = data[:, :-1]  # Input features (all columns except the last one)
    Y = data[:, -1:]  # Target variable (last column)

    value = ''
    form = HeartDiseaseForm(request.POST or None)  # Initialize the form

    if request.method == 'POST' and form.is_valid():
        # Retrieve the user input from the form
        male = form.cleaned_data['male']
        age = form.cleaned_data['age']
        education = form.cleaned_data['education']
        currentSmoker = form.cleaned_data['currentSmoker']
        cigsPerDay = form.cleaned_data['cigsPerDay']
        BPMeds = form.cleaned_data['BPMeds']
        prevalentStroke = form.cleaned_data['prevalentStroke']
        prevalentHyp = form.cleaned_data['prevalentHyp']
        diabetes = form.cleaned_data['diabetes']
        totChol = form.cleaned_data['totChol']
        sysBP = form.cleaned_data['sysBP']
        diaBP = form.cleaned_data['diaBP']
        BMI = form.cleaned_data['BMI']
        heartRate = form.cleaned_data['heartRate']
        glucose = form.cleaned_data['glucose']

        # Create a numpy array with the user's data
        user_data = np.array(
            (male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose)
        ).reshape(1, -1)

        # Create and train a Random Forest Classifier model
        rf = RandomForestClassifier(
            n_estimators=16,
            criterion='entropy',
            max_depth=9
        )

        rf.fit(np.nan_to_num(X), Y.ravel())  # Train the model using the training data
        rf.score(np.nan_to_num(X), Y.ravel())  # Evaluate the model's accuracy
        predictions = rf.predict(user_data)  # Make predictions on the user's data

        if int(predictions[0]) == 1:
            value = 'have'  # User is predicted to have heart disease
        elif int(predictions[0]) == 0:
            value = "don't have"  # User is predicted to not have heart disease

    return render(request,
                  'heart.html',
                  {
                      'context': value,
                      'title': 'Heart Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'heart': True,
                      'form': form,
                  })

def home(request):
    return render(request,
                  'home.html')
