
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import State, Input, Output
import dash_daq as daq
from dash_daq import DarkThemeProvider as DarkThemeProvider

app = dash.Dash(__name__)

# This is for Heroku
server = app.server

# This is to use Dash DAQ
app.scripts.config.serve_locally = True

# This is for the Dark Theme Provider
app.config['suppress_callback_exceptions'] = True


# CSS Imports
external_css = ["https://codepen.io/chriddyp/pen/bWLwgP.css",
                "https://cdn.rawgit.com/matthewchan15/dash-css-style-sheets/adf070fa/banner.css",
                "https://fonts.googleapis.com/css?family=Raleway:400,400i,700,700i",
                "https://fonts.googleapis.com/css?family=Product+Sans:400,400i,700,700i"]


for css in external_css:
    app.css.append_css({"external_url": css})

root_layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(
            [
                daq.ToggleSwitch(
                    id='toggleTheme',
                    style={
                        'position': 'absolute',
                        'transform': 'translate(-50%, 20%)'
                    },
                    size=25
                ),
            ], id="toggleDiv",
            style={
                'width': 'fit-content',
                'margin': '0 auto'
            }
        ),
        html.Div(id='page-content'),
    ]
)

light_layout = html.Div(
   [
        html.Div(
            id="container",
            style={"background-color": "#20304C"},

            children=[
                html.H2(
                    "Dash DAQ: Example App",
                ),
                html.A(
                html.Img(
                    src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/excel/dash-daq/dash-daq-logo-by-plotly-stripe+copy.png",
                ),
                href="http://www.dashdaq.io"
                )
            
        ],
        className="banner"
        ),
        html.Div(
            [   
                daq.Indicator(
                    id="color-led",
                    label="LED",
                    value=True,
                    color="#9B51E0",
                    width=16,
                    height=20,
                    className="two columns offset-by-two",
                    style={"paddingTop":"10%"}
                ),
                html.Div(
                    [
                        daq.ColorPicker(
                            id="color-picker",
                            label="Color Picker",
                            value=dict(hex="#119DFF"),
                        )
                    ], className="four columns"
                )
            ], className="row"
        )
   ], style={'padding': '0px 10px 0px 10px',
                   'marginLeft': 'auto',
                   'marginRight': 'auto',
                   "width": "1100",
                   'height': "1000",
                   'boxShadow': '0px 0px 5px 5px rgba(204,204,204,0.4)'
                   }
)

dark_layout = DarkThemeProvider(
    [
        html.Link(
            href="https://cdn.rawgit.com/matthewchan15/dash-css-style-sheets/94fdb056/dash-daq-dark.css",
            rel="stylesheet"
        ),
        html.Div(
            [

            
        html.Div(
            id="container",
            style={"background-color": "#20304C"},

            children=[
                html.H2(
                    "Dash DAQ: Example App",
                ),
                html.A(
                html.Img(
                    src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/excel/dash-daq/dash-daq-logo-by-plotly-stripe+copy.png",
                ),
                href="http://www.dashdaq.io"
                )
            
        ],
        className="banner"
        ),
       html.Div(
            [   
                daq.Indicator(
                    id="color-led",
                    label="LED",
                    value=True,
                    color="#9B51E0",
                    width=16,
                    height=20,
                    className="two columns offset-by-two",
                    style={"paddingTop":"10%"}
                ),
                html.Div(
                    [
                        daq.ColorPicker(
                            id="color-picker",
                            label="Color Picker",
                            value=dict(hex="#119DFF"),
                        )
                    ], className="four columns"
                )
            ], className="row"
        )
   ], style={'padding': '0px 10px 0px 10px',
                   'marginLeft': 'auto',
                   'marginRight': 'auto',
                   "width": "1100",
                   'height': "1000",
                   'boxShadow': '0px 0px 5px 5px rgba(204,204,204,0.4)'
                   }
)
]
)

app.layout = root_layout

# Callback for Dark Theme Provider
@app.callback(Output('toggleTheme', 'value'),
              [Input('url', 'pathname')])
def display_page(pathname):
    
    if pathname == '/dark':
        return True
    else:
        return False

# Callback for Dark Theme Provider
@app.callback(Output('page-content', 'children'),
              [Input('toggleTheme', 'value')])
def page_layout(value):
    if value:
        return dark_layout
    else:
        return light_layout

# Color Picker LED
@app.callback(
    Output('color-led', 'color'),
    [Input('color-picker', 'value')]
    )
def color_picker_led(color):
    return color['hex']

# Color Picker Banner
@app.callback(
    Output("container", "style"),
    [Input("color-picker", "value")]
)
def color_picker(color):
    style = {"background-color": ""}
    style["background-color"] = color['hex']
    return style

if __name__ == '__main__':

    app.run_server(debug=True)
