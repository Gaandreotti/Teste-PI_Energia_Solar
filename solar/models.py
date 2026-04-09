from django.db import models

class Cliente(models.Model):
    nome      = models.CharField(max_length=100, verbose_name="Nome completo")
    email     = models.EmailField(verbose_name="E-mail")
    telefone  = models.CharField(max_length=20, verbose_name="Telefone")
    cidade    = models.CharField(max_length=100, verbose_name="Cidade")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Data")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def _str_(self):
        return f"{self.nome} — {self.email}"


class Orcamento(models.Model):
    cliente         = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    consumo_kwh     = models.FloatField(verbose_name="Consumo (kWh)")
    conta_valor     = models.FloatField(verbose_name="Conta (R$)")
    potencia_kwp    = models.FloatField(verbose_name="Potência (kWp)")
    custo_estimado  = models.FloatField(verbose_name="Custo (R$)")
    economia_mensal = models.FloatField(verbose_name="Economia mensal (R$)")
    payback_anos    = models.FloatField(verbose_name="Payback (anos)")
    criado_em       = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"

    def _str_(self):
        return f"Orçamento de {self.cliente.nome}"