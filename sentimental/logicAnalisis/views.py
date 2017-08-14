# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
import urllib2
import json
import collections
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from logicAnalisis.models import word, user_facebook, likes, message,commentsClassified, page

# me 10153624026919284

data = ''
token = 'access_token=1604127026532208|NWabzRV4yFtpxh5Nv9AXh9g0aCI'
post_limit = '2'
id_page = ''

pages = {
    "pages": [
        {"name": "pagina1", "id": "123123123"},
        {"name": "pagina2", "id": "12989980"}
        ]
    }

stopWrd = [
    'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por',
    'un', 'para', 'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'pero', 'sus',
    'le', 'ya', 'o', 'este', 'síxad', 'porque', 'esta', 'entre', 'cuando',
    'muy', 'sin', 'sobre', 'también', 'me', 'hasta', 'hay', 'donde', 'quien',
    'desde', 'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra',
    'otros', 'ese', 'eso', 'ante', 'ellos', 'e', 'esto', 'antes', 'algunos',
    'quién', 'unos', 'yo', 'otro', 'otras', 'otra', 'tanto', 'esa', 'estos',
    'mucho', 'quienes', 'nada', 'muchos', 'cual', 'poco', 'ella', 'estar',
    'estas', 'algunas', 'algo', 'nosotros', 'mi', 'mis', 'tíxba', 'te', 'ti',
    'tu', 'tus', 'ellas', 'nosotras', 'vosostros', 'vosostras', 'os', 'míxado',
    'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos', 'suyas',
    'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro', 'vuestra',
    'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estábamos', 'estamos',
    'estemos', 'estaremos', 'estaba', 'estabas', 'estabais', 'estaban',
    'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 'estuvieron',
    'estuviera', 'estuvieras', 'estuviéramos', 'estuvierais', 'estuvieran',
    'estuviese', 'estuvieses', 'estuviésemos', 'estuviesemos', 'estuvieseis',
    'estuviesen', 'estando', 'estado', 'estada', 'estados', 'estadas', 'estad',
    'he', 'has', 'ha', 'hemos', 'han', 'haya', 'hayas', 'hayamos', 'hayan',
    'habrían', 'habríamos', 'habremos', 'hube', 'hubiste', 'hubo', 'hubimos',
    'hubisteis', 'hubieron', 'hubiera', 'hubieras', 'hubíxaramos', 'hubierais',
    'hubieran', 'hubiese', 'hubieses', 'hubíxasemos', 'hubieseis', 'hubiesen',
    'habiendo', 'habido', 'habida', 'habidos', 'habidas', 'soy', 'eres', 'es',
    'somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'seá1is', 'sean',
    'serías', 'seremos', 'serían', 'era', 'eras', 'erais', 'eran', 'fui',
    'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera', 'fueras',
    'fuéramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuésemos', 'fueseis',
    'fuesen', 'sintiendo', 'sentido', 'sentida', 'sentidos', 'sentidas',
    'siente', 'sentid', 'tengo', 'tienes', 'tiene', 'tenemos', 'tenéis',
    'tienen', 'tenga', 'tengas', 'tengamos', 'tengáis', 'tengan', 'tendrían',
    'tendrías', 'tendría', 'tendremos', 'tendrán', 'tendríxadas',
    'tendríxadamos', 'tendríxadais', 'tendríxadan', 'teníxada', 'teníxadas',
    'teníxadamos', 'teníxadais', 'teníxadan', 'tuve', 'tuviste', 'tuvo',
    'tuvimos', 'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuvíxaramos',
    'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuvíxa9semos',
    'tuvieseis', 'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos',
    'tenidas', 'tened']


