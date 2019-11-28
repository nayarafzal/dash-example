import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

# Dataset Processing

df_emissions = pd.read_csv('emission_full.csv')

df_emission_0 = df_emissions.loc[df_emissions['year']==2000]

# Building our Graphs

data_choropleth = dict(type='choropleth',
                       locations=df_emission_0['iso-a3'],  #There are three ways to 'merge' your data with the data pre embedded in the map
                       #locationmode=[]
                       z=np.log(df_emission_0['CO2_emissions']),
                       text=df_emission_0['country_name'],
                       colorscale='inferno'
                      )

layout_choropleth = dict(geo=dict(scope='world',  #default
                                  projection=dict(type='azimuthal equal area'
                                                 ),
                                  #showland=True,   # default = True
                                  landcolor='black',
                                  lakecolor='white',
                                  showocean=True,   # default = False
                                  oceancolor='azure'
                                 ),
                         
                         title=dict(text='World Choropleth Map',
                                    x=.5 # Title relative position according to the xaxis, range (0,1)
                                   )
                        )

fig = go.Figure(data=data_choropleth, layout=layout_choropleth)

# The App itself

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div(children=[
    html.H1(children='My First DashBoard'),

    html.Div(children='''
        Example of html Container
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
