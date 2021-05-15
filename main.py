#!C:\Users\Quentin\AppData\Local\Microsoft\WindowsApps\python.exe
# -*- coding: utf-8 -*-
from imdb import IMDb
import tkinter as tk
from tkinter import ttk
from textblob import TextBlob
from urllib.request import urlopen

global Version
Version = "1.0"

root = tk.Tk()
root.geometry('900x850')
ia = IMDb()
tk.Label(root, text='FILMS').pack()
area = ['Titre', 'Année', 'Durée', 'Note', 'Status']
ac = ['Titre', 'Année', 'Durée', 'Note', 'Status']
global ifilms
ifilms=0

#fait un tableau des films de filename
def extractMovies(filename):
    l = open(filename, "r", encoding='utf-8')
    lignes = l.readlines()
    tabMovies = []
    for ligne in lignes:
        lig = ligne.strip()
        lMovie = lig.split('\t')  # permet d'obtenir une liste à partir d'un str séparé par des tabs
        tabMovies.append(lMovie)
    l.close()
    return (tabMovies)

def tri_fichier(filename):
    l = open(filename, 'r', encoding='utf-8')
    lines = sorted(l.readlines())
    l.close()
    k = open(filename, 'w', encoding='utf-8')
    for line in lines:
        k.write(line)
    k.close()

#renvoie une liste des différentes caractéristiques d'un film dont le nom est fourni
def get_movie_infos(name, i):
    search = ia.search_movie(name)
    number = len(search)
    id = search[i].movieID
    movie = ia.get_movie(id, info=['main', 'taglines', 'plot'])
    title = movie.get('localized title')
    year = movie.get('year')
    runtimes0 = movie.get('runtimes')
    if runtimes0 is None:
        runtimes = 0
    else:
        runtimes = runtimes0
    genre = movie.get('genre')
    resume0 = movie.get('plot')
    if resume0 is None:
        resume = ""
    else:
        resume0 = resume0[0]
        resume = str(resume0)
        resume = resume.split('::')
        resume = resume[0]
        blob = TextBlob(resume)
        resume = blob.translate(to='fr')
    nbcast = movie.get('cast')
    if nbcast is None:
        cast = ''
    elif len(nbcast) == 0:
        cast = ''
    elif len(nbcast) == 1:
        cast0 = movie.get('cast')[0]
        cast = str(cast0)
    elif len(nbcast) == 2:
        cast0 = movie.get('cast')[0]
        cast1 = movie.get('cast')[1]
        cast = str(cast0) +", "+str(cast1)
    else :
        cast0 = movie.get('cast')[0]
        cast1 = movie.get('cast')[1]
        cast2 = movie.get('cast')[2]
        cast = str(cast0) + ", " + str(cast1) + ", " + str(cast2)
    real0 = movie.get('directors')
    if real0 is None:
        real = ""
    else:
        real = real0[0]
    note0 = movie.get('rating')
    if note0 == None:
        note = 0
    else:
        note = note0
    id = movie.get('imdbID')
    taglines = movie.get('taglines')
    if taglines is None:
        tagline = ""
    else :
        tagline = taglines[0]
    kind = movie.get('kind')
    haut = [title, year, runtimes, genre, note, resume, cast, real, id, tagline, kind, number]
    return(haut)


#sort la ligne correspondant à un film dans filename
def selectline(filename, movie):
    l = open(filename, "r", encoding='utf-8')
    lignes = l.readlines()
    tabMovies = []
    for ligne in lignes:
        tabMovies = ligne.split('\t')
        movieline = tabMovies[0]
        if movieline != movie:
            continue
        else:
            break
    l.close()
    return (tabMovies)

def write_full(filename, list):
    l = open(filename, 'a', encoding='utf-8')
    ligne = list[0] + '\t' + list[1] + '\t' + list[2] + '\t' + list[5] + '\t' + list[3] + '\t' + list[6] + '\t' + list[7] + '\t' + list[8] + '\t' + list[9] + '\t' + list[10] + '\t' + list[11] + '\t' + list[4] + '\n'
    l.write(ligne)
    l.close()


