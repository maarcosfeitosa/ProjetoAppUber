from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from jogoteca import app, db
from moldels import Ganhos, Verifica_Nulo
from helpers import FormularioGanhos
import time
from datetime import *
import locale
from sqlalchemy import extract


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

@app.route('/')
def index():
    lista = Ganhos.query.order_by(Ganhos.data)
    return render_template('lista.html', titulo='Ganhos', ganhos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioGanhos()
    return render_template('novo.html', titulo='Inserir_Ganhos', form=form)

@app.route('/criar', methods=['POST',])
def criar():
    form = FormularioGanhos(request.form)

    data = form.data_ganho.data
    ganhos = form.ganhos.data
    km = form.km.data
    consumo = form.consumo.data
    combustivel = form.combustivel.data

    verifica = Verifica_Nulo(km, consumo, combustivel)

    ganho = Ganhos.query.filter_by(data=data).first()

    if ganho:
        flash('Data já existente!')
        return redirect(url_for('index'))

    novo_ganho = Ganhos(data=data, ganhos=ganhos, km=verifica.km, consumo=verifica.consumo, combustivel=verifica.combustivel)
    db.session.add(novo_ganho)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/editar/<data_ganho>')
def editar(data_ganho):
    
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', data_ganho=data_ganho)))
    ganho = Ganhos.query.filter_by(data=data_ganho).first()
    form = FormularioGanhos()
    form.data_ganho.data = ganho.data
    form.ganhos.data = ganho.ganhos
    form.km.data = ganho.km
    form.consumo.data = ganho.consumo
    form.combustivel.data = ganho.combustivel
    #capa_jogo = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Ganhos', data=data_ganho, form=form)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    form = FormularioGanhos(request.form)

    print ("Nulo")
    verifica = Verifica_Nulo(form.km.data, form.consumo.data, form.combustivel.data)
    print (verifica.km)
    print (verifica.consumo)
    print (verifica.combustivel)
    
    ganho = Ganhos.query.filter_by(data=request.form['data_ganho']).first()
    ganho.data = form.data_ganho.data
    ganho.ganhos = form.ganhos.data
    ganho.km = verifica.km
    ganho.consumo = verifica.consumo
    ganho.combustivel = verifica.combustivel

    db.session.add(ganho)
    db.session.commit()
      
    return redirect(url_for('index'))

@app.route('/deletar/<data_ganho>')
def deletar(data_ganho):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Ganhos.query.filter_by(data=data_ganho).delete()
    db.session.commit()
    flash('Data deletada com sucesso!')

    return redirect(url_for('index'))

@app.route('/ganhos_mensais/<data_mostra>')
def ganhos_mensais(data_mostra):
    if data_mostra == None:
        data_mostra = datetime.month
        ganhos = Ganhos.query.filter_by(data=data_mostra.date.month).all()
        return render_template('lista_separada.html', ganhos=ganhos)
   
    ganhos = Ganhos.query.filter(extract('month', Ganhos.data)==5).all()
    
    return render_template('lista_separada.html', ganhos=ganhos)


    