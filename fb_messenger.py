####IMPORT NECESSARY LIBRARIES#### 
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
import os

##import dash_auth
##USERNAME_PASSWORD_PAIRS = [['jodi','fbportfolio']]

#### LOAD CSV FILES AND CREATE DATAFRAME ####
#data0 = pd.read_csv('.../data/messagestimeline.csv')
#data1 = pd.read_csv('.../data/videochattimeline.csv')
#data2 = pd.read_csv('.../data/avgmonthlywordcount.csv')
#data3 = pd.read_csv('.../data/activitybyweekday.csv')
#data4 = pd.read_csv('.../data/mediatotals.csv')

with open(os.path.join("data", "messagestimeline.csv")) as file:
    data0 = pd.read_csv(file)
    
with open(os.path.join("data", "videochattimeline.csv")) as file:
    data1 = pd.read_csv(file)    

with open(os.path.join("data", "avgmonthlywordcount.csv")) as file:
    data2 = pd.read_csv(file)    

with open(os.path.join("data", "activitybyweekday.csv")) as file:
    data3 = pd.read_csv(file)    
    
with open(os.path.join("data", "mediatotals.csv")) as file:
    data4 = pd.read_csv(file)    

#### GROUP DATA FOR GRAPHS ####

#Graph 1: total messages sent per user#
labels = data4['sender_name']
sizes = data4['content']

medialabels = data4.columns[1:]
jodivalues = data4.loc[0, ~data4.columns.isin(['content','sender_name'])]
richardvalues = data4.loc[1, ~data4.columns.isin(['content','sender_name'])]



#### CREATE DASHBOARD USING ####

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])
##auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server

colors = {
    'chartbackground': '#ffffff',
    'background':'#EEF1F6',
    'text': '#000000'
}

piecolours=['#7BA3B7','#6C8FA0','#5C7A89','#4D6672','#3D525B','#2E3D45','1F292E','0F1417']

graph1 = [
    #html.H3("Total Messages Per User",className="text-center"),
    dcc.Graph(
        id='piechart',
        figure={
        'data': [go.Pie(labels=labels, values=sizes,
                        marker={'colors': ['#C0D2D8','#425772']}, textinfo='label')],
        'layout': go.Layout(legend={'x': 1, 'y': 0.7}, 
                            plot_bgcolor = colors['background'], paper_bgcolor = colors['chartbackground'],
                            title='<b>Total Messages Per User</b>')
        }
    ),
]

graph2 = [
   ## html.H3("Timeline of Message Counts",className="text-center"),
    dcc.Graph(
        id='linegraph',
        figure={
            'data': [
                {'x': data0['date'], 'y': data0['jodi_count'], 'type': 'line', 'name': 'Jodi'},
                {'x': data0['date'], 'y': data0['richard_count'], 'type': 'line', 'name': 'Richard'},
            ],
            'layout': {'title': '<b>Timeline of Message Counts</b>',
					    'plot_bgcolor': colors['background'],
					    'paper_bgcolor': colors['chartbackground'],
						'font': {'color': colors['text']},
						 'colorway':['#C0D2D8','#425772']}
        }
    ),
]

graph3 = [
    #html.H3("Average Word Count per Month",className="text-center"),
    dcc.Graph(
        id='bargraph1',
        figure={
            'data': [
                {'x': data2['yearmonth'], 'y': data2['jodi_count'], 'type': 'line', 'name': 'Jodi'},
                {'x': data2['yearmonth'], 'y': data2['richard_count'], 'type': 'line', 'name': 'Richard'},
            ],
            'layout': {'title': '<b>Average Monthly Word Count</b>',
					    'plot_bgcolor': colors['background'],
					    'paper_bgcolor': colors['chartbackground'],
						'font': {'color': colors['text']},
						 'colorway':['#C0D2D8','#425772']}
        }
    ),
]

