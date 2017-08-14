# -*- coding: utf-8 -*-

# from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from logicAnalisis.views import *
from logicAnalisis.models import word

from .models import Twacount, Twcomment
from .scrapyWR import *

import json


def index(request):
    # savenegatives()
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def analisis(request):
    if request.method == 'POST':
        jsonfile = json.load(request.FILES['myfile'])
        data = {}
        # get query from json
        query = jsonfile['search_metadata']["query"]
        data['query'] = query
        data['object_list'] = []
        # get coments
        for tweet in jsonfile['statuses']:
            # user data
            acount = tweet['user']['screen_name']
            des = tweet['user']['description']
            loc = tweet['user']['location']
            fcoun = tweet['user']['friends_count']
            focoun = tweet['user']['followers_count']
            saveAcount(acount, des, loc, fcoun, focoun)
            # tweet data
            tid = tweet['id']
            ttext = tweet['text']
            tret = tweet['retweeted']
            trcou = tweet['retweet_count']
            tat = tweet['created_at']
            words = []
            words = ttext.split(' ')
            words = deleteStopWords(words)
            saveWordsUnknown(words)
            words = convertListInListOfStemWords(words)
            response = getWordsClassified(words)
            dictPolarity = classifyGeneralComment(response)
            tpo = dictPolarity['Positive']
            tne = dictPolarity['Negative']
            tnt = dictPolarity['Neutral']
            saveComment(
                tid, acount,
                ttext,
                trcou, tret,
                tat,
                tne, tpo, tnt,
                query
                )
            data['object_list'].append({
                'polarity': getStringOfMaxPolarity(dictPolarity),
                'user': '@'+acount,
                'text': ttext
            })

        template = loader.get_template('detail.html')
        context = RequestContext(request, data)
        return HttpResponse(template.render(context))


def saveAcount(tacount, descript, locat, fricount, folcount):
    dbasck = Twacount.objects.filter(acount=tacount).count()
    if dbasck == 0:
        obj = Twacount(
            acount=tacount,
            description=descript,
            location=locat,
            friends_count=fricount,
            followers_count=folcount
            )
        obj.save()


def saveComment(idcomment, tacount, text, rcount, retw, at, ne, po, nt, qry):
    dbasck = Twcomment.objects.filter(Twid=idcomment).count()
    if dbasck == 0:
        obj = Twcomment(
            Twid=idcomment,
            acount=Twacount.objects.get(acount=tacount),
            comment=text,
            retweet_count=rcount,
            retweeted=retw,
            created_at=at,
            negative=ne,
            positive=po,
            neutral=nt,
            query=qry
            )
        obj.save()


def printwords(pol):
    words = word.objects.filter(polarity=pol)
    items = []
    for obj in words:
        items.append(obj.name)
    print items
