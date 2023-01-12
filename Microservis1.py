from aiohttp import web
import requests
import json
import asyncio
import aiofiles
import aiohttp
import aiosqlite
from aiohttp import web
import sqlite3
import requests
import nest_asyncio
nest_asyncio.apply()
import logging

routes = web.RouteTableDef()

# Pracenje errora 
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# Req: Uzima json podatke, prelazi preko svakog dict-ija i stavlja u listu. 
# Vraća Json rez
@routes.post("/")
async def M1(request):
    try:
        podaci = await request.json()
        ds = []
        for dictionary in podaci:
            ds.append(dictionary)
        rez = ds
        print("rezultat", rez)
        #url1 = 'http://127.0.0.1:8083/'
        #url2 = 'http://127.0.0.1:8084/'
        #requests.post(url1, json=result)
        #requests.post(url2, json=result)
        return web.json_response(rez, status=200)
    except Exception as e:
        logger.error("Error: %s", e)
        return web.json_response({"error": "Error tokom procesirana requesta."}, status=500)
    
app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8081)
