from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def ler_linhas():
    import pandas as pd
    print("--- INICIANDO LEITURA DO ARQUIVO ---")
    
    caminho = '/opt/airflow/data/vendas_limpas.csv'
    
    try:
        df = pd.read_csv(caminho)
        print(f'Sucesso! Eu li {len(df)} linhas!')
    except Exception as e:
        print(f'ERRO AO LER ARQUIVO: {e}')
        raise # aviso tarefa falhou

with DAG(
    dag_id='meu_dag_pratico',
    start_date=datetime(2024, 1, 1),
    schedule='40 21 * * *',
    catchup=False
) as dag:

    tarefa_contar = PythonOperator(
        task_id='contar_vendas_olist',
        python_callable=ler_linhas
    )
