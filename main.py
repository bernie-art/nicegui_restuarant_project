from nicegui import ui, app
from sections import hero, welcome, menu

#  Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# Load various Google Fonts
ui.add_head_html(
    """
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Roboto:wght@400;700&family=Lobster&display=swap" rel="stylesheet">
<style>
  .font-poppins { font-family: 'Poppins', sans-serif; }
  .font-roboto { font-family: 'Roboto', sans-serif; }
  .font-lobster { font-family: 'Lobster', cursive; }
</style>
"""
)


#  Load font Awesome for social
ui.add_head_html(
    """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />    
"""
)

ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css" />')

hero.render()
welcome.render()
menu.render()

ui.run()