#traduit l'hexadecimal en nombre décimal
def tradHexa(strHex):
    nb = 0
    x = strHex[2]
    y = strHex[3]
    dico = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
    if x not in ('A','B','C','D','E','F'):
        x = int(x)
    else:
        x = dico[x]
    if y not in ('A','B','C','D','E','F'):
        y = int(y)
    else:
        y = dico[y]
    nb = x * 16 + y - 1
    return(nb)


#supprime la ligne numéro line dans le fichier filename
def deleteline(filename, recherche):
    l = open(filename, "r", encoding='utf-8')
    lines = l.readlines()
    l.close()
    k = open(filename, "w", encoding='utf-8')
    for line in lines:
        tmp = line.split('\t')
        nom = tmp[0]
        if nom != recherche:
            k.write(line)
    k.close()


#trie la colonne sélectionnée
def treeview_sort_column(tv, col, reverse):
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    l.sort(reverse=reverse)
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
    # reverse sort next time
    tv.heading(col, command=lambda: \
        treeview_sort_column(tv, col, not reverse))

def length_span(filename, min, max):
    l = open(filename, 'r', encoding='utf-8')
    lignes = l.readlines()
    tabMoviesFiltered = []
    for ligne in lignes:
        lig = ligne.strip()
        lMovie = lig.split('\t')  # permet d'obtenir une liste à partir d'un str séparé par des tabs
        if max >= int(lMovie[2]) >= min:
            tabMoviesFiltered.append(lMovie)
    l.close()
    return(tabMoviesFiltered)

def status_default():
    listStatus =[]
    listStatusStr = ''
    i = 0
    for line in tv.get_children():
        for value in tv.item(line)['values']:
            i += 1
            if i % 5 == 0:
                status = value
                if int(status) in listStatus:
                    pass
                else:
                    listStatus.append(status)
    for j in range(0, len(listStatus)-1):
        Status = str(listStatus[j])
        listStatusStr += Status
    textentryStatusWanted.insert('end', listStatus)


def reset():
    movies = extractMovies("CleanNoH.txt")
    for line in tv.get_children():
        tv.delete(line)
    for i in range(len(movies)):
        tv.insert('', 'end', values=movies[i])



#ajoute une ligne dans le tableau et dans le fichier
def add():
    nName = textentryName.get()
    nYear = textentryYear.get()
    nLength = textentryLength.get()
    nNote = textentryNote.get()
    nStatus = textentryStatus.get()
    nGenre = genre.get(1.0, 'end-1c')
    nResume = resume.get(1.0, 'end-1c')
    nActors = acteurs.get(1.0, 'end-1c')
    nReal = real.get(1.0, 'end-1c')
    nId = id.get(1.0, 'end-1c')
    nTagline = tagline.get(1.0, 'end-1c')
    nKind = kind.get(1.0, 'end-1c')
    new = []
    new.append(nName)
    new.append(nYear)
    new.append(nLength)
    new.append(nNote)
    new.append(nStatus)
    tv.insert('', 'end', values=new)
    new.append(nGenre)
    new.append(nResume)
    new.append(nActors)
    new.append(nReal)
    new.append(nId)
    new.append(nTagline)
    new.append(nKind)
    l = open("CleanNoH.txt", 'a', encoding='utf-8')
    l.write(nName + '\t' + nYear + '\t' + nLength + '\t' + nNote + '\t' + nStatus + '\n')
    l.close()
    write_full("DATALOCAL.txt", new)


#supprime une ligne du tableau après l'avoir supprimé du fichier
def delete():
    i = 0
    selected_item = tv.selection()[0]  ## get selected item
    for value in tv.item(selected_item)['values']:
        i += 1
        if i % 5 == 1:
            titre = value
    deleteline("CleanNoH.txt", titre)
    deleteline("DATALOCAL.txt", titre)
    tv.delete(selected_item)


#modifie une ligne en la supprimant puis en en ajoutant une
def modify():
    delete()
    add()


