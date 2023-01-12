import json
import asyncio
import nest_asyncio
import aiosqlite
import aiofiles
from aiohttp import web
import sqlite3
nest_asyncio.apply()
import aiohttp
import sqlite3
import requests
import nest_asyncio
nest_asyncio.apply()

routes = web.RouteTableDef()

# provjera postoje li podaci u DB + ispis broja redaka
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("SELECT COUNT(*) FROM baza3")
broj_redaka = c.fetchone()[0]
if broj_redaka == 0:
    print("Baza je prazna.")
else:
    print(f"Baza nije prazna. Ima {broj_redaka} redova.")

# funkcija za popunjavanje DB s testnim podacima
async def fill_data(data):
    line_data = [json.loads(line) for line in data]
    redovi = []
    async with aiosqlite.connect("database.db") as db:
        for item in line_data:
            username = item["repo_name"].rsplit("/",1)[0]
            ghlink = f"https://github.com/{item['repo_name']}.com"
            path_parts = item["path"].rsplit("/", 1)
            filename = path_parts[1] if len(path_parts) > 1 else item["path"]
            await db.execute(
                "INSERT INTO baza3 (username, ghlink, filename) VALUES (?,?,?)",
                (username, ghlink, filename))
        async with db.execute("SELECT * FROM baza3 LIMIT 100") as cur:
            columns = [column[0] for column in cur.description]
            rezultat = await cur.fetchall()
            for row in rezultat:
                redovi.append(dict(zip(columns, row)))
            url = 'http://127.0.0.1:8081'
            requests.post(url, json=redovi)
            await db.commit()
    return redovi

@routes.get("/getData")
async def get_Data(req):
    # izvodi se IFF je baza prazna
    if broj_redaka == 0:
        async with aiofiles.open('data.json', mode='r') as file_data:
            read_data = {await file_data.readline() for _ in range(1000)}
            data = await fill_data(read_data)
        return web.json_response(data, status=200)
    else:
        #ukoliko baza nije prazna, vraća ERROR 400
        return web.json_response({"error":"Database is not empty."}, status=400)
    
app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8080)
