from django.shortcuts import render, redirect
from datetime import datetime
from .models import Transacao
from .forms import TransacaoForm

def home(request):
  data = {}
  data['serverTime'] = datetime.now()
  data['transacoes'] = Transacao.objects.all()
  return render(request, 'contas/home.html', data)

def inserir_transacao(request):
  form = TransacaoForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('url_home')

  data = {}
  data['form'] = form
  return render(request, 'contas/form.html', data)

def update(request, pk):
  transacao = Transacao.objects.get(pk=pk)
  form = TransacaoForm(request.POST or None, instance=transacao)
  if form.is_valid():
    form.save()
    return redirect('url_home')

  data = {}
  data['form'] = form
  return render(request, 'contas/form.html', data)

def delete(request, pk):
  
  if Transacao.objects.filter(pk=pk).exists():
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
  return redirect('url_home')