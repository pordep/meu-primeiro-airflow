from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
from airflow.providers.mysql.hooks.mysql import MySqlHook

def executar_carga_mysql():
    #hook pega todas as credenciais salvas
    mysql_hook = MySqlHook(mysql_conn_id='mysql_olist')
    engine = mysql_hook.get_sqlalchemy_engine()
    
    df = pd.read_csv('/opt/airflow/data/vendas_limpas.csv')
    df.to_sql('vendas_ecommerce', con=engine, if_exists='replace', index=False)
    print("✅ Carga finalizada com sucesso via Connection Hook!")

with DAG(
    dag_id='dag_carga_olist_mysql',
    start_date=datetime(2024, 1, 1),
    schedule=None, #dispara manualmente no play
    catchup=False
) as dag:

    tarefa_carga = PythonOperator(
        task_id='carga_vendas',
        python_callable=executar_carga_mysql
    )
