from nicegui import ui


def render():
    with ui.element("div").classes("w-screen h-screen flex flex-row items-center"):
        with ui.element("div").classes(
            "font-bold text-center h-full w-full flex flex-col items-center justify-center"
        ):
            ui.label("Discover").classes("text-red-600 text-3xl italic font-lobster")
            ui.label("OUR MENU").classes("text-6xl font-poppins mb-8")
