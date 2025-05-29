import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
def coletarArquivos ():
    arquivoExcel = r"C:\Users\pietro.abrahamian\Desktop\excel1.xlsx"
    excel = pd.read_excel(arquivoExcel)

    excel['competencia'] = pd.to_datetime(excel['competencia']).dt.strftime('%d/%m/%Y')  
    excel['data_vencimento'] = pd.to_datetime(excel['data_vencimento']).dt.strftime('%d/%m/%Y')

    for index, row in excel.iterrows():
        empresa = row["empresa"]
        tipoAP = row["tipo_ap"]
        numAP = row["num_ap"]
        fornecedor = row["fornecedor"]
        valorTotal = row["valor_total"]
        competencia = row["competencia"]
        dataVencimento = row["data_vencimento"]
        comentario = row["comentario"]
        nomePdf = row["nome_pdf"]
        print(empresa, tipoAP, numAP, fornecedor, valorTotal, competencia, dataVencimento, comentario, nomePdf)

coletarArquivos()

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)
driver.get("https://workongroup.zeev.it/my/tasks")
time.sleep(40)