graph4 = [
    #html.H3("Number of Video Calls per Day",className="text-center"),
    dcc.Graph(
        id='bargraph2',
        figure={
            'data': [
                {'x': data1['date'], 'y': data1['jodi_count'], 'type': 'line', 'name': 'Jodi'},
                {'x': data1['date'], 'y': data1['richard_count'], 'type': 'line', 'name': 'Richard'},
            ],
            'layout': {'title': '<b>Video Calls Per Day</b>',
					    'plot_bgcolor': colors['background'],
					    'paper_bgcolor': colors['chartbackground'],
						'font': {'color': colors['text']},
						 'colorway':['#C0D2D8','#425772']}
        }
    ),
]

graph5 = [
    #html.H3("Jodi's Media Allocation",className="text-center"),
    dcc.Graph(
        id='piechart2',
        figure={
        "data": [go.Pie(labels=medialabels, values=jodivalues,
                        marker={'colors': piecolours}, textinfo='label',
                        hole=.4, hoverinfo="label+percent+name")],
        "layout": go.Layout(
                            legend={"x": 1, "y": 0.7}, 
                            plot_bgcolor = colors['background'], paper_bgcolor = colors['chartbackground'],
                            title="<b>Jodi's Media Allocation</b>")
        }
    )
]

graph6 = [
    #html.H3("Richard's Media Allocation",className="text-center"),
    dcc.Graph(
        id='piechart3',
        figure={
        "data": [go.Pie(labels=medialabels, values=richardvalues,
                        marker={'colors': piecolours}, textinfo='label',
                        hole=.4, hoverinfo="label+percent+name")],
        "layout": go.Layout(
                            legend={"x": 1, "y": 0.7}, 
                            plot_bgcolor = colors['background'], paper_bgcolor = colors['chartbackground'],
                            title="<b>Richard's Media Allocation</b>")
        }
    )
]

graph7 = [
    #html.H3("Activity per Week Day",className="text-center"),
    dcc.Graph(
        id='bargraph3',
        figure={
            'data': [
                {'x': data3['weekday'], 'y': data3['jodi_count'], 'type': 'bar', 'name': 'Jodi'},
                {'x': data3['weekday'], 'y': data3['richard_count'], 'type': 'bar', 'name': 'Richard'},
            ],
            'layout': {'title': '<b>Actvity Per Week</b>',
					    'plot_bgcolor': colors['background'],
					    'paper_bgcolor': colors['chartbackground'],
						'font': {'color': colors['text']},
						 'colorway':['#C0D2D8','#425772']}
        }
    ),
]


body = dbc.Container(
    [   html.H1('Facebook Messenger Dashboard',className="text-center"),
        html.Hr(),
        html.Div("This is dashboard made to visualize some facebook messenger chat history. I thought it would be interesting to see the different kind of information that could be collected and challenge myself to make a dashboard. The layout and style will be refined over time and I will be adding more graphs as I progress!",className="text-center"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(graph1, md=4),
                dbc.Col(graph2, md=8)
            ]
        ),
        dbc.Row(
            [
                dbc.Col(graph3),
                dbc.Col(graph4)
            ]
        ),
        dbc.Row(
            [
                dbc.Col(graph7, md=5),
                dbc.Col(graph5),
                dbc.Col(graph6)
            ]
        ),
        html.H2('Word Cloud',className="text-center"),
        dbc.Row(),
        dbc.Row(
            [
                dbc.Col([html.H5('Jodi',className="text-center"),
                        html.Img(src=app.get_asset_url('jodiwordcloud.png'),style={'height':'90%', 'width':'90%'})
                        ]),
                dbc.Col([html.H5('Richard',className="text-center"),
                        html.Img(src=app.get_asset_url('richardwordcloud.png'),style={'height':'90%', 'width':'90%'}) 
                        ])
            ]            
        )
    ]
    , fluid=True
)


# Setting layout for the application
app.layout = html.Div([body])

# Starting the server
if __name__ == "__main__":
    app.run_server(debug=True)  