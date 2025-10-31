# On définit les arguments de version pour Airflow et Python
ARG AIRFLOW_VERSION=2.9.2
ARG PYTHON_VERSION=3.10

# On utilise l’image officielle d’Airflow correspondant aux versions choisies
FROM apache/airflow:${AIRFLOW_VERSION}-python${PYTHON_VERSION}

# On définit la variable d’environnement pour le répertoire d’Airflow
ENV AIRFLOW_HOME=/opt/airflow

# On copie le fichier requirements.txt à la racine de l’image
COPY requirements.txt /requirements.txt

# On installe Airflow et les dépendances sans mise en cache pour réduire la taille de l’image
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
