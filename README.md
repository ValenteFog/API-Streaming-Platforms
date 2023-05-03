<p align="center" width="100%">
    <img width="10%" src="https://es.logodownload.org/wp-content/uploads/2018/11/netflix-logo-51.png">
    <img width="10%" src="https://logodownload.org/wp-content/uploads/2019/09/hulu-logo.png">
    <img width="10%" src="https://logodownload.org/wp-content/uploads/2020/11/disney-plus-logo-1.png">
    <img width="10%" src="https://logodownload.org/wp-content/uploads/2018/07/prime-video.png">
</p>

# <h1 align=center> **API for streaming platforms** </h1>

# <h1 align=center>**`Data Engineering`**</h1>


## ¡Welcome! 
We have 4 datasets from well-known streaming platforms: Amazon Prime, Disney+, Hulu, and Netflix. These datasets are contained in files with different extensions (csv and json), and our task is to ingest them, apply relevant transformations, and then make the clean data available for querying through an API. This API should be built in a Dockerized virtual environment and will be deployed on Mogenius.com. 

<hr>  

## Links:
API on Mogenius: https://pi01-data05-prod-pi01-data05-z6994f.mo6.mogenius.io/ *(Update: no longer available due to service changes)*

Video presentation: https://www.youtube.com/watch?v=j5qsUhYff_0 *(In Spanish)*

<hr>

## **Project Scope**
For this project, we should be able to:

* Ingest and normalize the data.
* Relate and transform the dataset as necessary to perform queries.
* Create an API in a Docker environment.
* Perform the requested queries, as outlined in the following section.
* Create a demonstration video.
* Deploy the API on Mogenius.

<br>

### The queries to be performed are:

+ Maximum duration by type of film (movie/series), by platform, and by year:
    The request should be: get_max_duration(year, platform, [min or season])

+ Number of movies and series (separate) by platform:
    The request should be: get_count_platform(platform)

+ Number of times a genre and platform occur together most frequently.
    The request should be: get_listed_in('genre')
    As an example of genre, you can use 'comedy', which should return a count of 2099 for the Amazon platform.

+ Actor who appears most frequently by platform and year.
    The request should be: get_actor(platform, year)

<br>

## **Files within the Repository**
Within this repository, we have a series of files and folders that we will briefly outline.

* **'Processes.ipynb'** is a Jupyter notebook where the project is essentially deployed. It consists of a first part where the data is ingested, explored, and then transformed based on our needs (ETL). The final output is a '.csv' file containing the processed information that will be used by the API. A second part exposes the functions that will be used to perform queries on the API we create.

* **'Dockerfile'** contains the necessary instructions to create a container image from scratch and indicates the base image that will be used, in our case FastAPI.

* **'Datasets'** folder includes 5 files. Four of them are the sources of our data that were provided to us for this project. The fifth file is the '.csv' resulting from the *ETL* process we performed in the notebook, which will be taken by the API to perform the queries.

* **'app'** folder contains the 'main.py' file, a Python file that contains everything needed to set up the API. Here, FastAPI is instantiated, the homepage for our API is defined, and the code for performing queries (which is also brought from the notebook) is written.

## **Technologies Used**

+ Python
+ Docker
+ Python libraries: pandas, FastAPI
+ Mogenius.com
+ Github
