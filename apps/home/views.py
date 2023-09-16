from datetime import datetime, timedelta

import pandas as pd
import plotly.express as px
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render

from apps.home.models import EntradaMensal, SaidaMensal


def get_mothly_dataframe(
    year: int,
):
    entrada_stats = EntradaMensal.objects.filter(ano=year).all()
    entrada_stats = pd.DataFrame(list(entrada_stats.values()))
    entrada_stats = entrada_stats.assign(tipo="entrada")

    saida_stats = SaidaMensal.objects.filter(ano=year).all()
    saida_stats = pd.DataFrame(list(saida_stats.values()))
    saida_stats = saida_stats.assign(tipo="saida")

    monthly_dataframe = pd.concat([entrada_stats, saida_stats])
    monthly_dataframe["mes"] = monthly_dataframe["mes"].astype("category")
    return monthly_dataframe


def get_dashboard_stats(monthly_dataframe):
    current_date = datetime.now()

    dashboard_stats = {}
    for tipo_dado in ["entrada", "saida"]:
        current_month_peso = monthly_dataframe.loc[
            (monthly_dataframe["mes"] == current_date.month)
            & (monthly_dataframe["tipo"] == tipo_dado),
            "peso",
        ].sum()
        current_month_peso = round(float(current_month_peso), 2)

        last_month_peso = monthly_dataframe.loc[
            (monthly_dataframe["mes"] == current_date.month - 1)
            & (monthly_dataframe["tipo"] == tipo_dado),
            "peso",
        ].sum()
        last_month_peso = round(float(last_month_peso), 2)

        diff = round(current_month_peso - last_month_peso, 2)
        diff_perc = diff / (last_month_peso + 1) * 100
        # convert to int
        diff_perc = int(diff_perc)
        trend = "up" if diff > 0 else "down"

        dashboard_stats[tipo_dado] = {
            "current_month_peso": current_month_peso,
            "diff": abs(diff),
            "diff_perc": abs(diff_perc),
            "trend": trend,
        }

    dashboard_stats["saldo"] = {
        "current_month_peso": dashboard_stats["entrada"]["current_month_peso"] - dashboard_stats["saida"]["current_month_peso"],
    }

    return dashboard_stats


def monthly_lineplot(dataframe):
    agg_dataframe_by_month = (
        dataframe.groupby(["mes", "tipo"]).agg({"peso": "sum"}).reset_index()
    )

    plot = px.line(
        agg_dataframe_by_month,
        x="mes",
        y="peso",
        color="tipo",
        labels={"peso": "Peso (kg)", "mes": "Mês", "ano": "Ano"},
        markers=True,
        template="plotly_white",
        line_shape="spline",
        color_discrete_map={
            "entrada": "#31316A",
            "saida": "#F3C78D",
        },
        
    )
    plot.update_xaxes(type="category")
    plot.update_traces(line=dict(width=5),
                       marker=dict(size=9),
                       hovertemplate=None)
    plot.update_layout(
        margin=dict(l=5, r=5, t=5, b=5),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            title=None,
        ),
        plot_bgcolor= "rgba(0, 0, 0, 0)",
        paper_bgcolor= "rgba(0, 0, 0, 0)",
        hovermode="x unified",
    )
    config = {"displayModeBar": False}

    return plot.to_html(
        full_html=False,
        default_height=350,
        div_id="line-plot",
        config=config,
    )


def home(request):
    current_date = datetime.now()
    monthly_dataframe = get_mothly_dataframe(current_date.year)

    dashboard_stats = get_dashboard_stats(monthly_dataframe)
    plot = monthly_lineplot(monthly_dataframe)

    context = {
        "stats_dict": dashboard_stats,
        "plot": plot,
    }

    return render(request, "home/home.html", context)
