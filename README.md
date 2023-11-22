# Log Ingestor and Query Interface Documentation

This documentation provides a detailed guide on setting up and using the Log Ingestor and Query Interface project. Log Ingestor and Query Interface project, powered by Django, Elastic Search, and Kibana is a comprehensive and efficient solution for managing and deriving insights from log data. This combination not only ensures a robust backend but also provides an accessible and insightful interface for users across various technical backgrounds. With a focus on simplicity, scalability, and speed, our project is poised to meet the ever-growing demands of log data management in today's dynamic IT landscape.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup](#setup)
   - [Django Setup](#django-setup)
   - [ElasticSearch Setup](#elasticsearch-setup)
   - [Kibana Setup](#kibana-setup)
3. [Run the Project](#run-the-project)
4. [Ingesting Logs](#ingesting-logs)
5. [Query Interface](#query-interface)
6. [Advanced Features](#advanced-features) 

## Project Overview

The Log Ingestor and Query Interface project is designed to address the critical need for efficiently handling and querying vast volumes of log data and provide a user-friendly interface for querying this data. In a world where system logs are invaluable for troubleshooting and performance optimization, our project offers a robust solution that combines simplicity, scalability, and speed.The system is built using Django as the web framework, Elastic Search, and Kibana for efficient log data indexing and retrieval.

## Setup

### Django Setup

To set up the Django project from the GitHub repository, follow these steps:

#### 1. Clone the Repository

```bash
git clone https://github.com/Exp-Communicate-Using-Markdown-Cohort-1/series-communicate-using-markdown-siddhardh-7.git
cd log_search_project
```

#### 2. Create a Virtual Environment

Create and activate a virtual environment to isolate the project dependencies:
When one clone's the github repo from above, it will come with env; they can use that one or delete the folder and create a new virtual environment.

```bash
python -m venv env
source env/bin/activate  # On Windows, use 'env\Scripts\activate'
```

#### 3. Install Dependencies

Install the required Python modules specified in the `requirements.txt` file:
File: [requirements.txt](https://github.com/Exp-Communicate-Using-Markdown-Cohort-1/series-communicate-using-markdown-siddhardh-7/blob/main/log_search_project/requirements.txt)

```bash
pip install -r requirements.txt
```

### ElasticSearch Setup

1. Install Elasticsearch: Follow the official Elasticsearch installation guide. (https://www.elastic.co/downloads/elasticsearch)

2. Visit http://localhost:9200 to access the logs in elastic search after successfully running the Elastic Search.
> After we ingest the logs, the image is going to be down one.

![elasticsearch](https://github.com/Exp-Communicate-Using-Markdown-Cohort-1/series-communicate-using-markdown-siddhardh-7/assets/84370785/9970af55-461a-4343-bcb5-b5951a222917)


### Kibana Setup

1. Install Kibana: Follow the official Elasticsearch installation guide. (https://www.elastic.co/downloads/kibana)

2. Visit http://localhost:5601 to access the query interface of Kibana after successfully running kibana.
> After we ingest the logs, the image is going to be down one.

![logs list](https://github.com/Exp-Communicate-Using-Markdown-Cohort-1/series-communicate-using-markdown-siddhardh-7/assets/84370785/056ca156-298c-431a-a8f6-e762f9fa0bf9)

## Run the Project

Run the development server:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 3000
```

Visit `http://localhost:3000` to access the query interface.

## Ingesting Logs

To ingest logs, a simple HTTP endpoint is provided. Logs are sent in JSON format to the `/ingest/` endpoint. And logs are seamlessly ingested via an HTTP server on port 3000, promoting standardized and accessible entry points. This streamlined process not only aligns with specified requirements but also underscores our commitment to reliability and efficiency in handling diverse log data sources.

Example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"level": "error", "message": "Failed to connect to DB", "resourceId": "server-1234", "timestamp": "2023-09-15T08:00:00Z", "traceId": "abc-xyz-123", "spanId": "span-456", "commit": "5e5342f", "metadata": {"parentResourceId": "server-0987"}}' http://localhost:3000/ingest/
```

or

Running this command 100 times to ingest 100 logs is time-consuming and also not an efficient way to send logs for testing.
So, we will run a Python program to send the logs using a post request. One can examine the Python program, which can be found file [random_log_ingestor.py](https://github.com/Exp-Communicate-Using-Markdown-Cohort-1/series-communicate-using-markdown-siddhardh-7/blob/main/random_log_ingestor.py)


## Query Interface

Our Query Interface is seamlessly integrated with Kibana, a powerful data visualization platform, enhancing the user experience and providing valuable insights into log data. Kibana plays a pivotal role in facilitating queries and allows users to search logs based on various filters, such as finding all logs with the level set to "error," searching for logs with specific messages like "Failed to connect," retrieving logs related to a specific resourceId, and filtering logs within defined timestamp ranges.

By leveraging Kibana's intuitive interface and real-time dashboards, users can effortlessly execute complex queries with just a few clicks. The integration empowers users to visualize log data trends, identify patterns, and efficiently troubleshoot issues. The ability to filter logs based on various criteria, such as error levels, specific messages, resourceIds, and timestamps, enhances the precision and granularity of log analysis.

To visualize the data, set up the index pattern in Kibana: [Tutorial](https://www.youtube.com/watch?v=wT-6RXA3K8w&ab_channel=CodingExplained)
In our case, the Index name is "logs"

> The dashboard can be customized to the user's preferences. Kibana offers the ability to customize a variety of graphs and charts to the user's specifications.

![dashboard](https://github.com/Exp-Communicate-Using-Markdown-Cohort-1/series-communicate-using-markdown-siddhardh-7/assets/84370785/73e8ac9f-f2af-45c0-82a8-2ffb15b26eaf)

Example queries:

- Find all logs with the level set to "error".
- Search for logs with the message containing the term "Failed to connect".
- Retrieve all logs related to resourceId "server-1234".
- Filter logs between the timestamp "2023-09-10T00:00:00Z" and "2023-09-15T23:59:59Z".

![filters](https://github.com/Exp-Communicate-Using-Markdown-Cohort-1/series-communicate-using-markdown-siddhardh-7/assets/84370785/b7c5a8f4-d322-4d26-a729-b472b77baadf)

![log](https://github.com/Exp-Communicate-Using-Markdown-Cohort-1/series-communicate-using-markdown-siddhardh-7/assets/84370785/e2cf4b17-b0e9-41db-b370-d62dc47d432d)

## Advanced Features

The project includes advanced features that enhance the functionality:

- **Date Range Filtering:** Filter logs between specific timestamp ranges.
- **Combining Multiple Filters:** Users can apply multiple filters simultaneously.
