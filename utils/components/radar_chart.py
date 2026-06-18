import plotly.graph_objects as go
import streamlit as st


def show_radar_chart(result):

    skills = result["skill_scores"]

    labels = list(skills.keys())
    values = list(skills.values())

    # Close polygon
    labels.append(labels[0])
    values.append(values[0])

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=labels,
            fill="toself",
            name="AI Skill Match",
            line=dict(
                color="#3B82F6",
                width=3
            ),
            fillcolor="rgba(59,130,246,0.35)",
            marker=dict(
                size=8,
                color="#60A5FA"
            ),
        )
    )

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        polar=dict(

            bgcolor="rgba(0,0,0,0)",

            radialaxis=dict(

                visible=True,

                range=[0, 100],

                tickfont=dict(
                    color="#CBD5E1",
                    size=10
                ),

                gridcolor="#334155",

                linecolor="#475569",

                angle=90,
            ),

            angularaxis=dict(

                tickfont=dict(
                    color="#F8FAFC",
                    size=12,
                    family="Segoe UI"
                ),

                gridcolor="#334155",

                linecolor="#475569",
            ),
        ),

        margin=dict(
            l=40,
            r=40,
            t=20,
            b=20,
        ),

        showlegend=False,

        height=500,
    )

    st.subheader("📈 AI Skill Radar")

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        },
    )