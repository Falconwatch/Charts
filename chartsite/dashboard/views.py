from django.http import HttpResponse
from django.shortcuts import render
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import pandas as pd
import random
from .misc import  gauge
import numpy as np

from .models import report_counts

def index(request):
    counts_list = report_counts.objects.all()
    context = {'counts_list': counts_list}
    return render(request, 'dashboard/index.html', context)

def counts_board(request):
    context = {}
    #Численность здоровых
    healthy_plot_script, healthy_plot_div = plot_healthy_count();
    context['healthy_plot_script'] = healthy_plot_script
    context['healthy_plot_div'] = healthy_plot_div

    # DR

    return render(request, 'dashboard/counts.html', context)

def risk(request):
    context ={}
    #уровень риска портфеля
    risk_gauge_script, risk_gauge_div = components(gauge(0.2))
    context['risk_gauge_script'] = risk_gauge_script
    context['risk_gauge_div'] = risk_gauge_div

    return render(request, 'dashboard/risk.html', context)


#########################################################################
##
##########################################################################

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def plot_default_share():
    fetched_report_counts = report_counts.objects.all()
    fetched_counts = pd.DataFrame(list(fetched_report_counts.values()))

    #Доля дефолтов
    #график

def plot_risk_gauge():
    risk_gauge = gauge(0.2)
    return components(risk_gauge)

def plot_healthy_count(width = 900, height = 500):
    # извлекаем данные по численностям
    fetched_report_counts = report_counts.objects.all()
    fetched_counts = pd.DataFrame(list(fetched_report_counts.values()))

    # численность здоровых
    grouped_healhty = fetched_counts.groupby(by=['report_date', 'product_type'])[['healthy']].sum()
    healhty_dynamics = grouped_healhty.unstack()
    healhty_dynamics.columns = healhty_dynamics.columns.droplevel()
    healhty_dynamics['Все вместе'] = healhty_dynamics.sum(axis=1)

    # график численности здоровых
    healthy_plot = figure(plot_width=width, plot_height=height, title='Численность "здоровых" договоров',
                          x_axis_type="datetime")
    healthy_plot_colors = [random_color() for c in range(fetched_counts.shape[1])]
    for i in range(len(healhty_dynamics.columns)):
        ctype = healhty_dynamics.columns[i]
        col = healthy_plot_colors[i]
        _y = healhty_dynamics[ctype].values
        _x = [v for v in healhty_dynamics.index.values]
        healthy_plot.line(y=_y, x=healhty_dynamics.index.values, legend_label=ctype, color=col)

    healthy_plot.legend.location = "top_left"
    healthy_plot.legend.click_policy = "hide"
    return components(healthy_plot)