def index(request):
    # el id de la pagina debe ser enviado por get

    print " "
    print "Cargando..."
    print "Procesando palabras, por favor espere"

    id_page =  getFirstPage()

    data = facebook_posts(id_page)
    # alterWordsInDBWithStemmWords()


    dictResponse = {}
    res = []

    # Recorrer cada post
    for post in data["data"]:
        # Recorrer cada comentario
        for comm in post["comments"]["data"]:
            # Guardar usuario
            cur_usr = comm['from']['id']
            infoUsr = facebook_infoUser(cur_usr)
            saveUsr(infoUsr)

            # Guardar los likes de un usuario
            saveLikes(cur_usr, facebook_likesUser(cur_usr))

            # ------ Procesamiento de textos, para clasificacion --------

            words = []
            # arreglo para filtrar las palabras utiles para la clasificación
            words = comm["message"].split(' ')

            # eliminar stop words
            words = deleteStopWords(words)
            # Guardar en la base de datos las palabras desconocidas
            saveWordsUnknown(words)
            # convertir en raiz gramatical
            words = convertListInListOfStemWords(words)
            # Obtener la clasificación por palabras
            dictResponse = getWordsClassified(words)
            # Obtener una clasificación general
            classify = classifyGeneralComment(dictResponse)
            # Retorna cual fue la clasificación mayor
            stringClassify = getStringOfMaxPolarity(classify)

            print words
            print dictResponse
            print classify

            print " "
            print " "

            # Guardar comentario
            idCommSaved = saveComment(
                comm['like_count'],
                comm["message"], cur_usr)

            # Guardar en clasificador
            saveClassifyOfComment(
                idCommSaved,
                comm["message"],
                id_page,
                stringClassify)

            # Armar el JSON para devolver al front-end
            responseForCurrentComment = {}
            responseForCurrentComment["message"] = comm["message"].encode('utf-8')
            responseForCurrentComment["polarity"] = classify
            responseForCurrentComment["wordsClassified"] = dictResponse

            res.append(responseForCurrentComment)

    template = loader.get_template('logicAnalisis/index.html')
    context = RequestContext(request, res)
    return render(request, 'logicAnalisis/index.html', {'datos': res})


def getListOfRestaurants(request):
    template = loader.get_template('logicAnalisis/index.html')
    context = RequestContext(request, pages)
    return HttpResponse(template.render(context))


def facebook_posts(id_page):
    URL_PAGE = 'https://graph.facebook.com/'+id_page+'/posts?limit='+post_limit+'&'+token

    obj = urllib2.urlopen(URL_PAGE)
    dat = json.load(obj)
    return dat


def facebook_infoUser(idUser):
    URL_PAGE = 'https://graph.facebook.com/'+idUser+'?fields=id,gender,about,email,location,religion'+"&"+token

    obj = urllib2.urlopen(URL_PAGE)
    dat = json.load(obj)
    return dat


def facebook_likesUser(idUser):
    URL_PAGE = 'https://graph.facebook.com/'+idUser+'/likes'+"?"+token
    # print URL_PAGE
    obj = urllib2.urlopen(URL_PAGE)
    dat = json.load(obj)
    return dat


def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data


def stemWord(word):
        stemmer = SnowballStemmer("spanish")
        return stemmer.stem(word)


def convertListInListOfStemWords(datos):
    response = []
    for dat in datos:
        response.append(stemWord(dat))

    return response


def deleteStopWords(datos):
    setStopWords = set(stopWrd)
    setDatos = set(datos)

    return list(set(setDatos) - set(setStopWords))


def getWordsClassified(datos):
    response = {}
    for wrd in datos:
        response[wrd] = searchWordClassifyInDB(wrd)

    return response


def searchWordClassifyInDB(wrd):
    responseDB = word.objects.filter(gram_root=wrd)
    if responseDB.count() == 1:
        return (responseDB[0].polarity).encode('utf-8')
    else:
        return "none"


def alterWordsInDBWithStemmWords():
    words = word.objects.all()
    for wrd in words:
        newName = stemWord(wrd.name)
        word.objects.filter(name=wrd.name).update(gram_root=newName)


def classifyGeneralComment(wordsClassified):
    countOfPositive = 0
    countOfNegative = 0
    countOfNeutral = 0

    countOfWords = len(wordsClassified.keys())

    for wrd in wordsClassified:
        if wordsClassified[wrd] == 'PO':
            countOfPositive += 1
        elif wordsClassified[wrd] == 'NE':
            countOfNegative += 1
        elif wordsClassified[wrd] == 'NT':
            countOfNeutral += 1

    response = {}
    response['Positive'] = (float(countOfPositive)/countOfWords)
    response['Negative'] = (float(countOfNegative)/countOfWords)
    response['Neutral'] = (float(countOfNeutral)/countOfWords)

    return response


