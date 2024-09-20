# Docker Compose Simple Practice

## Description

This project demonstrates a simple setup using Docker Compose to build and run a backend and frontend application using pre-defined Docker images. The main focus is on simplifying the setup process for running multiple services in a unified environment.

<br>

## Features:
- **Backend Service**: A Python API (`Flask`) that interacts with a MySQL/MariaDB database.
- **Frontend Service**: A basic `HTML/JavaScript` web app that sends requests to the backend API.
- **Docker Compose Integration**: Run both services using `docker-compose.yml`, or start from build the service images using a single `docker-compose.build.yml` file.

<br>

## Prerequisites
- `Docker`: Make sure Docker is installed on your machine.
- `Docker Compose`: You should have Docker Compose installed.
- `MySQL/MariaDB`: You need to create a table first, using this command bellow.<br>
    ```mysql
    CREATE TABLE items (
        id INT AUTO_INCREMENT PRIMARY KEY,
        thing VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL
    );
    ```

<br>

## Folder Structure:
```
docker-compose-simple-practice/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   ├── script.js
│   │   └── style.css
│   │
│   └── Dockerfile
│
├──  docker-compose.build.yml
│
└──  docker-compose.yml
```

<br>

## Configure your own
It's important to configure several settings in the `docker-compose.yml` or `docker-compose.build.yml` file so that you don't encounter errors.
1. Environment Variable

    ```
    services:
        backend:
            ...
            environment:
            - DB_HOST=<your_db_host_ip>
            - DB_USER=<your_db_user>
            - DB_PASSWORD=<your_db_password>
            - DB_NAME=<your_db_name>
            ...

        frontend:
            ...
            environment:
            - API_BASE_URL=http://<your_backend_docker_api>:2020
            ...
    ```
2. Docker Network
    ```
    $ docker network create --subnet=192.168.15/24 docker_network
    ```

<br>

## Getting Started
Clone this repository:

```bash
$ git clone https://github.com/thisilfa/docker-compose-simple-practice.git
$ cd docker-compose-simple-practice
```

### Building and Running Locally
Build and run using `docker-compose.build.yml`:
```bash
$ docker-compose -f docker-compose.build.yml up --build
```

### Using Pre-built Docker Images
If you prefer to use the pre-built images from mine:
1. Download the images from [Google Drive](https://drive.google.com/drive/folders/1dEkqAN7nk8oBfyIFm4KGg9lBB-c82Uky?usp=sharing) and load them into Docker:
    ```bash
    $ docker load -i backend_image.tar
    $ docker load -i frontend_image.tar
    ```

2. Check if Images are Loaded: After loading, run:
    ```bash
    $ docker images
    ```
    Ensure that both `flask-app:<ver>` and `web-app:<ver>` are listed.

3. Once loaded, run the containers using the standard docker-compose.yml:
    ```bash
    $ docker-compose up
    ```

#### Connecting to the API
- The web app will be accessible at `http://<your-frontend-ip>:8080`.
- The Flask API will be running at `http://<your-backend-ip>:2020`.

