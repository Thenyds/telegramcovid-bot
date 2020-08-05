import casos
from datetime import datetime


def action_handler(action, parameters, return_var):
    return_values = {}
    if action == 'totais':
        return_values = get_totais(parameters, return_var)
    elif action == 'novos':
        return_values = get_novos(parameters, return_var)
    return {
            'skills': {
                'main skill': {
                    'user_defined': return_values
                }
            }
        }

def get_totais(parameters, return_var):
    sigla = parameters['sigla']
    casos_totais_info = casos.get_totais(sigla)

    totais_texto = '\n\n'
    for totais in casos_totais_info:
        if str(totais['city']) != 'None' and str(totais['city']) != '':
            totais_texto += 'Cidade: ' + str(totais['city']) + ',\n'

        dataFormatada = ''
        data = datetime.strptime(totais['date'], '%Y-%m-%d').date()
        dataFormatada = data.strftime('%d/%m/%Y')
        
        totais_texto += 'Estado: ' + str(totais['state']) + ',\n'
        totais_texto += 'Data de atualização: ' + dataFormatada + ',\n'
        totais_texto += 'Casos confirmados: ' + str(totais['confirmed']) + ',\n'
        totais_texto += 'Óbitos: ' + str(totais['deaths']) + '.\n'
        totais_texto += ' ' + '\n'
    totais_texto += '* Fonte: Secretarias de Saúde das Unidades Federativas, dados tratados por Álvaro Justen e equipe de voluntários Brasil.IO' + '.\n'
    totais_texto += '* Brasil.IO: boletins epidemiológicos da COVID-19 por município por dia, disponível em: https://brasil.io/dataset/covid19/' + '.\n'
    return {
        return_var: totais_texto
    }

def get_novos(parameters, return_var):
    sigla = parameters['sigla']
    casos_novos_info = casos.get_novos(sigla)

    novos_texto = '\n\n'
    for novos in casos_novos_info:
        if str(novos['city']) != 'None' and str(novos['city']) != '':
            novos_texto += 'Cidade: ' + str(novos['city']) + ',\n'

        dataFormatada = ''
        data = datetime.strptime(novos['date'], '%Y-%m-%d').date()
        dataFormatada = data.strftime('%d/%m/%Y')

        novos_texto += 'Estado: ' + str(novos['state']) + ',\n'
        novos_texto += 'Data de atualização: ' + dataFormatada + ',\n'
        novos_texto += 'Novos casos confirmados: ' + str(novos['new_confirmed']) + ',\n'
        novos_texto += 'Novos óbitos: ' + str(novos['new_deaths']) + '.\n'
        novos_texto += ' ' + '\n'
    novos_texto += '* Fonte: Secretarias de Saúde das Unidades Federativas, dados tratados por Álvaro Justen e equipe de voluntários Brasil.IO' + '.\n'
    novos_texto += '* Brasil.IO: boletins epidemiológicos da COVID-19 por município por dia, disponível em: https://brasil.io/dataset/covid19/' + '.\n'
    return {
        return_var: novos_texto
    }


