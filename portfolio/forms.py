from django import forms
from .models import Skills

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['label', 'level']
        widgets = {
            'label': forms.TextInput(
                attrs={
                    'class': 'form-label',
                    'placeholder': 'Libellé de la compétence'
                }
            ),
            'level': forms.NumberInput(
                attrs={
                    'class': 'form-label',
                    'placeholder': 'Pourcentage de maîtrise'
                }
            )
        }

 
    def clean_label(self):
        label = self.cleaned_data['label'] 
        if not label:
            raise forms.ValidationError('Le libellé ne doit pas être vide.')
        return label

    # Validation personnalisée pour le champ 'level'
    def clean_level(self):
        level = self.cleaned_data['level']  
        if level is None:  
            raise forms.ValidationError('Vous ne pouvez pas créer une compétence sans niveaux de compétence.')
        
        if level < 0 or level > 100:  
            raise forms.ValidationError("Le niveau doit être compris entre 0 et 100.")
        
        return level
