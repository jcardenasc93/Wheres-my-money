""" App entrypoint """

from fastapi import FastAPI
import uvicorn

from config.app_config import AppConfigManager

app_config = AppConfigManager()
app = FastAPI()

app.add_event_handler("startup", app_config.db.connect_db)
app.add_event_handler("shutdown", app_config.db.close_connection)


@app.get("/are-you-alive/")
async def live_server():
    return {"data": "Yes I am"}


if __name__ == '__main__':
    uvicorn.run(app_config.module_name,
                host=app_config.host,
                port=app_config.port,
                reload=app_config.reload)
