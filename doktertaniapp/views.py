from django.shortcuts import render

def detect(request):
    return render(request,'option.html')

def home(request):
    return render(request, 'index.html')

# prediction/views.py
from django.shortcuts import render
from django.conf import settings
import pickle
from .forms import SymptomForm
import os

# Load the models
with open(os.path.join(settings.BASE_DIR, 'static', 'ML', 'cabe_model_plant_conditions.pkl'), 'rb') as f:
    df_plant_conditions = pickle.load(f)

with open( os.path.join(settings.BASE_DIR, 'static', 'ML', 'cabe_model_diseases.pkl'), 'rb') as f:
    df_diseases = pickle.load(f)

with open(os.path.join(settings.BASE_DIR, 'static', 'ML', 'cabe_model_rules.pkl'), 'rb') as f:
    df_rules = pickle.load(f)

def predict_disease(symptoms):
    matching_conditions = set(df_plant_conditions[df_plant_conditions['gejala'].isin(symptoms)]['kode_gejala'])

    predicted_diseases = set()
    for index, row in df_rules.iterrows():
        condition_codes = row['condition_disease'][0]
        disease_code = row['condition_disease'][1]

        if set(condition_codes) == matching_conditions:
            predicted_diseases.add(disease_code)

    if predicted_diseases:
        return list(predicted_diseases)
    else:
        return ["Penyakit tidak ditemukan"]

# prediction/views.py

def index(request):
    gejala_list = df_plant_conditions['gejala'].tolist()

    if request.method == "POST":
        form = SymptomForm(request.POST, gejala_list=gejala_list)
        if form.is_valid():
            symptoms = form.cleaned_data['symptoms']
            predicted_diseases = predict_disease(symptoms)
            if predicted_diseases != ["Penyakit tidak ditemukan"]:
                diseases_names = df_diseases[df_diseases['kode_penyakit'].isin(predicted_diseases)]['penyakit'].tolist()
                return render(request, 'predict.html', {'form': form, 'prediksi_penyakit': diseases_names})
            else:
                return render(request, 'predict.html', {'form': form, 'prediksi_penyakit': predicted_diseases})
    else:
        form = SymptomForm(gejala_list=gejala_list)
    return render(request, 'predict.html', {'form': form, 'gejala_list': gejala_list})

