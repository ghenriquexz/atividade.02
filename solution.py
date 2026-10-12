import requests
from datetime import datetime, timedelta

def cotar():
    cotacoes = []
    hoje = datetime.today()

    for i in range(365):
        dia = hoje - timedelta(days=i)
        data = dia.strftime("%m-%d-%Y")
        print("Consultando:", data)

        url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"

        res = requests.get(url, timeout=15)
        res = res.json() 

        if res["value"]:
            cotacoes.append(res["value"][0]["cotacaoCompra"])
        else:
            cotacoes.append(None)

    return cotacoes
print(cotar())
