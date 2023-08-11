import xmltodict
import os
import pandas as pd

def pegar_infos(nome_arquivo, valores):
    print(f"Pegou as informações {nome_arquivo}")
    with open(f'nfs/{nome_arquivo}',"rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        #print(json.dumps(dic_arquivo, indent=4))
        infos_nf = dic_arquivo["nfeProc"]["NFe"]["infNFe"]

        numero_nota = infos_nf["ide"]["nNF"]
        serie = infos_nf["ide"]["serie"]

        cnpj_emissora = infos_nf["emit"]["CNPJ"]
        nome_emissor = infos_nf["emit"]["xNome"]
        endereco_emissor = infos_nf["emit"]["enderEmit"]["xLgr"]
        endero_nro_emissor = infos_nf["emit"]["enderEmit"]["nro"]
        endereco_cidade_emissor = infos_nf["emit"]["enderEmit"]["xMun"]

        cnpj_destinatario = infos_nf["dest"]["CNPJ"]
        empresa_destinatario = infos_nf["dest"]["xNome"]
        endereco_destinatario_= infos_nf["dest"]["enderDest"]["xLgr"]
        endereco_nro_destinatario = infos_nf["dest"]["enderDest"]["nro"]
        endereco_cidade_destinatario =  infos_nf["dest"]["enderDest"]["xMun"]

        valor = infos_nf["pag"]["detPag"]["vPag"]

        valores.append([numero_nota, serie, cnpj_emissora, nome_emissor, endereco_emissor, endero_nro_emissor, 
               endereco_cidade_emissor, cnpj_destinatario, empresa_destinatario, endereco_nro_destinatario,endereco_cidade_destinatario, valor])

lista_arquivos = os.listdir("nfs")

colunas = ["numero_nota", "serie", "cnpj_emissora", "nome_emissor", "endereco_emissor", "endero_nro_emissor", 
               "endereco_cidade_emissor", "cnpj_destinatario", "empresa_destinatario", "endereco_nro_destinatario","endereco_cidade_destinatario", "valor"]

valores = []

for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)
    
tabela = pd.DataFrame(columns=colunas,data=valores)
tabela.to_excel("NotasFiscais.xlsx", index=False)

