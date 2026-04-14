from app import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#app-header", "Pink Morsel Sales Visualiser", timeout=4)
    assert dash_duo.find_element("#app-header").text == "Pink Morsel Sales Visualiser"


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.wait_for_element("#sales-line-chart", timeout=4)
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    region_picker = dash_duo.wait_for_element("#region-selector", timeout=4)
    assert region_picker is not None