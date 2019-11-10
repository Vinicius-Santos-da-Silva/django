from django.db import models


class FinanceManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )


class Finance(models.Model):

    name = models.CharField('Nome', max_length=100)
    loja = models.SlugField('Loja')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )

    end_date = models.DateField(
        'Data Final', null=True, blank=True
    )
    
    # image = models.ImageField(
    #     upload_to='courses/images', verbose_name='Imagem',
    #     null=True, blank=True
    # )

    valor = models.IntegerField(blank=True, null=True)

    numero_parcelas = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FinanceManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'
        ordering = ['created_at']







class Receita(models.Model):

    name = models.CharField('Nome', max_length=100)
    origem = models.SlugField('Origem')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )

    end_date = models.DateField(
        'Data Final', null=True, blank=True
    )
    
    # image = models.ImageField(
    #     upload_to='courses/images', verbose_name='Imagem',
    #     null=True, blank=True
    # )

    valor = models.IntegerField(blank=True, null=True)

    numero_parcelas = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FinanceManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'receitas'
        ordering = ['created_at']






class Empresa(models.Model):

    name = models.CharField('Nome', max_length=100)
    
    email = models.CharField('Email', max_length=100)
    
    endereco = models.CharField('Enderco', max_length=100)

    cnpj = models.CharField('CNPJ', max_length=100)
    
    origem = models.SlugField('Origem')

    description = models.TextField('Descrição', blank=True)
    
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )

    end_date = models.DateField(
        'Data Final', null=True, blank=True
    )
    
    logo = models.ImageField(
        upload_to='administrador/financeiro/logo_tipo', verbose_name='Logotipo',
        null=True, blank=True
    )

    created_at = models.DateTimeField(
        'Criado em', auto_now_add=True
    )
    
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = FinanceManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'empresas'
        ordering = ['created_at']