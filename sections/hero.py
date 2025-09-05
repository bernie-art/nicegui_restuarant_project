from nicegui import ui


def render():
    #  big container
    with ui.element("div").style("background-image: url(/assets/hero.jpg)").classes("h-screen w-screen flex flex-col bg-cover bg-center justify-center items-center"):
        #  navbar
        with ui.element("nav").classes("flex flex-row justify-between items-center w-full fixed left-0 top-0 px-20 py-10"):
        #    logo
            ui.label("S.K").classes("text-white font-bold text-2xl")

            # navlinks
            navlinks = [{"title": "Home", "path": "/"}, {"title": "Menu", "path": "/"}, {"title": "Reservation", "path": "/"}, {"title": "Gallary", "path": "/"}, {"title": "About", "path": "/",}, {"title": "Blog", "path": "/",}, {"title": "Contact", "path": "/"}]

            with ui.row():
                for item in navlinks:
                    ui.link(item["title"], item["path"]).classes("no-underline uppercase text-white font-bold")

            # Socials
            with ui.row().classes("text-white"):
                ui.html('<i class="fab fa-facebook fa-1x"></i>')
                ui.html('<i class="fab fa-instagram fa-1x"></i>')
                ui.html('<i class="fab fa-x-twitter fa-1x"></i>')

        #  Text
        with ui.element("div").classes("text-red font-bold text-center"):
            ui.label("Welcome to").classes("text-4xl")
            ui.html("<h1>Sankofa Boulangerie</h1>").classes("text-6xl")
            ui.button("Look Menu", color="red-800").classes("text-white")