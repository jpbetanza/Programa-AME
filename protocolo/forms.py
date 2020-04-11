from django import forms
from .models import exercicios_model

class exercicios(forms.ModelForm):
    Vezes_Semana_FC = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_FC = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_FP = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_FP = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_FS = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_FS = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_HB = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_HB = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_BB = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_BB = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_PS = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_PS = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_ATL = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_ATL = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_NAT = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_NAT = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_GO = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_GO = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_AM = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_AM = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_DAN = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_DAN = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_COR = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_COR = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_BIC = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_BIC = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_CE = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_CE = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_CT = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_CT = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_VQ = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_VQ = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_VP = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_VP = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_QP = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_QP = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_SB = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_SB = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_MC = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_MC = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_EF = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_EF = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_TC = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_TC = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_PC = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_PC = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_GA = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_GA = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Vezes_Semana_OA = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Minutos_Dia_OA = forms.IntegerField(widget=forms.NumberInput, label='', required=False)
    Nao_pratico_AF = forms.BooleanField(label='Não pratico atividades físicas', required=False)
    class Meta:
        model = exercicios_model
        
        fields = (
           
            'Vezes_Semana_FC',
            'Minutos_Dia_FC',
            
            'Vezes_Semana_FP',
            'Minutos_Dia_FP',

            'Vezes_Semana_FS',
            'Minutos_Dia_FS',
            
            'Vezes_Semana_HB',
            'Minutos_Dia_HB',
            
            'Vezes_Semana_BB',
            'Minutos_Dia_BB',
            
            'Vezes_Semana_PS',
            'Minutos_Dia_PS',
            
            'Vezes_Semana_ATL',
            'Minutos_Dia_ATL',
            
            'Vezes_Semana_NAT',
            'Minutos_Dia_NAT',
            
            'Vezes_Semana_GO',
            'Minutos_Dia_GO',
            
            'Vezes_Semana_AM',
            'Minutos_Dia_AM',
            
            'Vezes_Semana_DAN',
            'Minutos_Dia_DAN',
            
            'Vezes_Semana_COR',
            'Minutos_Dia_COR',
            
            'Vezes_Semana_BIC',
            'Minutos_Dia_BIC',
            
            'Vezes_Semana_CE',
            'Minutos_Dia_CE',
            
            'Vezes_Semana_CT',
            'Minutos_Dia_CT',
            
            'Vezes_Semana_VQ',
            'Minutos_Dia_VQ',
            
            'Vezes_Semana_VP',
            'Minutos_Dia_VP',
            
            'Vezes_Semana_QP',
            'Minutos_Dia_QP',
            
            'Vezes_Semana_SB',
            'Minutos_Dia_SB',
            
            'Vezes_Semana_MC',
            'Minutos_Dia_MC',
            
            'Vezes_Semana_EF',
            'Minutos_Dia_EF',
            
            'Vezes_Semana_TC',
            'Minutos_Dia_TC',
            
            'Vezes_Semana_PC',
            'Minutos_Dia_PC',
            
            'Vezes_Semana_GA',
            'Minutos_Dia_GA',
            
            'Vezes_Semana_OA',
            'Minutos_Dia_OA',
            
            'Nao_pratico_AF'
            )