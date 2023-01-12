from aiohttp import web
import json
import logging
import nest_asyncio
nest_asyncio.apply()

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

routes = web.RouteTableDef()

# uzima JSon podatke, filtrira W s list comprehension. Vraća username sa w ili log-ira greske
@routes.post("/")
async def WTw(request):
    try:
        data = await request.json()
        username_w = [w['username'] for w in data if 'username' in w and w['username'].lower().startswith('w')]

        print(username_w)
        return web.json_response(username_w, status=200)
    except json.decoder.JSONDecodeError:
        logger.error("Invalid JSON data")
        return web.json_response({"error": "Invalid JSON data"}, status=400)
    except Exception as e:
        logger.error("Error: %s", e)
        return web.json_response({"error": "Error tokom procesuiranja requesta."}, status=500)

app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8082)
