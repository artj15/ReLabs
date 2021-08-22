import fastapi
import uvicorn
from views import site
from pathlib import Path
from fastapi.staticfiles import StaticFiles

api = fastapi.FastAPI()
api.mount(
    '/static',
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name='static',
)



def configure():
    api.include_router(site.router)


configure()
if __name__ == '__main__':
    uvicorn.run(api)