def getStringOfMaxPolarity(data):
    positive = data['Positive']
    negative = data['Negative']
    neutral = data['Neutral']

    if positive > negative and positive > neutral:
        return 'PO'
    elif negative > positive and negative > neutral:
        return 'NE'
    else:
        return 'NT'


def saveWord(name, polarity, root):
    count_word = word.objects.filter(gram_root=root).count()
    if count_word == 0:
        obj = word(name=name, polarity=polarity, gram_root=root)
        obj.save()


def saveWordsUnknown(listOfWords):
    for wrd in listOfWords:
        if searchWordClassifyInDB(wrd) == 'none':
            saveWord(wrd, 'NN', stemWord(wrd))


def saveUsr(infoUser):
    data = normalizeInfoUsr(infoUser)
    responseDB = user_facebook.objects.filter(id_user=data['id_user']).count()
    gender = data['sex']
    genderR = ''
    if gender == 'male':
        genderR = 'M'
    else:
        genderR = 'F'

    if responseDB == 0:
        obj = user_facebook(
            id_user=data['id_user'],
            email=data['email'],
            sex=genderR,
            about_me=data['about_me'],
            city=data['city'],
            religion=data['religion'])
        obj.save()


def normalizeInfoUsr(infoUser):
    data = {}
    data["id_user"] = infoUser['id']

    if 'email' in infoUser.keys():
        data["email"] = infoUser['email']
    else:
        data["email"] = ''

    if 'gender' in infoUser.keys():
        data["sex"] = infoUser['gender']
    else:
        data["sex"] = ''

    if 'about' in infoUser.keys():
        data['about_me'] = infoUser['about']
    else:
        data['about_me'] = ''

    if 'location' in infoUser.keys():
        data['city'] = infoUser['location']['name']
    else:
        data['city'] = ''

    if 'religion' in infoUser.keys():
        data['religion'] = infoUser['religion']
    else:
        data['religion'] = ''

    return data


def saveLikes(usr, likes_usr):
    # print likes_usr['data'][0]['name']

    for li in likes_usr["data"]:
        if len(li.keys()) > 0:
            print li['name'].encode('utf-8')
            page_name = li['name'].encode('utf-8')
            cur_usr = user_facebook.objects.filter(id_user=usr)
            filterargs = {'page_name': page_name, 'from_id': usr}

            cur_likes = likes.objects.filter(**filterargs).count()

            if cur_likes == 0:
                obj = likes(page_name=page_name, from_id=cur_usr[0])
                obj.save()


def saveComment(countLikes, text, idUsr):
    comments = message.objects.filter(text=text)

    if comments.count() == 0:
        user = user_facebook.objects.filter(id_user=idUsr)

        obj = message(from_id=user[0], count_likes=countLikes, text=text)
        obj.save()
        return obj.id
    else:
        return comments[0].id


def saveClassifyOfComment(idComm, text, idPag, autoClass):
    comment = message.objects.filter(id=idComm)
    commentClass = commentsClassified.objects.filter(from_message_id=idComm)

    if comment.count() == 1 and commentClass.count() == 0:
        obj = commentsClassified(
            from_message_id=comment[0],
            auto_classification=autoClass,
            user_classification='NN',
            text=text,
            id_page=idPag)
        obj.save()


def getFirstPage():
	idPages = page.objects.all()
	return idPages[0].id_page
	
    # print convert(data)
    # for dat in data:
    #   # dictEncode[str(dat)] = str(data[dat])
    #   # print dat.encode('utf-8')

    #   if isinstance(data[dat], dict):
    #       dictIntern = {}
    #       for dat2 in data[dat]:
    #           # print str(((data[dat])[dat2])).encode('utf-8')
    #           dictIntern[dat2.encode('utf-8')] = 'hola'
    #           dictIntern[dat2.encode('utf-8')] = str(((data[dat])[dat2])).encode('utf-8')
    #           dictEncode[dat.encode('utf-8')] = dictIntern
    #   elif isinstance(data[dat], bool):
    #       dictEncode[dat.encode('utf-8')] = data[dat]
    #   elif isinstance(data[dat],  (int, long, float, complex)):
    #       dictEncode[dat.encode('utf-8')] = data[dat]
    #   else:
    #       # dictEncode[dat.encode('utf-8')] = str(data[dat])
    #       dictEncode[dat.encode('utf-8')] = data[dat].encode('utf-8')
