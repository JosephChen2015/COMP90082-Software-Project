# COMP90082-Software-Project

## Create a new instance on nectar
Run the following code **locally** (requires local installation of ansible dependencies)：
```shell
cd nectar
./run-nectar.sh
```

## Deploy both front-end and back-end
Enter the following command in the terminal in the ‘deployment’ directory
```shell
docker-compose up -d
```

## Deploy the back-end separately
Enter the following command in the terminal in the ‘deployment’ directory
```shell
cd backend
docker build -t backend .
docker run -p 5000:5000 -d -it --name backend backend
```

## Deploy the front-end separately
Enter the following command in the terminal in the ‘deployment’ directory
```shell
cd frontend
docker build -t frontend .
docker run -p 8080:80 -d --name frontend frontend
```
