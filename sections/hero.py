from nicegui import ui


def render():
    # Big container
    with ui.element("div").style(
        """background-image: url(/assets/hero.jpg);background-size: cover; background-position: center; width: 100%; min-height: 100vh; inset: 0; z-index: -2;"""
    ).classes("flex flex-col justify-center items-center relative"):

        # Overlay (semi-transparent dark layer)
        ui.element("div").style(
            """background: rgba(0, 0, 0, 0.5); position: absolute; inset: 0; z-index: -1;"""
        )

        # Foreground content (your UI stays the same here)
        with ui.element("div").classes(
            "h-screen w-screen flex flex-col bg-cover bg-center justify-center items-center relative"
        ):

            # Navbar
            with ui.element("nav").classes(
                "flex flex-row justify-between items-center w-full fixed left-0 top-0 px-20 py-10"
            ):

                # Logo
                with ui.element("div").classes("text-red"):
                    ui.label("CHALE CIAO").classes("font-lobster font-bold text-4xl")
                    ui.label("Cafe").classes(
                        "font-poppins text-center font-bold text-2xl"
                    )

                # Navlinks
                navlinks = [
                    {"title": "Home", "path": "/"},
                    {"title": "Menu", "path": "/"},
                    {"title": "Reservation", "path": "/"},
                    {"title": "Gallary", "path": "/"},
                    {"title": "About", "path": "/"},
                    {"title": "Blog", "path": "/"},
                    {"title": "Contact", "path": "/"},
                ]

                with ui.row():
                    for item in navlinks:
                        ui.link(item["title"], item["path"]).classes(
                            "font-roboto no-underline uppercase text-red font-bold"
                        )

                # Socials
                with ui.row().classes("text-red"):
                    ui.html('<i class="fab fa-facebook fa-1x"></i>')
                    ui.html('<i class="fab fa-instagram fa-1x"></i>')
                    ui.html('<i class="fab fa-x-twitter fa-1x"></i>')

            # Hero Text
            with ui.element("div").classes("text-red font-bold text-center"):
                ui.label("Akwaaba to").classes("font-lobster text-5xl")
                ui.html("<h1>CHALE CIAO!</h1>").classes("font-poppins text-7xl")
                ui.button("CHECK MENU").classes(
                    "font-roboto bg-white text-red px-6 py-2 mt-4 rounded-lg"
                )