def search(ifilms):
    i = ifilms
    titre.delete(0.0, 'end')
    annee.delete(0.0, 'end')
    duree.delete(0.0, 'end')
    genre.delete(0.0, 'end')
    note.delete(0.0, 'end')
    resume.delete(0.0, 'end')
    real.delete(0.0, 'end')
    acteurs.delete(0.0, 'end')
    id.delete(0.0, 'end')
    tagline.delete(0.0, 'end')
    kind.delete(0.0, 'end')
    numbermax.delete(0.0, 'end')
    numbercurr.delete(0.0, 'end')
    title = textsearchName.get()
    infos = get_movie_infos(title, i)
    titre.insert('end', infos[0])
    annee.insert('end', infos[1])
    duree.insert('end', infos[2])
    genre.insert('end', infos[3])
    note.insert('end', infos[4])
    resume.insert('end', infos[5])
    acteurs.insert('end', infos[6])
    real.insert('end', infos[7])
    id.insert('end', infos[8])
    tagline.insert('end', infos[9])
    kind.insert('end', infos[10])
    numbermax.insert('end', infos[11])
    numbercurr.insert('end', i+1)

def more_click():
    global ifilms
    ifilms += 1
    search(ifilms)

def less_click():
    global ifilms
    ifilms -= 1
    search(ifilms)

def insert():
    textentryName.delete(0, 'end')
    textentryYear.delete(0, 'end')
    textentryLength.delete(0, 'end')
    textentryNote.delete(0, 'end')
    textentryStatus.delete(0, 'end')
    title = titre.get(1.0, 'end-1c')
    textentryName.insert('end', str(title))
    year = annee.get(1.0, 'end-1c')
    textentryYear.insert('end', str(year))
    length = duree.get(1.0, 'end-1c')
    textentryLength.insert('end', str(length))
    note0 = note.get(1.0, 'end-1c')
    textentryNote.insert('end', str(note0))
    #+ insert les autres trucs dans le fichier DATALOCAL.txt


def selectItem(a):
    titre.delete(0.0, 'end')
    annee.delete(0.0, 'end')
    duree.delete(0.0, 'end')
    genre.delete(0.0, 'end')
    note.delete(0.0, 'end')
    resume.delete(0.0, 'end')
    real.delete(0.0, 'end')
    acteurs.delete(0.0, 'end')
    id.delete(0.0, 'end')
    tagline.delete(0.0, 'end')
    kind.delete(0.0, 'end')
    numbermax.delete(0.0, 'end')
    numbercurr.delete(0.0, 'end')
    curItem = tv.focus()
    title = tv.item(curItem)['values'][0] #nom du film sélectionné
    infos = selectline("DATALOCAL.txt", str(title))
    titre.insert('end', infos[0])
    annee.insert('end', infos[1])
    duree.insert('end', infos[2])
    genre.insert('end', infos[3])
    note.insert('end', infos[4])
    resume.insert('end', infos[5])
    acteurs.insert('end', infos[6])
    real.insert('end', infos[7])
    id.insert('end', infos[8])
    tagline.insert('end', infos[9])
    kind.insert('end', infos[10])
    selected_item = tv.selection()[0]## get selected item


def display_title():
    title = textentryTitle.get()
    title = title.replace(' ', '').replace(',', '').replace(':', '').replace('-', '').replace("'", '')
    title = title.replace('è', 'e').replace('é', 'e').replace('ê', 'e').replace('ï', 'i').replace('à', 'a').replace('ù', 'u').replace('ç', 'c')
    title = title.lower()
    i = 0
    for line in tv.get_children():
        for value in tv.item(line)['values']:
            i += 1
            if i%5 == 1:
                titre = value
                titre = titre.replace(' ', '').replace(',', '').replace(':', '').replace('-', '').replace("'", '')
                titre = titre.replace('è', 'e').replace('é', 'e').replace('ê', 'e').replace('ï', 'i').replace('à', 'a').replace('ù', 'u').replace('ç', 'c')
                titre = titre.lower()
                if str(title) in str(titre):
                    pass
                else:
                    tv.delete(line)

def display_length():
    min = textentryLengthMin.get()
    max = textentryLengthMax.get()
    i = 0
    for line in tv.get_children():
        for value in tv.item(line)['values']:
            i += 1
            if i%5 == 3:
                longueur = value
                if int(max) >= int(longueur) >= int(min):
                    pass
                else:
                    tv.delete(line)

