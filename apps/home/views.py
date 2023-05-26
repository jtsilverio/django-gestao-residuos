from datetime import datetime, timedelta

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render

from apps.entrada.models import Entrada
from apps.saida.models import Saida


def get_monthly_peso(model, month, year):
    return(int(
        model.objects.filter(data__month=month, data__year=year)
        .aggregate(Sum("peso", default=0))
        .get(
            "peso__sum",
        )
    )) # test for None


def get_current_stats(model):
    current_date = datetime.now()
    previous_date = current_date - timedelta(days=31)

    peso_current_month = get_monthly_peso(model, current_date.month, current_date.year)
    peso_previous_month = get_monthly_peso(model, previous_date.month, previous_date.year)
    
    peso_diff = peso_current_month - peso_previous_month
    trend = "up" if peso_diff > 0 else "down"
    peso_diff_perc = peso_diff / (peso_previous_month + 1) * 100
    
    return {
        f"current_month": peso_current_month,
        f"trend": trend,
        f"diff": round(peso_diff, 2),
        f"diff_perc": round(peso_diff_perc, 2),
        f"range": (previous_date.strftime("%d %B"), current_date.strftime("%d %B")),
    }


def get_balance(entrada_stats, saida_stats):
    return {
        "current_month": entrada_stats["current_month"] - saida_stats["current_month"],
        "trend": entrada_stats["trend"] if entrada_stats["trend"] == saida_stats["trend"] else "down",
        "diff": entrada_stats["diff"] - saida_stats["diff"],
        "diff_perc": entrada_stats["diff_perc"] - saida_stats["diff_perc"],
        "range": entrada_stats["range"],
    }


def home(request):
    entrada_stats = get_current_stats(Entrada)
    saida_stats = get_current_stats(Saida)
    saldo = get_balance(entrada_stats, saida_stats)

    context = {
        "object_list": {
            "entrada": entrada_stats,
            "saida": saida_stats,
            "saldo": saldo,
        }
    }

    return render(request, "home/home.html", context)
