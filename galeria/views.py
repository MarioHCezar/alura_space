from django.shortcuts import render


# render permite envio de dados
def index(request):
    dados = {
        1: {'nome': 'Nebulosa de Carina', 
            'legenda': 'webtelescope.org / NASA / James Webb'},
        2: {'nome': 'Galaxia NGC 1079', 
            'legenda': 'nasa.org / NASA / Hubble'}
    }

    return render(request, 'index.html', {'cards': dados})


def imagem(request):
    return render(request, 'imagem.html')