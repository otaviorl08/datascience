#Projeto: Caulculadora de IVA
#Autor: Otavio Rocha
#Linguagem: Python
#Plataforma: VS Code

#O que é IVA?
#O Imposto sobre o Valor Acrescentado (IVA) é um imposto indireto aplicado sobre o valor acrescentado em cada etapa da cadeia de produção e distribuição de bens e serviços. Ele é geralmente repassado ao consumidor final. O IVA é um mecanismo de arrecadação de impostos adotado por muitos países para evitar a tributação cumulativa. Cada empresa ou indivíduo que vende um produto ou serviço é responsável por coletar o IVA sobre o valor que adicionou. O valor total do imposto é calculado subtraindo o IVA pago nas etapas anteriores do valor do IVA coletado. Isso resulta em uma carga fiscal final sobre o consumidor. A alíquota do IVA pode variar conforme o país e o tipo de produto ou serviço. É uma fonte significativa de receita para os governos e uma maneira eficaz de tributar o consumo.

# Como adicionar o IVA?
# IVA = (IVA * Valor líquido) / 100
# Valor Bruto = IVA + Valor Líquido
# Imposto = Valor Bruto - Valor Líquido

# Como retirar o IVA?
# Valor líquido = Valor Bruto / (1+(IVA/100))
# Imposto = Valor bruto - Valor líquido

#Adicionando IVA

#Criando função
def adicionar_iva():
    #imputando valores: taxa IVA em % e Valor Líquido de um produto
    iva_imposto = float(input('Insira o IVA: '))
    valor_liquido = float(input('Insira o valor líquido do produto: '))
    #Calculando valor de IVA sobre o produto e o valor bruto final
    iva = ((iva_imposto * valor_liquido)/100)
    valor_bruto = (iva + valor_liquido)

    #Exibindo resultados
    print('Seu imposto IVA: R$ {:,.2f}'.format(iva))
    print('Valor Líquido: R$ {:,.2f}'.format(valor_liquido))
    print('Valor Bruto: R$ {:,.2f}'.format(valor_bruto))

#Removendo IVA

#Criando função
def remover_iva():
    #imputando valores: Valor Bruto de um produto e taxa IVA em %
    valor_bruto = float(input('Insira o valor bruto do produto: '))
    iva_imposto = float(input('Insira o IVA: '))
    #Calculando Valor líquido do produto e valor sem IVA
    valor_liquido = (valor_bruto / (1 + (iva_imposto / 100)))
    iva = (valor_bruto - valor_liquido)

    #Exibindo resultados
    print('Seu imposto IVA: R$ {:,.2f}'.format(iva))
    print('Valor Líquido: R$ {:,.2f}'.format(valor_liquido))
    print('Valor Bruto: R$ {:,.2f}'.format(valor_bruto))

#Criando Menu

while True:
    print('\n ===== Opções ====')
    print('1. Adicionar IVA')
    print('2. Remover IVA')
    print('3. Sair')

    escolha = int(input('\n Escolha uma opção de operação: '))

    if escolha == 1:
        print('\n === Adicionar IVA ao Produto ===')
    
        adicionar_iva()

    elif escolha == 2:
        print('\n === Remover IVA ao Produto ===')
        
        remover_iva()
    elif escolha == 3:
        break

    else:
        print('Escolha invalida')
