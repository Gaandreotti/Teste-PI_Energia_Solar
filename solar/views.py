from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Cliente, Orcamento
from .forms import ClienteForm

def calculadora(request):
    return render(request, 'solar/index.html')

@csrf_exempt
def calcular(request):
    if request.method != 'POST':
        return JsonResponse({'erro': 'Método não permitido'}, status=405)

    dados = json.loads(request.body)
    consumo    = float(dados.get('consumo', 0))
    conta      = float(dados.get('conta', 0))
    tarifa     = float(dados.get('tarifa', 0.85))
    irradiacao = float(dados.get('irradiacao', 5.0))
    geracao    = float(dados.get('geracao', 100)) / 100
    reajuste   = float(dados.get('reajuste', 8)) / 100

    consumo_alvo    = consumo * geracao
    potencia        = consumo_alvo / (irradiacao * 30 * 0.82)
    custo           = potencia * 1000 * 4.5
    economia_mensal = consumo_alvo * tarifa
    economia_anual  = economia_mensal * 12

    acumulado = 0
    payback   = 0
    eco_ano   = economia_anual
    for ano in range(1, 31):
        acumulado += eco_ano
        if acumulado >= custo and payback == 0:
            payback = ano
        eco_ano *= (1 + reajuste)
    if payback == 0:
        payback = 30

    request.session['ultimo_calculo'] = {
        'consumo_kwh':     consumo,
        'conta_valor':     conta,
        'potencia_kwp':    round(potencia, 2),
        'custo_estimado':  round(custo, 2),
        'economia_mensal': round(economia_mensal, 2),
        'payback_anos':    payback,
    }

    return JsonResponse({
        'potencia':        round(potencia, 2),
        'custo':           round(custo, 2),
        'economia_mensal': round(economia_mensal, 2),
        'payback':         payback,
        'compensa':        payback <= 10,
    })

def cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            calculo = request.session.get('ultimo_calculo')
            if calculo:
                Orcamento.objects.create(cliente=cliente, **calculo)
            return redirect('sucesso')
    else:
        form = ClienteForm()
    return render(request, 'solar/cadastro.html', {'form': form})

def sucesso(request):
    return render(request, 'solar/sucesso.html')