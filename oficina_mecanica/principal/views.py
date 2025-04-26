from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Produto, OrdemDeServico, Agendamento
from django.utils import timezone

def lista_clientes(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'principal/lista_clientes.html', context)

def cadastro_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        cep = request.POST.get('cep')
        endereco = request.POST.get('endereco')
        numero_endereco = request.POST.get('numero_endereco')
        bairro = request.POST.get('bairro')
        complemento = request.POST.get('complemento')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        observacao = request.POST.get('observacao')

        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, cep=cep, endereco=endereco,
                          numero_endereco=numero_endereco, bairro=bairro, complemento=complemento,
                          cidade=cidade, estado=estado, observacao=observacao)
        cliente.save()
        return redirect('lista_clientes')
    else:
        return render(request, 'principal/cadastro_cliente.html')

def lista_produtos(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'principal/lista_produtos.html', context)

def cadastro_produto(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        codigo_barras = request.POST.get('codigo_barras')
        marca = request.POST.get('marca')
        unidade = request.POST.get('unidade')
        observacao = request.POST.get('observacao')

        produto = Produto(categoria=categoria, nome=nome, preco=preco, codigo_barras=codigo_barras,
                          marca=marca, unidade=unidade, observacao=observacao)
        produto.save()
        return redirect('lista_produtos')
    else:
        return render(request, 'principal/cadastro_produto.html')

def lista_ordens_servico(request):
    ordens_servico = OrdemDeServico.objects.all()
    context = {'ordens_servico': ordens_servico}
    return render(request, 'principal/lista_ordens_servico.html', context)

def gerar_ordem_servico(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        descricao_problema = request.POST.get('descricao_problema')
        servicos_realizados = request.POST.get('servicos_realizados')
        produtos_utilizados_ids = request.POST.getlist('produtos_utilizados')
        valor_total = request.POST.get('valor_total')
        status = request.POST.get('status')

        cliente = Cliente.objects.get(id=cliente_id)
        ordem_servico = OrdemDeServico(cliente=cliente, descricao_problema=descricao_problema,
                                      servicos_realizados=servicos_realizados, valor_total=valor_total,
                                      status=status)
        ordem_servico.save()
        ordem_servico.produtos_utilizados.set(produtos_utilizados_ids)
        return redirect('lista_ordens_servico')
    else:
        clientes = Cliente.objects.all()
        produtos_disponiveis = Produto.objects.all()
        context = {'clientes': clientes, 'produtos_disponiveis': produtos_disponiveis}
        return render(request, 'principal/gerar_ordem_servico.html', context)

def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    context = {'agendamentos': agendamentos}
    return render(request, 'principal/lista_agendamentos.html', context)

def novo_agendamento(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        data_agendada_str = request.POST.get('data_agendada')
        descricao = request.POST.get('descricao')

        cliente = Cliente.objects.get(id=cliente_id)
        data_agendada = timezone.datetime.strptime(data_agendada_str, '%Y-%m-%dT%H:%M')

        agendamento = Agendamento(cliente=cliente, data_agendada=data_agendada, descricao=descricao)
        agendamento.save()
        return redirect('lista_agendamentos')
    else:
        clientes = Cliente.objects.all()
        context = {'clientes': clientes}
        return render(request, 'principal/novo_agendamento.html', context)