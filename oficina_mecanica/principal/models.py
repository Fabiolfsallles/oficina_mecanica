from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    numero_endereco = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.CharField(max_length=100, blank=True, null=True)
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_barras = models.CharField(max_length=255, unique=True, blank=True, null=True)
    marca = models.CharField(max_length=100, blank=True, null=True)
    unidade = models.CharField(max_length=50, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class OrdemDeServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(blank=True, null=True)
    descricao_problema = models.TextField()
    servicos_realizados = models.TextField(blank=True, null=True)
    produtos_utilizados = models.ManyToManyField(Produto, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=50, default='Em Aberto')

    def __str__(self):
        return f"OS #{self.id} - {self.cliente.nome}"

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_agendada = models.DateTimeField()
    descricao = models.TextField()
    alerta_enviado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cliente.nome} - {self.data_agendada}"