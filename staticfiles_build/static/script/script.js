//Teclado como controle
function teclado(event) {
    switch (event.keyCode) {
        case 49: //tecla 1
            document.getElementById('0').click()
            break;
        case 50: //tecla 2
            document.getElementById('1').click()
            break;
        case 51: //tecla 3
            document.getElementById('2').click()
            break;
        case 52: //tecla 4
            document.getElementById('3').click()
            break;
        default: //qualquer outra tecla
            break;
    }
}
function bottomFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 9999999999999;
  }
//TOAST 8=======D
function toast(b) {
    $('#notificacoes').append(`
    <div class="toast m-0" role="alert" aria-live="assertive" aria-atomic="true" data-delay="4500">
    <div class="toast-header">
      <strong class="mr-auto col-md-5">Stroop</strong>
      <small class="text-muted col-md-6 text-right">recentemente</small>
      <button type="button" class="close" data-dismiss="toast" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>
    <div class="toast-body text-dark">
      Etapa ` + b + ` concluída
    </div>
  </div>
    `);
    $('.toast').toast('show')
    $('.toast').on('hidden.bs.toast', e => {
        $(e.currentTarget).remove();
    })
}
//Eu fiz o cronometro mas é tão confuso que nem eu lembro mais como que faz
var cronometro

function timer() {
    console.log(armazemTempo.a)
    armazemTempo.a += 30;
}

function stop() {
    clearInterval(cronometro)
}

//marca a etapa
var etapa = 1;
//responsavel por fazer o processo de varredura pelas questoes durante o teste
var numeroQuestao = 1;
//armazena as respostas corretas antes do teste
var gabarito = [];
//armazena as pontuações do usuário de cada etapa
var pontuacoes = {
    primeira: 0,
    segunda: 0,
    terceira: 0,
}
//armazena os tempos de resposta do usuário para cada questão
var armazemTempo = {
    tempos1: [],
    tempos2: [],
    tempos3: [],
    a: 0,
}

//habilita os botões no começo do teste
function desabilitarRespostas(b) {
    for (let i = 0; i < 4; i++) {
        document.getElementById(i).disabled = b
    }
}
//desabilita/habilita o botão de ir para a proxima etapa
function desabilitarProxima(b) {
        document.getElementById('proxima').disabled = b
}
//As funções abaixo são as executadas dentro das funcões executadas ao responder a questão
function respostaCerta(id) {
    if (id == 1) {
        armazemTempo.tempos1[numeroQuestao - 1] = armazemTempo.a;
        armazemTempo.a = 0;
        pontuacoes.primeira++;
        numeroQuestao++;
    }
    if (id == 2) {
        armazemTempo.tempos2[numeroQuestao - 1] = armazemTempo.a;
        armazemTempo.a = 0;
        pontuacoes.segunda++;
        numeroQuestao++;
    }
    if (id == 3) {
        armazemTempo.tempos3[numeroQuestao - 1] = armazemTempo.a;
        armazemTempo.a = 0;
        pontuacoes.terceira++;
        numeroQuestao++;
    }
}

