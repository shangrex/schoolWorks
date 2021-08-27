# SchoolWorks-backend

Repository of NCKU CSIE slides,exams, and homeworks

未來可能新增不同系所的東西

## Development

### Prerequisitive

| Name | Version |
| --- | --- |
| Python | 3.8 |
| pipenv(Python module) | 2018.11.26 or up |

### Environment setup

0. Initialize environment variable

```
cp sample.env .env
```

1. Initialize Python environment

```
make init
```

2. Enter the environment and start developing

```
pipenv shell
```

3. Start development API service

```
cd api/
uvicorn app:APP
```
The server will run at http://127.0.0.1:8000

## Contribution

Read the `Contributing.md`
