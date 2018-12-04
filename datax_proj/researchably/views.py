# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import table_query
import pandas as pd

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = table_query(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            print("Valid")
            # redirect to a new URL:
            return HttpResponseRedirect('/researchably/output/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = table_query()

    context = {
        'form': form
    }
    return render(request, 'tables_home.html',context)


def output_page(request):
    # Get data passed in by form
    form = table_query(request.POST)
    index_val = form['paper_index'].value()
    index_val = int(index_val)

    # Read in data and extract the line wanted
    file_name = 'happy.csv'
    df = pd.read_csv(file_name)
    data_requested = df[df.pmid.isin([index_val])]
    url_add = "https://www.ncbi.nlm.nih.gov/pubmed/?term="
    # Pass in to web page
    context = {
        "index_val": index_val,
        "form":form,
        'title' : data_requested['title'].values[0],
        'authors' : data_requested['authors'].values[0],
        'url' : url_add + str(index_val),
        'summarization' : data_requested['summarization'].values[0],
        'article_type' : data_requested['article type'].values[0],
        'study_design' : data_requested['study design'].values[0]
    }
    return render(request, 'tables_output.html', context)
