from starlette.background import BackgroundTask
from starlette.endpoints import HTTPEndpoint
from starlette.responses import FileResponse, HTMLResponse
from weasyprint import HTML

from app.globals import templates
from app.utils import cleanup, random_string


class Home(HTTPEndpoint):
    async def get(self, request):
        template = "home.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)


class FromString(HTTPEndpoint):
    async def get(self, request):
        template = "from_string.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)

    async def post(self, request):
        form = await request.form()
        filename = await random_string(10)
        path = f"/tmp/{filename}.pdf"
        content = form["string"]
        html = HTML(string=content)
        html.write_pdf(path)
        task = BackgroundTask(cleanup, path=path)
        return FileResponse(
            path, media_type="application/pdf", filename="output.pdf", background=task
        )


class FromURL(HTTPEndpoint):
    async def get(self, request):
        template = "from_url.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)

    async def post(self, request):
        form = await request.form()
        filename = await random_string(10)
        path = f"/tmp/{filename}.pdf"
        url = form["url"]
        html = HTML(url=url)
        html.write_pdf(path)
        task = BackgroundTask(cleanup, path=path)
        return FileResponse(
            path, media_type="application/pdf", filename="output.pdf", background=task
        )
