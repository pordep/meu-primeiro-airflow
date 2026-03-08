# 🚀 Pipeline E-commerce Olist - Arquitetura Medalhão

Este projeto demonstra um pipeline de Engenharia de Dados completo utilizando **Apache Airflow**, **Docker** e **MySQL**.

## 🏗️ Arquitetura (Medalhão)
O pipeline processa os dados de vendas em três estágios:
1.  **Bronze:** Ingestão dos dados brutos do CSV para o MySQL (`bronze_vendas`).
2.  **Silver:** Limpeza e tipagem de dados, incluindo conversão de datas e decimais (`silver_vendas`).
3.  **Gold:** Agregações de negócio para visualização de faturamento diário (`gold_faturamento_diario`).

## 🛠️ Tecnologias
- **Orquestrador:** Airflow (Celery Executor)
- **Containerização:** Docker & Docker Compose
- **Linguagem:** Python (Pandas, SQLAlchemy)
- **Banco de Dados:** MySQL 8.0

## 💡 Desafios Superados (Troubleshooting)

Durante o desenvolvimento, foram resolvidos problemas reais de ambiente:

1. **Compatibilidade de Versões**: Ajuste de parâmetros de `schedule_interval` para `schedule` conforme as novas especificações do Airflow.

2. **Docker Networking**: Resolução de erros de comunicação entre o Worker e o Log Server.

3. **Gerenciamento de Recursos**: Otimização dos containers para rodar em ambiente WSL2.

4. **Segurança de Credenciais**: Substituição de strings de conexão expostas por Airflow Hooks (MySqlHook), centralizando a gestão de segredos na interface administrativa do Airflow.

5. **Persistência de Dados**: Configuração de volumes no Docker Compose para garantir a integridade dos logs e DAGs.

## 📸 Capturas de Tela ##


<img width="654" height="366" alt="Interface Apache Airflow. Dags funcionando" src="https://github.com/user-attachments/assets/56f7ee91-1ccc-4d21-865f-3e4a91036208" />


<img width="654" height="366" alt="Interface MySQL. Query gold_faturamento" src="https://github.com/user-attachments/assets/a8c2468f-63de-4fe2-89c9-2e685bd31ef9" />

## 🔧 Como rodar
1. Clone o repositório.
2. Certifique-se de ter o Docker instalado.
3. Execute: `docker-compose up -d`.
4. Acesse o Airflow em `localhost:8080`.