function respostaErrada(id) {
    if (id == 1) {
        armazemTempo.tempos1[numeroQuestao - 1] = armazemTempo.a;
        armazemTempo.a = 0;
        numeroQuestao++;
    }
    if (id == 2) {
        armazemTempo.tempos2[numeroQuestao - 1] = armazemTempo.a;
        armazemTempo.a = 0;
        numeroQuestao++;
    }
    if (id == 3) {
        armazemTempo.tempos3[numeroQuestao - 1] = armazemTempo.a;
        armazemTempo.a = 0;
        numeroQuestao++;
    }
}
//Função da resposta sobre a qual mencionei à 2 comentários atras
function clicar(id) {
    document.getElementById('td' + numeroQuestao).classList.remove("border-dark")
    document.getElementById('td' + numeroQuestao).classList.add("border-light")
    if (etapa == 1) {
        if (document.getElementById('dot' + numeroQuestao).style.background == document.getElementById(id).value) {
            respostaCerta(etapa);
        } else {
            respostaErrada(etapa);
        }
    } else {
        if (document.getElementById('td' + numeroQuestao).style.color == document.getElementById(id).value) {
            respostaCerta(etapa);
        } else {
            respostaErrada(etapa);
        }
    }
    if (numeroQuestao <= 24) {
        document.getElementById('td' + numeroQuestao).classList.remove("border-light")
        document.getElementById('td' + numeroQuestao).classList.add("border-dark")
    }
    if (numeroQuestao > 24) {
        stop()
        if (etapa < 4) {
            //alert("Etapa " + etapa + " concluida")
            //TOAST 8=======D
            toast(etapa)
            //TOAST 8=======D
            desabilitarRespostas(true)
            desabilitarProxima(false)
            if (etapa < 3) {
                //document.getElementById('divProxima').classList.add("show")
                $('#divProxima').collapse('toggle')
            }
            numeroQuestao = 1;
            if (etapa == 3) {
                //document.getElementById('teste').classList.add("d-none")
                //document.getElementById('divMostrarR').classList.add("show")
                $('#divMostrarR').collapse('toggle')
            }
        }
    }

}
//Elabora o ambiente da primeira etapa na tabela
function gerarCores() {
    var cor = ["green", "yellow", "red", "blue"]
    for (var i = 1; i <= 24; i++) {
        var corIndice = parseInt(Math.random() * 3.9999)
        gabarito[i - 1] = cor[corIndice]
        document.getElementById('dot' + i).style.background = cor[corIndice]
    }
}
//Elabora o ambiente da segunda etapa na tabela
function gerarCores2() {
    var cor = ["green", "yellow", "red", "blue"]
    var palavra = ["tudo", "nunca", "cada", "hoje"]
    for (var i = 1; i <= 24; i++) {
        var corIndice = parseInt(Math.random() * 3.9999)
        var palavraIndice = parseInt(Math.random() * 3.9999)
        gabarito[i - 1] = cor[corIndice]
        var elem = document.getElementById('dot' + i)
        elem.parentNode.removeChild(elem)
        document.getElementById('td' + i).style.color = cor[corIndice]
        document.getElementById('td' + i).innerHTML = palavra[palavraIndice]
        document.getElementById('td' + i).style.background = "#bbb"
    }
}
//Elabora o ambiente da terceira etapa na tabela
function gerarCores3() {
    var cor = ["green", "yellow", "red", "blue"]
    var palavras = ["Verde", "Amarelo", "Vermelho", "Azul"]
    for (var i = 1; i <= 24; i++) {
        var corIndice = parseInt(Math.random() * 3.9999)
        var palavra = parseInt(Math.random() * 3.9999)
        while (corIndice == palavra) {
            var palavra = parseInt(Math.random() * 3.9999)
        }
        gabarito[i - 1] = cor[corIndice]
        document.getElementById('td' + i).innerHTML = palavras[palavra]
        document.getElementById('td' + i).style.color = cor[corIndice]
        document.getElementById('td' + i).style.background = "#bbb"

    }
}
//processa e exibe os resultados ao usuário
function gerarResultados(a, b) {
    var temp1Total = 0,
        temp2Total = 0,
        temp3Total = 0,
        temp1Media, temp2Media, temp3Media
    for (let i = 0; i < b.tempos1.length; i++) {
        temp1Total += b.tempos1[i];
        temp2Total += b.tempos2[i];
        temp3Total += b.tempos3[i];
    }
    temp1Media = temp1Total / b.tempos1.length
    temp2Media = temp2Total / b.tempos2.length
    temp3Media = temp3Total / b.tempos3.length
    //Muda o HTML
    //card1
    /*document.getElementById('pont1').innerHTML = "Acertos: " + a.primeira
    document.getElementById('media1').innerHTML = "Tempo Médio de resposta: " + (temp1Media / 1000) + 's'
    document.getElementById('tempo1').innerHTML = "Tempo total da etapa: " + (temp1Total / 1000) + 's'
    //card2
    document.getElementById('pont2').innerHTML = "Acertos: " + a.segunda
    document.getElementById('media2').innerHTML = "Tempo Médio de resposta: " + temp2Media / 1000 + 's'
    document.getElementById('tempo2').innerHTML = "Tempo total da etapa: " + (temp2Total / 1000) + 's'
    //card3
    document.getElementById('pont3').innerHTML = "Acertos: " + a.terceira
    document.getElementById('media3').innerHTML = "Tempo Médio de resposta: " + (temp3Media / 1000) + 's'
    document.getElementById('tempo3').innerHTML = "Tempo total da etapa: " + (temp3Total / 1000) + 's'
*/
    document.getElementById('acertos1').innerHTML = a.primeira
    document.getElementById('acertos1').value = a.primeira
    
    document.getElementById('tempo1').innerHTML = temp1Total/1000+'s'
    document.getElementById('tempo1').value = temp1Total/1000

    document.getElementById('acertos2').innerHTML = a.segunda
    document.getElementById('acertos2').value = a.segunda

    document.getElementById('tempo2').innerHTML = temp2Total/1000+'s'
    document.getElementById('tempo2').value = temp2Total/1000

    document.getElementById('acertos3').innerHTML = a.terceira 
    document.getElementById('acertos3').value = a.terceira 

    document.getElementById('tempo3').innerHTML = temp3Total/1000+'s'
    document.getElementById('tempo3').value = temp3Total/1000

}
//Botão de confirmação para prosseguir para a proxima etapa (exibido ao fim de cada etapa)
function proxEtapa() {
    desabilitarRespostas(false)
    etapa++;
    if (etapa < 4) {
        console.log("essa é a etapa "+ etapa)
        document.getElementById('td' + numeroQuestao).classList.add("border-dark")
        cronometro = setInterval(timer, 30)
        
    }
    if (etapa == 2) {
        console.log("essa é a etapa "+ etapa)
        gerarCores2();
        
    } else if (etapa == 3) {
        console.log("essa é a etapa "+ etapa)
        gerarCores3();
        
    } else {
        console.log("essa é a etapa "+ etapa)
        desabilitarRespostas(true)
        gerarResultados(pontuacoes, armazemTempo);
        
    }
}

function Resultado(){

}

function iniciar() {
    desabilitarRespostas(false)
    //seleciona a questao inicial
    document.getElementById('td' + numeroQuestao).classList.add("border-dark")
    //Aparentemente isso bota o cronometro pra funcionar (roda a cada 30ms)
    cronometro = setInterval(timer, 30)
    //Começa a etapa 1
    gerarCores()
}