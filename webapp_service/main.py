# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from fastapi.middleware.cors import CORSMiddleware
#
# from api.v1.routes import router
# from api.v1.views import router as views
#
# from os import getenv
#
# app = FastAPI()
# app.mount("/static", StaticFiles(directory="./build/static"), name="static")
#
# origins = [
#     "http://localhost:3000",
#     "*"
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# app.include_router(router)
# app.include_router(views)
