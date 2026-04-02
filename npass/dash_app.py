from django_plotly_dash import DjangoDash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import requests

app = DjangoDash("thesis_dashboard")

app.layout = html.Div([
    html.H2("Cybersickness Prediction (Thesis)"),

    dcc.Dropdown(
        id="gender",
        options=[
            {"label": "Male", "value": 1},
            {"label": "Female", "value": 0}
        ],
        placeholder="Select Gender"
    ),

    dcc.Input(
        id="gad_score",
        type="number",
        placeholder="Enter GAD Score"
    ),

    dcc.Dropdown(
        id="task_condition",
        options=[
            {"label": "Control", "value": "control"},
            {"label": "0-back", "value": "0-back"},
            {"label": "2-back", "value": "2-back"}
        ],
        placeholder="Select Task Condition"
    ),

    html.Button("Predict", id="predict_btn"),

    html.Div(id="prediction_output")
])
@app.callback(
    Output("prediction_output", "children"),
    Input("predict_btn", "n_clicks"),
    State("gender", "value"),
    State("gad_score", "value"),
    State("task_condition", "value"),
)
def predict_cybersickness(n_clicks, gender, gad_score, task_condition):

    if not n_clicks:
        return ""

    data = {
        "gender": gender,
        "gad_score": gad_score,
        "task_condition": task_condition
    }

    r = requests.post(
        "http://127.0.0.1:8000/dash/app/thesis_dashboard/",
        json=data
    )

    prediction = r.json()["prediction"]

    return f"Prediction: {prediction}"