import web # IMPORTACCION DE WEB.

render = web.template.render("mvc/views/content")

class Referencias():
    
    def GET(self):
        try:
            return render.referencias() # RETORNAMOS EL REDERIZADO.
        except Exception as e:
            return "Error " + str(e.args) # EN CASO DE ERRORES, LOS DEVOLVERA.