def display_status():
    listStatus = textentryStatusWanted.get()
    listStatus = listStatus.split(',')
    listStatus = list(map(int, listStatus))
    i = 0
    for line in tv.get_children():
        for value in tv.item(line)['values']:
            i += 1
            if i % 5 == 0:
                status = value
                if int(status) in listStatus:
                    pass
                else:
                    tv.delete(line)

def display_year():
    min = textentryYearMin.get()
    max = textentryYearMax.get()
    i = 0
    for line in tv.get_children():
        for value in tv.item(line)['values']:
            i += 1
            if i%5 == 2:
                annee = value
                if int(max) >= int(annee) >= int(min):
                    pass
                else:
                    tv.delete(line)

def display_note():
    min = textentryNoteMin.get()
    max = textentryNoteMax.get()
    i = 0
    for line in tv.get_children():
        for value in tv.item(line)['values']:
            i += 1
            if i%5 == 4:
                note = value
                if float(max) >= float(note) >= float(min):
                    pass
                else:
                    tv.delete(line)

def display_all():
    reset()
    display_title()
    display_year()
    display_length()
    display_note()
    display_status()

def connect(host='http://google.com'):
    try:
        urlopen(host)
        return True
    except:
        return False


tri_fichier("CleanNoH.txt")
tri_fichier("DATALOCAL.txt")
movies = extractMovies("CleanNoH.txt")

tv = ttk.Treeview(root, columns=ac, show='headings', height=20)
for i in range(len(area)):
    if ac[i] == 'Titre':
        tv.column(ac[i], width=300, anchor='c')
    else:
        tv.column(ac[i], width=60, anchor='c')
    tv.heading(ac[i], text=area[i])
tv.pack(side='left', anchor='nw', padx=50)

for i in range(len(movies)):
    tv.insert('', 'end', values=movies[i])

vsb = ttk.Scrollbar(root, orient="vertical", command=tv.yview)
vsb.place(x=591, y=22, height=426)
tv.configure(yscrollcommand=vsb.set)
tv.bind('<ButtonRelease-1>', selectItem)

for col in ac:
    tv.heading(col, text=col, command=lambda _col=col: \
        treeview_sort_column(tv, _col, False))

######################################################################################################################
#################################################CASES################################################################
######################################################################################################################

#####BOUTON D AFFICHAGE#####
canevas = tk.Canvas(root, width=900, height=900)
canevas.place(x=610, y=20)
canevas.create_rectangle(0, 0, 260, 270, fill='grey')

tk.Label(root, text='RECHERCHE LOCALE', background='lightgrey', font=("Courier", 12, "italic")).place(x=660, y=25)

tk.Label(root, text='TITRE :', font=("Courier", 9, "italic")).place(x=620, y=60)
textentryTitle = tk.Entry(root, width=12, font=('Helvetica', 10))
textentryTitle.place(x=690, y=60)
button_year_span = tk.Button(root, text="FILTER", width=6, command=display_title)
button_year_span.place(x=800, y=60)

tk.Label(root, text='ANNEE :', font=("Courier", 9, "italic")).place(x=620, y=100)
textentryYearMin = tk.Entry(root, width=5, font=('Helvetica', 10))
textentryYearMin.place(x=690, y=100)
textentryYearMin.insert('end', 1900)
textentryYearMax = tk.Entry(root, width=5, font=('Helvetica', 10))
textentryYearMax.place(x=740, y=100)
textentryYearMax.insert('end', 2050)
button_year_span = tk.Button(root, text="FILTER", width=6, command=display_year)
button_year_span.place(x=800, y=100)

tk.Label(root, text='DUREE :', font=("Courier", 9, "italic")).place(x=620, y=140)
textentryLengthMin = tk.Entry(root, width=5, font=('Helvetica', 10))
textentryLengthMin.place(x=690, y=140)
textentryLengthMin.insert('end', 0)
textentryLengthMax = tk.Entry(root, width=5, font=('Helvetica', 10))
textentryLengthMax.place(x=740, y=140)
textentryLengthMax.insert('end', 500)
button_length_span = tk.Button(root, text="FILTER", width=6, command=display_length)
button_length_span.place(x=800, y=140)

