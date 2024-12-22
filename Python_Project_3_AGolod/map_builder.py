from typing import List, Dict, Any
import plotly.graph_objs as go

def generate_map_chart(points_data: List[Dict[str, Any]]) -> go.Figure:
    figure = go.Figure(go.Scattermapbox(
        lat=[entry["lat"] for entry in points_data],
        lon=[entry["lon"] for entry in points_data],
        mode="markers",
        marker=go.scattermapbox.Marker(
            size=13,
            color="rgb(255, 0, 0)"
        ),
        text=[entry["name"] for entry in points_data],
        hoverinfo="text"
    ))

    figure.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=2.8,
        mapbox_center={"lat": 55.0, "lon": 35.0},
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        height=520,
        paper_bgcolor="#F1F8E9"
    )
    return figure
