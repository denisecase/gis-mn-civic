import ipywidgets as widgets

def county_selector():
    # Eventually extendable to more counties
    return widgets.Dropdown(
        options=[("St. Louis County", "county_69_slc")],
        value="county_69_slc",
        description="County:",
        layout=widgets.Layout(width="50%")
    )