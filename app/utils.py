import re

def validar_nome(lista, nome):
    if nome is None:
        lista.append('O nome é obrigatório')

    if not isinstance(nome, str) or len(nome.strip()) < 3:
        lista.append('O nome deve ter pelo menos 3 caracteres')
    
    if re.search(r'\d', nome):
        lista.append('O nome não deve conter números')
    
    return lista



def validar_sobrenome(lista, sobrenome):
    if sobrenome is None:
        lista.append('O sobrenome é obrigatório')

    if not isinstance(sobrenome, str) or len(sobrenome.strip()) < 3:
        lista.append('O sobrenome deve ter pelo menos 3 caracteres')

    if re.search(r'\d', sobrenome):
        lista.append('O sobrenome não deve conter números')
    
    return lista


def validar_idade(lista, idade):
    if idade is None:
        lista.append('A idade é obrigatório')
        return lista
    try:
        i = int(idade)
    except (TypeError, ValueError):
        lista.append('Idade inválida')
        return lista
    if i <= 0:
        lista.append('Idade ser maior que zero')
    if i > 120:
        lista.append('Você não deve ser tão velho(a) assim')
    return lista

def validar_genero(lista, genero):

    if genero is None or not isinstance(genero, str) or genero not in ('Feminino', 'Masculino'):
        lista.append('É necessário selecionar um genero')
    return lista



def validar_refeicoes_dia(lista, quantidade):
    if quantidade is None:
        lista.append('Informe a quantidade de refeições por dia')
    try:
        q = int(quantidade)
    except (TypeError, ValueError):
        lista.append('Quantidade de refeições invalida')
        return lista
    
    if q == 0:
        lista.append('Como assim você não se alimenta ? não minta e coloque o valor correto')
    if q < 0:
        lista.append('Não pode ser um valor negativo')
    
    return lista



def validar_consumo_frutas(lista, consumo):
    if consumo is None or not isinstance(consumo, str) or consumo not in ('sim', 'não'):
        lista.append('Informe se consome fruta ou não')

    return lista



def validar_consumo_agua(lista, consumo):
    if consumo is None:
        lista.append('Informe o consumo de agua em litros')
        return lista
    try:
        c = float(consumo)
    except(TypeError, ValueError):
        lista.append('Consumo de agua invalido')
        return lista
    
    if c == 0:
        lista.append('Não bebe agua ?? OLHAA A PEDRAAAAA')
    if c < 0:
        lista.append('Não pode ser um valor negativo')

    return lista



def validar_horario(lista, horario):
    if horario is None:
        lista.append('Informe o horário do jantar')
        return lista
    if not isinstance(horario, str):
        lista.append('Horário inválido')
        return lista
    
    horario = horario.strip()
    if not re.match(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$', horario):
        lista.append('Formato de horário inválido (use HH:mm)')
        return lista
    
    try:
        hora, minuto = map(int, horario.split(':'))
        if not (0 <= hora <= 23 and 0 <= minuto <= 59):
            lista.append('Horário fora do intervalo válido (00 - 23:59)')
    except (ValueError, TypeError):
        lista.append('Horário inválido')
    
    return lista