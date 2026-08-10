from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "HRM API is running"
    }

employees = [
    {
        "name": "John Doe",
        "age": 30,
        "position": "Software Engineer",
        "department": "Engineering",
    },
    {
        "name": "Jane Smith",
        "age": 28,
        "position": "Product Manager",
        "department": "Product",
    },
    {
        "name": "Alice Johnson",
        "age": 35,
        "position": "Data Scientist",
        "department": "Data",
    },
    {
        "name": "Bob Brown",
        "age": 40,
        "position": "UX Designer",
        "department": "Design",
    },
    {
        "name": "Charlie Davis",
        "age": 32,
        "position": "DevOps Engineer",
        "department": "Operations",
    },
]

@app.get("/employees")
def get_employees():
    return employees