import numpy as np
from recommendations.loadUserProfileCluster import PredictCluster
from datetime import date

#array 

#calcular idade

def ProcessData(userProfile):

    #calcular idade
    idade = CalculateAge(userProfile["data_nascimento"])
    #pegar valor booleano de acompanhamento
    acompanhamento = GetAsBool(userProfile["acompanhamento"])
    #pegar os tiposLocais
    tiposLocais = list(userProfile["preferencia_locais"])
    #pegar as preferenciasDam
    preferenciasDam = list(userProfile["preferencia_dam"])
    #pegar as os tiposRecursos
    tiposRecursos = list(userProfile["preferencia_recursos"])

    userPreferencesTable = {
        'idade': idade,
        'acompanhamento': acompanhamento,
        'progressiva/degenerativa': GetUserPreferences('progressiva/degenerativa', userProfile["duracao_condicao"]),
        'temporaria': GetUserPreferences('temporaria', userProfile["duracao_condicao"]),
        'estavel ou permanente': GetUserPreferences('estavel ou permanente', userProfile["duracao_condicao"]),
        'pmlr': GetUserPreferences('pmlr', userProfile["tipo_usuario"]),
        'acompanhante': GetUserPreferences('acompanhante', userProfile["tipo_usuario"]),
        "elevador":  GetPreferences("elevador", tiposRecursos),  
        "plataforma elevatória": GetPreferences("plataforma elevatória", tiposRecursos),  
        "ponto de taxi":  GetPreferences("ponto de taxi", tiposRecursos),  
        "sinalização": GetPreferences("sinalização", tiposRecursos),  
        "rampas":  GetPreferences("rampas", tiposRecursos),  
        "corrimões": GetPreferences("corrimões", tiposRecursos),  
        "portas amplas": GetPreferences("portas amplas", tiposRecursos),  
        "calçada acessível":GetPreferences("calçada acessível", tiposRecursos),  
        "vagas preferenciais": GetPreferences("vagas preferenciais", tiposRecursos),  
        "banheiro família":GetPreferences("banheiro família", tiposRecursos),  
        "barras de apoio":GetPreferences("barras de apoio", tiposRecursos),  
        "ponto de ônibus":GetPreferences("ponto de ônibus", tiposRecursos),  
        "funcionários treinados": GetPreferences("funcionários treinados", tiposRecursos),  
        "filas preferenciais":GetPreferences("filas preferenciais", tiposRecursos),  
        "banheiro adaptado":  GetPreferences("banheiro adaptado", tiposRecursos),  
        "piso nivelado":  GetPreferences("piso nivelado", tiposRecursos),  
        "área de transferência": GetPreferences("área de transferência", tiposRecursos),  
        "barra sanitária":  GetPreferences("barra sanitária", tiposRecursos),  
        "piso antiderrapante": GetPreferences("piso não trepidante", tiposRecursos),  
        "guia rebaixada": GetPreferences("guia rebaixada", tiposRecursos),  
        "piso não trepidante": GetPreferences("piso não trepidante", tiposRecursos),      
        "bengala": GetPreferences("bengala", preferenciasDam),
        "muleta":  GetPreferences("muleta", preferenciasDam),
        "andador": GetPreferences("andador", preferenciasDam),
        "cadeira de rodas motorizada": GetPreferences("cadeira de rodas motorizada", preferenciasDam),
        "cadeiras de rodas manual": GetPreferences("cadeiras de rodas manual", preferenciasDam),
        "cadeira de rodas monobloco": GetPreferences("cadeira de rodas monobloco", preferenciasDam),
        "cadeira de rodas dobravel em x":  GetPreferences("cadeira de rodas dobravel em x", preferenciasDam),
        "cadeira de rodas com elevação automatica":  GetPreferences("cadeira de rodas com elevação automatica", preferenciasDam),
        "protese":  GetPreferences("protese", preferenciasDam),
        "ortese":  GetPreferences("ortese", preferenciasDam),   
        "igreja": GetPreferences("igreja", tiposLocais),
        "museu": GetPreferences("museu", tiposLocais),
        "estátua": GetPreferences("estátua", tiposLocais),
        "parque": GetPreferences("parque", tiposLocais),
        "praia": GetPreferences("praia", tiposLocais),
        "teatro":  GetPreferences("teatro", tiposLocais),
        "biblioteca": GetPreferences("biblioteca", tiposLocais),
        "monumento":GetPreferences("monumento", tiposLocais),
        "galeria":  GetPreferences("galeria", tiposLocais),
        "mercado": GetPreferences("mercado", tiposLocais),
        "jardim botânico": GetPreferences("jardim botânico", tiposLocais),
        "zoológico": GetPreferences("zoológico", tiposLocais),
        "catedral": GetPreferences("catedral", tiposLocais),
        "sinagoga": GetPreferences("sinagoga", tiposLocais),
        "mesquita":  GetPreferences("mesquita", tiposLocais),
        "castelo": GetPreferences("castelo", tiposLocais),
        "palácio": GetPreferences("palácio", tiposLocais),
        "torre": GetPreferences("torre", tiposLocais),
        "observatório": GetPreferences("observatório", tiposLocais),
        "planetário":  GetPreferences("planetário", tiposLocais),
        "aquário":  GetPreferences("aquário", tiposLocais),
        "farol":  GetPreferences("farol", tiposLocais),
        "ilha":  GetPreferences("ilha", tiposLocais),
        "praça":  GetPreferences("praça", tiposLocais),
    }
    #print(f"Default Table: ", userPreferencesTable)
    #print(ConvertToArray(userPreferencesTable))
    return PredictCluster(GetValues(userPreferencesTable))

def CalculateAge(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def GetAsBool(value):
    match value:
        case "nao":
            return 0
        case "sim":
            return 1
        case _:
            return 0
def GetUserPreferences(key, value):
    if(value == key):
        return 1
    else:
        return 0

def GetPreferences(value, prefList):
    for element in prefList:
        print(f"ELEMENT==", str(element))
        if(value == str(element)):
            return 1
    return 0

def GetValues(dictionary):
    valueList = [1]
    valueList[0] = list(dictionary.values())
    return valueList
