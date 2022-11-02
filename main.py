import uvicorn as uvicorn
from app.routes import app


if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='localhost',
        port=8000,
        reload=True
    )