tk.Label(root, text='NOTE :', font=("Courier", 9, "italic")).place(x=620, y=180)
textentryNoteMin = tk.Entry(root, width=5, font=('Helvetica', 10))
textentryNoteMin.place(x=690, y=180)
textentryNoteMin.insert('end', 0.0)
textentryNoteMax = tk.Entry(root, width=5, font=('Helvetica', 10))
textentryNoteMax.place(x=740, y=180)
textentryNoteMax.insert('end', 9.3)
button_note_span = tk.Button(root, text="FILTER", width=6, command=display_note)
button_note_span.place(x=800, y=180)

tk.Label(root, text='STATUS :', font=("Courier", 9, "italic")).place(x=620, y=220)
textentryStatusWanted = tk.Entry(root, width=5, font=('Helvetica', 10))
textentryStatusWanted.place(x=690, y=220)
status_default()
button_status_wanted = tk.Button(root, text="FILTER", width=6, command=display_status)
button_status_wanted.place(x=800, y=220)

button_reset = tk.Button(root, text="RESET", width=6, command=reset)
button_reset.place(x=750, y=260)
button_filter = tk.Button(root, text="FILTER", width=6, command=display_all)
button_filter.place(x=680, y=260)

#####BOUTON MODIFIER#####
canevas = tk.Canvas(root, width=900, height=900)
canevas.place(x=610, y=300)
canevas.create_rectangle(0, 0, 260, 70, fill='grey')
button_modif = tk.Button(root, text="MODIFIER", command=modify)
button_modif.place(x=709, y=310)
tk.Label(root, text='ATTENTION, ACTION DÉFINITIVE !', font=("Courier", 8), background='grey').place(x=635, y=340)

#####BOUTON DELETE#####
canevas = tk.Canvas(root, width=900, height=900)
canevas.place(x=610, y=380)
canevas.create_rectangle(0, 0, 260, 70, fill='grey')
button_del = tk.Button(root, text="SUPPRIMER", command=delete)
button_del.place(x=705, y=390)
tk.Label(root, text='ATTENTION, ACTION DÉFINITIVE !', font=("Courier", 8), background='grey').place(x=635, y=420)


#####CASES D ECRITURE######
tk.Label(root, text='TITRE :', font=("Courier", 8, "italic")).place(x=120, y=463)
textentryName = tk.Entry(root, width=25, font=('Helvetica', 10))
textentryName.place(x=100, y=483)
tk.Label(root, text='ANNÉE :', font=("Courier", 8, "italic")).place(x=286, y=463)
textentryYear = tk.Entry(root, width=6, font=('Helvetica', 10))
textentryYear.place(x=290, y=483)
tk.Label(root, text='DURÉE :', font=("Courier", 8, "italic")).place(x=342, y=463)
textentryLength = tk.Entry(root, width=6, font=('Helvetica', 10))
textentryLength.place(x=345, y=483)
tk.Label(root, text='NOTE :', font=("Courier", 8, "italic")).place(x=400, y=463)
textentryNote = tk.Entry(root, width=6, font=('Helvetica', 10))
textentryNote.place(x=400, y=483)
tk.Label(root, text='STATUS :', font=("Courier", 8, "italic")).place(x=450, y=463)
textentryStatus = tk.Entry(root, width=6, font=('Helvetica', 10))
textentryStatus.place(x=455, y=483)

#####BOUTONS######
button_add = tk.Button(root, text="ADD", width=6, command=add)
button_add.place(x=30, y=480)
button_search = tk.Button(root, text="SEARCH", command=lambda *args: search(0))
button_search.place(x=560, y=480)
tk.Label(root, text='RECHERCHE IMDB :', font=("Courier", 8, "italic")).place(x=630, y=463)
textsearchName = tk.Entry(root, width=28, font=('Helvetica', 11))
textsearchName.place(x=630, y=483)

#####FOND GRIS######

canevas = tk.Canvas(root, width=900, height=900)
canevas.place(x = 20, y=520)
canevas.create_rectangle(0, 0, 850, 270, fill='grey')


