## Installation

### 1. Clone the Repository

Copy the repository to your local machine:

```
git clone https://github.com/damianpud/django_app.git
cd django_app
```

### 2. Run the Application with Docker Compose

```
docker-compose up --build
```

### 3. Run Migrations with Docker Compose

```
docker-compose exec web python manage.py migrate --noinput
```
