from streamlit_echarts import st_echarts


def show_gauge(score: int):

    if score >= 80:
        color = "#22C55E"  # Green
    elif score >= 60:
        color = "#F59E0B"  # Orange
    else:
        color = "#EF4444"  # Red

    option = {
        "backgroundColor": "transparent",
        "series": [
            {
                "name": "ATS Score",
                "type": "gauge",
                "center": ["50%", "58%"],
                "radius": "95%",
                "startAngle": 225,
                "endAngle": -45,
                "min": 0,
                "max": 100,
                "splitNumber": 10,
                "progress": {
                    "show": True,
                    "width": 20,
                    "roundCap": True,
                    "itemStyle": {
                        "color": color
                    },
                },
                "axisLine": {
                    "lineStyle": {
                        "width": 20,
                        "color": [[1, "#2D3748"]],
                    }
                },
                "axisTick": {
                    "distance": -25,
                    "splitNumber": 5,
                    "lineStyle": {
                        "width": 2,
                        "color": "#94A3B8"
                    }
                },
                "splitLine": {
                    "distance": -25,
                    "length": 12,
                    "lineStyle": {
                        "width": 3,
                        "color": "#CBD5E1"
                    }
                },
                "axisLabel": {
                    "distance": -45,
                    "color": "#94A3B8",
                    "fontSize": 11,
                },
                "pointer": {
                    "show": True,
                    "length": "70%",
                    "width": 6,
                },
                "anchor": {
                    "show": True,
                    "size": 12,
                    "itemStyle": {
                        "color": color
                    }
                },
                "title": {
                    "show": True,
                    "offsetCenter": [0, "75%"],
                    "fontSize": 20,
                    "color": "#FFFFFF"
                },
                "detail": {
                    "valueAnimation": True,
                    "formatter": "{value}%",
                    "fontSize": 42,
                    "fontWeight": "bold",
                    "color": color,
                    "offsetCenter": [0, "28%"],
                },
                "data": [
                    {
                        "value": score,
                        "name": "ATS Score",
                    }
                ],
            }
        ],
    }

    st_echarts(options=option, height="430px")