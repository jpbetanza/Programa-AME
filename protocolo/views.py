from django.shortcuts import render, redirect
from django.contrib import messages
from .models import stroop, exercicios_model
from protocolo.forms import exercicios
# Create your views here.

'''Pagina de utilização geral'''
def Index(request):
    return render(request, 'index.html')

def Stroop2(request,cod):
    resultado = {}
    try:
        print('oi')
        c = stroop.objects.get(cod=cod)
        print('oi2')
        resultado['valores'] = c
        return render(request,'Stroop2.html', resultado)
    except stroop.DoesNotExist:
        messages.error(request,'O teste que você está buscando não existe', extra_tags='text-danger')
        return redirect('/stroop/')

def Stroop1(request,cod):
    if request.method == 'POST':
        data = request.POST.copy()
        tempo1 = data.get('tempo1')
        tempo2 = data.get('tempo2')
        tempo3 = data.get('tempo3')
        acertos1 = data.get('acertos1')
        acertos2 = data.get('acertos2')
        acertos3 = data.get('acertos3')
        try:
            try:
                stroop.objects.get(cod=cod)
                messages.warning(request, 'Você já fez o teste', extra_tags='text-warning')
                print(f'{cod} tentou refazer o teste stroop - pt2')
                return redirect('/stroop')
            except stroop.DoesNotExist:
                c = stroop(cod=cod,tempo1=tempo1,tempo2=tempo2,tempo3=tempo3,acertos1=acertos1,acertos2=acertos2,acertos3=acertos3)
                c.save()
                print(f'Recebemos o Stroop de: {cod}')
                url = '/stroop_resultados/'+cod
                return redirect(url)
        except:
            print(f'Deu algo errado com o Stroop de: {cod}')
            messages.error(request,'Algo deu errado no envio das informações')
            return redirect('/stroop/')
    return render(request, 'Stroop1.html')



def Stroop(request):
    if request.method == 'POST':
        #Pegando os valores do form e copiando-os para uma variável 'data'
        data = request.POST.copy()
        #separando de forma estúpida cada campo recebido
        cod = data.get('codigo')
        #criando um objeto stroop (vindo das models) que armazenará os valores acima e será salvo no banco
        try:
            if (int(cod)) and (int(cod)>=0) and (int(cod)<=9999):
                try:
                    stroop.objects.get(cod=cod)
                    messages.warning(request, 'Você já fez o teste', extra_tags='text-warning')
                    print(f'{cod} tentou refazer o teste stroop')
                except:
                    url = '/stroop_teste/'+ cod
                    return redirect(url)
            else:
                messages.warning(request, 'Digite um código válido',extra_tags='text-danger')
        except:
            messages.warning(request, 'Digite um código válido',extra_tags='text-danger')

    return render(request, 'Stroopm.html')

def StroopTry(request):
    return render(request, 'StroopTry.html')
    
def Form(request):
    return render(request, 'form.html')
    
def Exercicios(request,cod):
    form = exercicios()

    #FUNÇÃO PARA A ELABORAÇÃO DOS CAMPOS A SEREM INSERIDOS NA PÁGINA
    names = ['Futebol de campo','Futebol de praia','Futsal','Handebol','Basquetebol','Patins ou skate','Atletismo','Natação','Ginástica Olímpica','Artes marciais','Dança','Correr','Andar de bicicleta','Caminhar por exercicio','Caminhar como transporte','Volei de quadra','Volei de praia','Queimado ou pular','Surfe ou bodyboard','Musculacao','Exercicios de força','Tenis de campo','Passeio com cão','Ginastica aeróbica','Outras atividades']
    dias = []
    minutos = []
    
    h=0
    for i in form:
        if h%2==0:
            dias.append(i)
            h=h+1
        else:
            minutos.append(i)
            h=h+1
    ultimo = []
    ultimo.append(dias.pop())

    form = []
    for i in range(len(names)):
        dic = {}
        dic['nome']=names[i]
        dic['dia']=dias[i]
        dic['minutos']=minutos[i]
        form.append(dic)
        

    #FIM DA FUNÇÃO

    if request.method == 'POST':
        form = exercicios(request.POST)
        
        try:
            exercicios_model.objects.get(cod=cod)
            messages.warning(request, 'Você já fez o teste',extra_tags='text-warning')
            print(f'{cod} tentou refazer o teste das Atividades físicas - pt2')
            return redirect('/exercicios')
        except exercicios_model.DoesNotExist:
            if form.is_valid():
                fMod = form.save(commit=False)
                fMod.cod = cod
                fMod.save()
                messages.success(request,'Sua resposta foi submetida',extra_tags='text-success')
                return redirect('/exercicios')
            else:
                #FUNÇÃO PARA A ELABORAÇÃO DOS CAMPOS A SEREM INSERIDOS NA PÁGINA
                names = ['Futebol de campo','Futebol de praia','Futsal','Handebol','Basquetebol','Patins ou skate','Atletismo','Natação','Ginástica Olímpica','Artes marciais','Dança','Correr','Andar de bicicleta','Caminhar por exercicio','Caminhar como transporte','Volei de quadra','Volei de praia','Queimado ou pular','Surfe ou bodyboard','Musculacao','Exercicios de força','Tenis de campo','Passeio com cão','Ginastica aeróbica','Outras atividades']
                dias = []
                minutos = []
                
                h=0
                for i in form:
                    if h%2==0:
                        dias.append(i)
                        h=h+1
                    else:
                        minutos.append(i)
                        h=h+1
                ultimo = []
                ultimo.append(dias.pop())

                form = []
                for i in range(len(names)):
                    dic = {}
                    dic['nome']=names[i]
                    dic['dia']=dias[i]
                    dic['minutos']=minutos[i]
                    form.append(dic)
                print(form[0]['dia'])
                #FIM DA FUNÇÃO
                messages.warning(request,'Você preencheu algum campo incorretamente',extra_tags='text-danger')

        except:
            messages.warning(request,'Aconteceu algo de errado com o envio da sua resposta',extra_tags='text-danger')
            return redirect('/exercicios')
    
    return render(request, 'exercicios.html', {'form': form,'ultimo':ultimo})

def Exercicios0(request):
    if request.method == 'POST':
        #Pegando os valores do form e copiando-os para uma variável 'data'
        data = request.POST.copy()
        #separando de forma estúpida cada campo recebido
        cod = data.get('codigo')
        #criando um objeto stroop (vindo das models) que armazenará os valores acima e será salvo no banco
        try:
            if (int(cod)) and (int(cod)>=0) and (int(cod)<=9999):
                try:
                    exercicios_model.objects.get(cod=cod)
                    messages.warning(request, 'Você já fez o teste',extra_tags='text-warning')
                    print(f'{cod} tentou refazer o teste das Atividades físicas')
                except:
                    url = '/exercicios/'+ cod
                    return redirect(url)
            else:
                messages.warning(request, 'Digite um código válido',extra_tags='text-danger')
        except:
            messages.warning(request, 'Digite um código válido')

    return render(request, 'exercicios0.html')
