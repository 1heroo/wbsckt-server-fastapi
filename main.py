import uvicorn as uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def main():
    return {'message': 'success'}


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='localhost',
        port=8000,
        reload=True
    )