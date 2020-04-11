from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
class stroop(models.Model):
    cod = models.CharField(max_length=5)
    acertos1 = models.IntegerField()
    acertos2 = models.IntegerField()
    acertos3 = models.IntegerField()
    tempo1 = models.CharField(max_length=7)
    tempo2 = models.CharField(max_length=7)
    tempo3 = models.CharField(max_length=7)

    def __str__(self):
        return self.cod + ', ' + self.acertos1 + ', '+ self.acertos2 + ', '+ self.acertos3 + ', '+ self.tempo1 + ', '+ self.tempo2 + ', '+ self.tempo3

class exercicios_model(models.Model):
    cod = models.CharField(max_length=5)

    Vezes_Semana_FC = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_FC = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_FP = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_FP = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_FS = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_FS = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_HB = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_HB = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_BB = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_BB = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_PS = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_PS = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_ATL = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_ATL = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_NAT = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_NAT = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_GO = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_GO = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_AM = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_AM = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_DAN = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_DAN = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_COR = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_COR = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])
    
    Vezes_Semana_BIC = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_BIC = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_CE = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_CE = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_CT = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_CT = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_VQ = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_VQ = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_VP = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_VP = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_QP = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_QP = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_SB = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_SB = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_MC = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_MC = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_EF = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_EF = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_TC = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_TC = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_PC = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_PC = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_GA = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_GA = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Vezes_Semana_OA = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="O valor precisa estar entre 0 e 7"), MaxValueValidator(7,message="O valor precisa estar entre 0 e 7")])
    Minutos_Dia_OA = models.IntegerField(null=True, blank=True, default=0, validators=[MinValueValidator(0,message="Por favor, seja realista"), MaxValueValidator(960,message="Por favor, seja realista")])

    Nao_pratico_AF = models.BooleanField()