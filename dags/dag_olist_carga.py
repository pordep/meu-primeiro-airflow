from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator as MySqlOperator

def executar_carga_mysql():
    mysql_hook = MySqlHook(mysql_conn_id='mysql_default')#hook pega todas as credenciais salvas
    connection_uri = mysql_hook.get_uri().replace('mysql://', 'mysql+pymysql://') #força uso do driver
    engine = create_engine(connection_uri)
    
    print("🚀 Lendo arquivo CSV...")
    try:
        df = pd.read_csv('/opt/airflow/data/vendas_limpas.csv')

        print("📤 Enviando para o MySQL (Tabela: bronze_vendas)...")
        df.to_sql('bronze_vendas', con=engine, if_exists='replace', index=False)

        print("✅ Camada Bronze Carregada com sucesso!")
    except Exception as e:
        print(f"❌ ERRO CRÍTICO: {str(e)}")
        raise

with DAG(
    dag_id='dag_carga_olist_mysql',
    start_date=datetime(2024, 1, 1),
    schedule=None, #dispara manualmente no play
    catchup=False
) as dag:

    tarefa_carga = PythonOperator(
        task_id='carga_vendas_bronze',
        python_callable=executar_carga_mysql
    )

    tarefa_silver = MySqlOperator(
        task_id = 'criar_silver_vendas',
        conn_id = 'mysql_default',
        sql = '''
        DROP TABLE IF EXISTS silver_vendas;
        CREATE TABLE silver_vendas AS
        SELECT
            order_id,
            product_id,
            STR_TO_DATE(shipping_limit_date, '%Y-%m-%d %H:%i:%s') AS data_compra,
            CAST(price AS DECIMAL(10, 2)) AS valor_item,
            freight_value AS valor_frete
        FROM bronze_vendas;
        ''',
    )
    
    tarefa_gold = MySqlOperator(
        task_id = 'criar_gold_faturamento',
        conn_id = 'mysql_default',
        sql = '''
        DROP TABLE IF EXISTS gold_faturamento_diario;
        CREATE TABLE gold_faturamento_diario AS
        SELECT
            DATE(data_compra) AS dia,
            COUNT(DISTINCT order_id) AS total_pedidos,
            SUM(valor_item) AS receita_total
        FROM silver_vendas
        GROUP BY dia;
        ''',
    )

    tarefa_carga >> tarefa_silver >> tarefa_gold