#####CASES PRINCIPALES######
tk.Label(root, text='TITRE :', background='grey', font=("Courier", 8, "italic")).place(x=80, y=552)
titre = tk.Text(root, height=1, width=36, background='lightgrey', font=("Courier", 11))
titre.place(x=40, y=570)
tk.Label(root, text='ANNÉE :', background='grey', font=("Courier", 8, "italic")).place(x=385, y=552)
annee = tk.Text(root, height=1, width=4, background='lightgrey', font=("Courier", 11))
annee.place(x=390, y=570)
tk.Label(root, text='DURÉE :', background='grey', font=("Courier", 8, "italic")).place(x=445, y=552)
duree = tk.Text(root, height=1, width=4, background='lightgrey', font=("Courier", 11))
duree.place(x=450, y=570)
tk.Label(root, text='GENRE(S) :', background='grey', font=("Courier", 8, "italic")).place(x=520, y=552)
genre = tk.Text(root, height=1, width=27, background='lightgrey', font=("Courier", 11))
genre.place(x=510, y=570)
tk.Label(root, text='NOTE :', background='grey', font=("Courier", 8, "italic")).place(x=775, y=552)
note = tk.Text(root, height=1, width=4, background='lightgrey', font=("Courier", 11))
note.place(x=780, y=570)

#####TITRE######
tk.Label(root, text='INFORMATIONS', background='lightgrey', font=("Courier", 12, "italic")).place(x=420, y=525)

#####CASE RESUME######
tk.Label(root, text='RÉSUMÉ :', background='grey', font=("Courier", 8, "italic")).place(x=80, y=600)
resume = tk.Text(root, height=5, width=90, background='lightgrey', wrap='word', font=("Courier", 11))
resume.place(x=40, y=620)

#####CASES ACTEURS ET REAL######
tk.Label(root, text='ACTEURS :', background='grey', font=("Courier", 8, "italic")).place(x=80, y=720)
acteurs = tk.Text(root, height=1, width=60, background='lightgrey', font=("Courier", 11))
acteurs.place(x=50, y=740)
tk.Label(root, text='RÉALISATEUR :', background='grey', font=("Courier", 8, "italic")).place(x=660, y=720)
real = tk.Text(root, height=1, width=18, background='lightgrey', font=("Courier", 11))
real.place(x=650, y=740)

#####CASES ID KIND TAGLINE######
id = tk.Text(root, height=1, width=8, font=("Courier", 7, "italic"), background='grey', bd=1)
id.place(x=40, y=530)
kind = tk.Text(root, height=1, width=8, font=("Courier", 8, "italic"), background='grey', bd=0)
kind.place(x=90, y=528)
tagline = tk.Text(root, height=1, width=100, font=("Courier", 9, "italic"), background='grey', bd=0)
tagline.place(x=40, y=770)
numbermax = tk.Text(root, height=1, width=2, font=("Courier", 9, "italic"), background='grey', bd=0)
numbermax.place(x=760, y=530)
numbercurr = tk.Text(root, height=1, width=2, font=("Courier", 9, "italic"), background='grey', bd=0)
numbercurr.place(x=730, y=530)
#####BOUTON INSERT######
button_inser = tk.Button(root, text="INSERT", width=6, command=insert)
button_inser.place(x=580, y=525)
button_less = tk.Button(root, text="<-", width=2, command=less_click)
button_less.place(x=800, y=525)
button_more = tk.Button(root, text="->", width=2, command=more_click)
button_more.place(x=830, y=525)


version = tk.Text(root, height=1, width=20, font=("Courier", 9, "italic"), background='grey95', bd=0)
version.place(x=80, y=810)
Version = "Version : "+Version
version.insert('end', Version)

result = 'connected' if connect() else 'no connection!'
colResult = 'green' if connect() else 'red'
connected = tk.Text(root, height=1, width=10, font=("Courier", 10), background='grey95', bd=0)
connected.place(x=700, y=810)
connected.insert('end', result)
connectedSymb = tk.Text(root, height=1, width=2, font=("Courier", 10), background='grey95', fg=colResult, bd=0)
connectedSymb.place(x=682, y=810)
connectedSymb.insert('end', '⬤')

root.mainloop()
