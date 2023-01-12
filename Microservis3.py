from aiohttp import web
import json
import logging
import nest_asyncio
nest_asyncio.apply()

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

routes = web.RouteTableDef()

# uzima JSon podatke, filtrira D s list comprehension. Vraća username sa d ili log-ira greske
@routes.post("/")
async def WTd(request):
    try:
        data = await request.json()
        username_d = [d['username'] for d in data if 'username' in d and d['username'].lower().startswith('d')]
        print(username_d)
        return web.json_response(username_d, status=200)
    except json.decoder.JSONDecodeError:
        logger.error("Invalid JSON data")
        return web.json_response({"error": "Invalid JSON data"}, status=400)
    except Exception as e:
        logger.error("Error: %s", e)
        return web.json_response({"error": "Error tokom procesuiranja requesta."}, status=500)

app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8083)
