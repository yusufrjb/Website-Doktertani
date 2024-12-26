# prediction/forms.py

from django import forms

class SymptomForm(forms.Form):
    symptoms = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'horizontal-list', 'style': 'column-count: 3;'}),  # Atur jumlah kolom
        label='Pilih gejala (maksimal 5 gejala penyakit cabai)',
    )

    def __init__(self, *args, **kwargs):
        gejala_list = kwargs.pop('gejala_list', [])
        super(SymptomForm, self).__init__(*args, **kwargs)
        self.fields['symptoms'].choices = [(gejala, gejala) for gejala in gejala_list]

    def clean_symptoms(self):
        symptoms = self.cleaned_data.get('symptoms')
        if len(symptoms) > 5:
            raise forms.ValidationError("Anda hanya dapat memilih maksimal 5 gejala.")
        return symptoms
