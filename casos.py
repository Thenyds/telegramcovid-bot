import requests
import json
import os



base_url = 'https://brasil.io/api/dataset/covid19'


def get_totais(sigla):
    endpoint = '/caso/data/?is_last=True'
    siglaInformada = sigla.upper()
    if siglaInformada == 'BR' or siglaInformada == '':
        parameters = '&place_type=state'
    else:
        parameters = '&place_type=state&state=' + siglaInformada

    final_url = base_url + endpoint + parameters

    req = requests.get(final_url)
    response = json.loads(req.text)

    return response['results']

def get_novos(sigla):
    endpoint = '/caso_full/data/?is_last=True&is_repeated=False'
    siglaInformada = sigla.upper()
    if siglaInformada == 'BR' or siglaInformada == '':
        parameters = '&place_type=state'
    else:
        parameters = '&place_type=state&state=' + siglaInformada

    final_url = base_url + endpoint + parameters

    req = requests.get(final_url)
    response = json.loads(req.text)

    return response['results']
