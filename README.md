
#Data Warehouse for City Traffic Data - 

This repository contains the necessary information and resources to set up a scalable data warehouse for city traffic data. The data warehouse is designed to store and analyze vehicle trajectory data collected by swarm UAVs (drones) and static roadside cameras. The data warehouse uses a tech stack comprising PostgreSQL as the database, DBT for Extract Load Transform (ELT) workflows, and Airflow for workflow orchestration.
Business Need

The objective of this project is to assist the city traffic department in improving traffic flow and undertaking various data-driven projects by leveraging the vehicle trajectory data collected from multiple locations in the city. This data will provide critical insights and intelligence to optimize traffic management and support future initiatives.
##Data Warehouse Architecture

The data warehouse follows an ELT (Extract Load Transform) framework, which allows analytic engineers to set up transformation workflows as needed. The architecture consists of the following components:

    Data Sources: The raw data is collected from swarm UAVs and static roadside cameras, capturing vehicle trajectory information. These data sources feed into the data warehouse for further processing and analysis.

    MySQL/PostgreSQL Database: The data warehouse utilizes either MySQL or PostgreSQL as the relational database management system (RDBMS) for storing and querying the collected data. Choose one of these databases based on your specific requirements and preferences.

    DBT (Data Build Tool): DBT is a powerful tool used for Extract Load Transform (ELT) workflows. It allows you to define transformations and build data models on top of your raw data. With DBT, you can create reusable and maintainable SQL transformations, manage dependencies between tables, and ensure data consistency.

    Airflow: Airflow is an open-source platform used for workflow orchestration and scheduling. It provides a rich set of features for managing and automating data pipelines. In this project, Airflow is used to schedule and execute DBT jobs, ensuring that the data transformations are performed on a regular basis.

##Repository Structure

This repository is organized as follows:

    /data: This directory contains sample data files representing the raw vehicle trajectory data collected from the swarm UAVs and static roadside cameras. Use this data to simulate the data ingestion process.

    /dbt: This directory contains the DBT project, including the configuration files and SQL transformations. Customize these files to match your specific requirements and data models.

    /airflow: This directory contains the Airflow DAGs (Directed Acyclic Graphs) that define the data pipeline workflows. Customize these DAGs to schedule and execute the DBT jobs based on your desired frequency.

    README.md: This file provides an overview of the project, its objectives, and the repository's structure.

##Getting Started

To set up the data warehouse and start processing the city traffic data, follow these steps:

    Choose either MySQL or PostgreSQL as your RDBMS, and ensure it is installed and properly configured on your system.

    Set up DBT by installing it on your machine. Refer to the DBT documentation for installation instructions: https://docs.getdbt.com/

    Configure the DBT project located in the /dbt directory. Customize the database connection settings in the profiles.yml file to point to your MySQL or PostgreSQL instance.

    Define the necessary transformations in DBT by creating SQL files in the /dbt/models directory. These transformations should process the raw vehicle trajectory data into meaningful insights and analytics.

    Set up Airflow by installing it on your machine. Refer to the Airflow documentation for installation instructions: https://airflow.apache.org/docs/

    Customize the Airflow DAGs located in the /airflow/dags directory. These DAGs should define the workflow and scheduling for executing the DBT jobs. Adjust the schedule and dependencies according to your needs.

    Test the data pipeline by running the Airflow DAGs and monitoring the execution. Ensure that the data is loaded into the database and the transformations are applied successfully.

    Once the data pipeline is running smoothly, you can explore different downstream projects and analytics that leverage the data stored in the data warehouse. Use SQL queries or BI tools to query and analyze the data for various use cases.

##Conclusion

By setting up this scalable data warehouse for city traffic data, you can efficiently store, process, and analyze vehicle trajectory data collected from swarm UAVs and static roadside cameras. The ELT framework using DBT allows you to define and manage data transformations effectively, while Airflow ensures the orchestration and scheduling of the data pipeline. With this infrastructure in place, you can support various downstream projects and initiatives to improve traffic flow and gain critical intelligence from the collected data