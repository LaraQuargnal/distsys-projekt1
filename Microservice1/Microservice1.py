from aiohttp import web
import asyncio
import requests
import nest_asyncio
nest_asyncio.apply()
import logging

routes = web.RouteTableDef()

# Pracenje errora 
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# Req: Uzima json podatke, prelazi preko svakog dictionarija i stavlja u listu. 
# Vraća Json rez
@routes.post("/")
async def M1(req):
    try:
        podaci = await req.json()
        ds = []
        for dictionary in podaci:
            ds.append(dictionary)
        rez = ds
        print("rezultat", rez)
        veza1 = 'http://127.0.0.1:8082/'
        veza2 = 'http://127.0.0.1:8083/'
        requests.post(veza1, json=rez)
        requests.post(veza2, json=rez)
        return web.json_response(rez, status=200)
    except Exception as e:
        logger.error("Error: %s", e)
        return web.json_response({"error": "Error tokom procesirana requesta."}, status=500)
    
app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8081)
