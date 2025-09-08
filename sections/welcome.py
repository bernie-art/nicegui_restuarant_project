from nicegui import ui


def render():
    #  big container
    with ui.element("div").classes("w-screen h-screen flex flex-row items-center"):

        with ui.element("div").classes(
            "w-[50%] h-screen flex flex-col justify-center items-center text-center p-6"
        ):
            ui.label("Italian Cafe").classes("text-red-600 italic text-3xl")
            ui.label("WELCOME").classes(
                "text-5xl font-extrabold text-black-300 mt-2 font-poppins"
            )
            ui.html(
                "A Fusion of Two Worlds.<br>"
                "At Chale Caio Cafe, we celebrate the romance of Italian cuisine<br>"
                "and the heart of Ghanaian flavors-crafted together for a dinning experience like no other."
            ).classes("mt-6 text-m font-poppins")
            ui.link("OUR STORY >>>", "#").classes(
                "text-black mt-5 px-6 py-3 rounded-lg no-underline"
            )

        # Right side Image Container
        with ui.element("div").classes(
            "w-[50%] h-full flex items-center justify-center"
        ):
            ui.image("/assets/welcome.jpg").classes(
                "w-[70%] h-[65%] object-cover rounded-xl transition-transform duration-500 ease-in-out transform hover:scale-110"
            )
