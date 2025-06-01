import ipywidgets as widgets

def layer_selector():
    return widgets.Dropdown(
        options=[
            ("Precincts", "precincts"),
            ("Polling Places", "polling"),
            ("School Districts", "schools"),
            ("Minor Civil Divisions", "mcd"),
            ("County Boundary", "county")
        ],
        value="precincts",
        description="Layer:",
        layout=widgets.Layout(width="50%")
    )