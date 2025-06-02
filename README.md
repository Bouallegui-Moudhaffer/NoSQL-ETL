# Healthcare ETL & MongoDB Demo

## Overview

This project demonstrates a straightforward way to load a healthcare CSV file into MongoDB using a multi-container Docker setup. It also provides a Jupyter Notebook to explore the data model and run basic queries, plus a web interface (mongo-express) to inspect the collection visually.

## Components

1. **Docker Compose Services**  
   - **Jupyter Notebook/Lab**: An interactive environment for designing the data model (Step 1) and running MongoDB queries (Step 4).  
   - **MongoDB**: Stores patient records loaded from the CSV.  
   - **mongo-express**: A lightweight web UI for browsing the MongoDB database.  
   - **ETL Python Container**: Automatically runs a script that reads the CSV, cleans data, and inserts records into a `patients` collection.

2. **Environment File (`.env`)**  
   Holds MongoDB credentials so they are not hard-coded into service definitions.

3. **ETL Script**  
   - Reads a semicolon-delimited CSV from a shared volume  
   - Normalizes column names and date fields, fills missing values  
   - Bulk-inserts all rows into the `patients` collection in MongoDB

4. **Jupyter Notebook**  
   - Step 1: Propose a simple MongoDB document schema based on the CSV structure  
   - Step 4: Execute queries such as “count all patients,” “patients admitted after 2023-01-01,” medication frequencies, etc.

## Quick Setup

1. **Add the CSV**  
   Place your healthcare CSV file in the `./data` folder (named exactly as expected by the ETL script).

2. **Configure Credentials**  
   Verify or update the `.env` file with your preferred MongoDB username and password.

3. **Launch Services**  
   Run `docker-compose up -d` to start all containers:
   - The ETL container will automatically process the CSV and load data into MongoDB.  
   - The Jupyter Notebook service will be available on port 9988.  
   - The mongo-express web UI will be available on port 8081.

4. **Explore the Data**  
   - Open Jupyter Lab (http://localhost:9988) to review the proposed schema and run queries in the provided notebook.  
   - Open mongo-express (http://localhost:8081) to browse the `healthcare.patients` collection directly.

5. **Stopping Everything**  
   When finished, run `docker-compose down` to stop and remove containers. MongoDB data persists in a Docker volume, so you can restart later without reloading.
