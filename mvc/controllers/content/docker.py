import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/content")

class Docker():
    
    def GET(self):
        try:
            return render.docker() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.