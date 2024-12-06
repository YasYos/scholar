import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv('country_wise_latest.csv')

df.rename(columns={
    'Country/Region': 'Country',
    'Confirmed': 'Total Cases',
    'Deaths': 'Total Deaths',
    'Recovered': 'Total Recovered',
    'Active': 'Active Cases',
    'Deaths / 100 Cases': 'Death Rate (%)',
    'Recovered / 100 Cases': 'Recovery Rate (%)',
    'WHO Region': 'Region'
}, inplace=True)


top_cases = df.sort_values('Total Cases', ascending=False).head(10)
bar_top10_death = df.sort_values('Death Rate (%)', ascending=False).head(10)
bar_active = df.groupby('Region')['Active Cases'].sum().reset_index()
total = df[['Total Cases', 'Total Deaths', 'Total Recovered']].sum()
pie_split = pd.DataFrame({
    'Case Type': ['Total Cases', 'Total Deaths', 'Total Recovered'],
    'Count': [total['Total Cases'], total['Total Deaths'], total['Total Recovered']]
})


actual_top10_case = px.bar(
    top_cases,
    x='Country',
    y='Total Cases',
    title='Top 10 Countries by Total Cases'
)

actual_death = px.bar(
    bar_top10_death,
    x='Country',
    y='Death Rate (%)',
    title='Top 10 Countries by Death Rate'
)

actual_active = px.bar(
    bar_active,
    x='Region',
    y='Active Cases',
    title='Active Cases by Region'
)

actual_scatter = px.scatter(
    df,
    x='Recovery Rate (%)',
    y='Death Rate (%)',
    size='Total Cases',
    color='Region',
    hover_name='Country',
    title='Death & Recovery by Country'
)

actual_pie = px.pie(
    pie_split,
    names='Case Type',
    values='Count',
    title='Global Cases'
)

actual_box = px.box(
    df,
    points=False,
    x='Region',
    y='Total Cases',
    title='(Logarithmic) Cases by Region',
    labels={'Region': 'WHO Region', 'Total Cases': 'Total Cases'}
)

actual_box.update_layout(
    yaxis_type="log"
)

app = dash.Dash()

app.layout = html.Div([

    # 3 bars
    html.Div([

        html.Div([
            dcc.Graph(figure=actual_top10_case)
        ], style={'width': '33%', 'display': 'inline-block'}),


        html.Div([
            dcc.Graph(figure=actual_death)
        ], style={'width': '33%', 'display': 'inline-block'}),


        html.Div([
            dcc.Graph(figure=actual_active)
        ], style={'width': '33%', 'display': 'inline-block'})
    ], style={'display': 'flex', 'justifyContent': 'space-between'}),  # Flexbox to align them side by side

    # Scatter & Pie
    html.Div([

        html.Div([
            dcc.Graph(figure=actual_scatter)
        ], style={'width': '50%', 'display': 'inline-block'}),


        html.Div([
            dcc.Graph(figure=actual_pie)
        ], style={'width': '50%', 'display': 'inline-block'})
    ], style={'display': 'flex', 'justifyContent': 'space-between'}),  # Flexbox for the pie chart and scatter plot

    # Box-and-Whiskers
    dcc.Graph(figure=actual_box)
])

app.run_server()
