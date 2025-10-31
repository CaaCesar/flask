from estudo import app
from flask import render_template, url_for, request, redirect

from estudo.models import Contato
from estudo.forms import ContatoForm
from estudo import db

@app.route('/')
def homepage():
    context ={
        'usuario': 'Usuario',
        'idade': 25,
    }
    return render_template('index.html', context=context)


@app.route('/nova/', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
        

    return render_template('contato.html', context=context, form=form)





# Formato não recomendado de lidar com formulários
@app.route('/nova/', methods=['GET', 'POST'])
def contatoold():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        context.update({'pesquisa': pesquisa})
        print(f'GET: {pesquisa}')
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contato = Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )

        db.session.add(contato)
        db.session.commit()
        
    return render_template('contato_old.html', context=context)
