from django import forms

class HeartDiseaseForm(forms.Form):
    # Define form fields for heart disease prediction
    male = forms.IntegerField(label='Male', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter 1 for male, 0 for female'}))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}))
    education = forms.FloatField(label='Education', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter education level'}))
    currentSmoker = forms.IntegerField(label='Current Smoker', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter 1 for yes, 0 for no'}))
    cigsPerDay = forms.FloatField(label='Cigarettes Per Day', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of cigarettes per day'}))
    BPMeds = forms.FloatField(label='BP Medication', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter 1 for yes, 0 for no'}))
    prevalentStroke = forms.IntegerField(label='Prevalent Stroke', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter 1 for yes, 0 for no'}))
    prevalentHyp = forms.IntegerField(label='Prevalent Hypertension', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter 1 for yes, 0 for no'}))
    diabetes = forms.IntegerField(label='Diabetes', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter 1 for yes, 0 for no'}))
    totChol = forms.FloatField(label='Total Cholesterol', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter total cholesterol level'}))
    sysBP = forms.FloatField(label='Systolic Blood Pressure', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter systolic blood pressure'}))
    diaBP = forms.FloatField(label='Diastolic Blood Pressure', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter diastolic blood pressure'}))
    BMI = forms.FloatField(label='Body Mass Index (BMI)', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter BMI'}))
    heartRate = forms.FloatField(label='Heart Rate', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter heart rate'}))
    glucose = forms.FloatField(label='Glucose Level', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter glucose level'}))


    