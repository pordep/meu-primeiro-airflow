# 🚀 Primeiro Pipeline Orquestrado com Apache Airflow



Este repositório contém o código e a infraestrutura para um pipeline de dados básico, mas funcional, utilizando o ecossistema moderno de Engenharia de Dados.



## 📋 Sobre o Projeto

O objetivo deste projeto foi criar uma DAG (Directed Acyclic Graph) no Airflow para automatizar a leitura e processamento inicial de um dataset de vendas (Olist) com mais de 111.000 registros.



## 🛠️ Tecnologias Utilizadas

* **Python 3.12**: Lógica de processamento.

* **Pandas**: Manipulação e leitura de dados.

* **Apache Airflow 3.0 (ou 2.x)**: Orquestração e agendamento.

* **Docker & Docker Compose**: Isolamento de ambiente e infraestrutura.
  
* **MySQL 8.0**: Banco de dados relacional de destino para persistência dos dados processados.



## 🏗️ Estrutura do Projeto

- `dags/pratica_dag.py`: Definição da DAG e operadores Python.

- `dags/vendas_limpas.csv`: Dataset utilizado (Olist).

- `docker-compose.yaml`: Configuração dos serviços do Airflow (Webserver, Scheduler, Worker, Postgres, Redis).



## 💡 Desafios Superados (Troubleshooting)

Durante o desenvolvimento, foram resolvidos problemas reais de ambiente:

1. **Compatibilidade de Versões**: Ajuste de parâmetros de `schedule_interval` para `schedule` conforme as novas especificações do Airflow.

2. **Docker Networking**: Resolução de erros de comunicação entre o Worker e o Log Server.

3. **Gerenciamento de Recursos**: Otimização dos containers para rodar em ambiente WSL2.

4. **Segurança de Credenciais**: Substituição de strings de conexão expostas por Airflow Hooks (MySqlHook), centralizando a gestão de segredos na interface administrativa do Airflow.

5. **Persistência de Dados**: Configuração de volumes no Docker Compose para garantir a integridade dos logs e DAGs.



## ⏱️ Agendamento

O pipeline foi configurado para execução automática utilizando expressões **Cron**, garantindo que o processamento ocorra diariamente sem intervenção humana.



<img width="1452" height="373" alt="Captura de tela 2026-03-05 145808" src="https://github.com/user-attachments/assets/7d3e01d2-8aea-4b4b-b04f-c44d39f404ad" />



<img width="1274" height="534" alt="Captura de tela 2026-03-05 150629" src="https://github.com/user-attachments/assets/3a8ed0ee-e7cc-4a36-8ffb-2045c2dc18cf" />



<img width="1919" height="811" alt="Captura de tela 2026-03-03 185835" src="https://github.com/user-attachments/assets/b1666d30-932e-40c7-82b5-0b076bd5eb42" />



<img width="1919" height="854" alt="Captura de tela 2026-03-03 185813" src="https://github.com/user-attachments/assets/d22e3f61-231b-4dec-ba67-d097c7d9aaa7" />