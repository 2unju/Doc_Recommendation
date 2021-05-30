import psycopg2
import pandas as pd

from django.shortcuts import render, redirect

from . import recommend, init, database

def main(request):
    init.main()
    return redirect('page/1')

def index(request, _page):
    q = request.GET.get('q', '')
    if q:
        docs_df = database.GetDF()
        docs_list = recommend.SearchDoc(docs_df, q)
    else:
        sign_info = "host='localhost' dbname ='docdb' user='postgres' password='tlqejr1010'"
        sign = psycopg2.connect(sign_info)
        cursor = sign.cursor()
        fnum = _page * 20
        snum = (_page - 1) * 20
        sql = "SELECT * FROM doclist WHERE id < '{}' AND id >= '{}'".format(fnum, snum)
        cursor.execute(sql)
        docs_list = cursor.fetchall()
        cursor.close()
        sign.close()
    return render(request, 'DocList/index.html', {
        'docs_list':
            docs_list,
        'previous':
            _page-1,
        'next':
            _page+1
    })

def docs(request, _id):
    sign_info = "host='localhost' dbname ='docdb' user='postgres' password='tlqejr1010'"
    sign = psycopg2.connect(sign_info)
    cursor = sign.cursor()

    sql = "SELECT title, url, content FROM doclist WHERE id = '{}'".format(_id)
    cursor.execute(sql)
    doc = cursor.fetchone()
    cursor.close()
    sign.close()
    page = _id // 20 + 1

    docs_df = database.GetDF()
    related, frequency = recommend.Top10_Docs(docs_df, _id)
    return render(request, 'DocList/docs.html', {
        'doc':
            doc,
        'page':
            page,
        'related':
            related,
        'frequency':
            frequency[:10]
    })