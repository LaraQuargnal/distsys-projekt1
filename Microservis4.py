from aiohttp import web
import asyncio
import aiofiles
import nest_asyncio
nest_asyncio.apply()

routes = web.RouteTableDef()

wd_usernames = []
file_path = 'file.txt'

@routes.post("/gatherData")
async def gather_data(req):
    jdata = await req.json()
    wd_usernames.extend([username for username in jdata])
    print(wd_usernames)
    
    if len(wd_usernames) > 10:
        async with aiofiles.open(file_path, mode='w') as f:
            await f.write('\n'.join(wd_usernames))
    return web.json_response(wd_usernames, status=200)

app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8084)
