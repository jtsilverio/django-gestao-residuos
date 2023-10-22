from datetime import datetime
from itertools import groupby
from operator import itemgetter

import plotly.graph_objects as go
from django.shortcuts import render

from apps.home.models import ResumoMensalResiduos


def get_mothly_data(year: int):
    monthly_data = list(ResumoMensalResiduos.objects.filter(ano=year).values())
    return monthly_data


# def get_dashboard_stats(monthly_data):
#     current_month = datetime.now().month
#     dashboard_stats = {}
#     for tipo_dado in ["entrada", "saida"]:
#         current_month_peso = sum(
#             v["peso"]
#             for v in monthly_data.values()
#             if v["mes"] == current_month and v["tipo"] == tipo_dado
#         )

#         last_month_peso = sum(
#             v["peso"]
#             for v in monthly_data.values()
#             if v["mes"] == current_month - 1 and v["tipo"] == tipo_dado
#         )

#         diff = current_month_peso - last_month_peso
#         diff_perc = (
#             100 * (diff / last_month_peso)
#             if last_month_peso
#             else (9999 if current_month_peso else 0)
#         )
#         diff_perc = int(diff_perc)

#         trend = "up" if last_month_peso <= current_month_peso else "down"

#         dashboard_stats[tipo_dado] = {
#             "current_month_peso": current_month_peso,
#             "diff": diff,
#             "diff_perc": diff_perc,
#             "trend": trend,
#         }

#     dashboard_stats["saldo"] = {
#         "current_month_peso": dashboard_stats["entrada"]["current_month_peso"]
#         - dashboard_stats["saida"]["current_month_peso"],
#         "diff": dashboard_stats["entrada"]["diff"] - dashboard_stats["saida"]["diff"],
#         "diff_perc": dashboard_stats["entrada"]["diff_perc"]
#         - dashboard_stats["saida"]["diff_perc"],
#         "trend": "up"
#         if dashboard_stats["entrada"]["current_month_peso"]
#         >= dashboard_stats["saida"]["current_month_peso"]
#         else "down",
#     }

#     return dashboard_stats


def monthly_lineplot(monthly_data):
    monthly_data.sort(key=itemgetter("tipo", "ano", "mes"))

    result = []
    for key, group in groupby(monthly_data, key=itemgetter("tipo", "ano", "mes")):
        result.append(
            {
                "tipo": key[0],
                "ano": key[1],
                "mes": key[2],
                "peso": sum(item["peso"] for item in group),
            }
        )

    # Create traces
    trace_entrada = go.Scatter(
        x=[d["mes"] for d in result if d["tipo"] == "entrada"],
        y=[d["peso"] for d in result if d["tipo"] == "entrada"],
        mode="markers+lines",
        name="entrada",
        line=dict(color="#31316A", shape="spline", width=5),
        marker=dict(size=9),
    )

    trace_saida = go.Scatter(
        x=[d["mes"] for d in result if d["tipo"] == "saida"],
        y=[d["peso"] for d in result if d["tipo"] == "saida"],
        mode="markers+lines",
        name="saida",
        line=dict(color="#F3C78D", shape="spline", width=5),
        marker=dict(size=9),
    )

    # Create layout
    layout = go.Layout(
        template="plotly_white",
        xaxis=dict(type="category"),
        margin=dict(l=5, r=5, t=5, b=5),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title=None,
        ),
        plot_bgcolor="rgba(255, 255, 255, 0)",
        paper_bgcolor="rgba(255, 255, 255, 0)",
        hovermode="x unified",
    )
    fig = go.Figure(data=[trace_entrada, trace_saida], layout=layout)
    config = {"displayModeBar": False}

    return fig.to_html(
        full_html=False,
        default_height=350,
        div_id="line-plot",
        config=config,
    )


def home(request):
    current_date = datetime.now()
    monthly_data = get_mothly_data(current_date.year)
    # dashboard_stats = get_dashboard_stats(monthly_data)
    plot = monthly_lineplot(monthly_data)

    context = {
        # "stats_dict": dashboard_stats,
        "plot": plot,
    }

    return render(request, "home/home.html", context)
