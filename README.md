# 🧱 YT_ELT — YouTube Data ELT Pipeline

## 🚀 Objectif du projet
Ce projet a pour but de construire un pipeline **ELT (Extract, Load, Transform)** complet en Python autour de la collecte et du traitement de données issues d’**APIs**, leur stockage dans un **data warehouse PostgreSQL**, puis leur orchestration via **Apache Airflow**.

---

## 🧩 Description
Le pipeline a pour mission de :
1. **Extraire** les données depuis des APIs (par exemple, YouTube Data API) à l’aide de scripts Python et Postman.
2. **Charger** les données dans un entrepôt de données (**PostgreSQL**).
3. **Transformer** les données directement dans le data warehouse.
4. **Orchestrer et automatiser** les tâches grâce à **Apache Airflow**.
5. **Containeriser** les différentes briques de l’application avec **Docker** pour plus de portabilité et de scalabilité.

---

## 🛠️ Stack technique

| Outil / Technologie | Rôle principal |
|----------------------|----------------|
| **Python 3.12+** | Développement des scripts ETL/ELT |
| **PostgreSQL** | Data Warehouse |
| **DBeaver / psql** | Interaction et exploration des données |
| **Docker** | Conteneurisation des services |
| **Apache Airflow** | Orchestration et planification du pipeline |
| **Requests / python-dotenv** | Requêtes API et gestion des variables d’environnement |
| **Pandas** | Transformation et manipulation de données |

---

