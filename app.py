import web

urls = [
    '/','mvc.controllers.content.index.Index', 
    '/index/?','mvc.controllers.content.index.Index',
    '/docker/?','mvc.controllers.content.docker.Docker',
    '/ubuntu/?','mvc.controllers.content.ubuntu.Ubuntu',
    '/referencias/?','mvc.controllers.content.referencias.Referencias',
] # COLOCAMOS LA RUTA

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()