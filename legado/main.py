from flask import Flask,render_template,request,redirect,url_for
from legado.models import Medico, Paciente
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login_medico', methods=['GET', 'POST']) #ROTA PARA O LOGIN DO MEDICO
def login_medico():
    if request.method == 'GET':
        return render_template('login-medico.html')
    elif request.method == 'POST':
        id= request.form['idCRM']
        Senha = request.form['senha']
        medico = Medico.query.filter_by(id=id).first()
        if medico and medico.senha == Senha:
            return render_template('page_medico.html')
        else:
            return render_template('login-medico.html')
@app.route('/cadastrarMedico', methods=['GET', 'POST']) #ROTA PARA O CADASTRO DO MEDICO
def cadastrarMedico():
    if request.method == 'GET':
        return render_template('cadastroMedico.html')
    elif request.method == 'POST':
        nomeMedico = request.form['nomeMedico']
        especialidade = request.form['especialidade']
        clinica = request.form['clinica']
        cidade_clinica = request.form['cidClinica']
        id=request.form['idCRM'] #ID DO MEDICO , ESSA VARIAVEL SERA USADA NO CADASTRO DO MEDICO, A VARIAVEL ID POSSUE VALOR UNICO PARA CADASTRO NAO PODENDO TER UMA IGUAL
        telefone = request.form['telMedico']
        senha = request.form['senhaMedico']
        novo_medico = Medico(nome=nomeMedico, especialidade=especialidade, clinica=clinica, cidade_clinica=cidade_clinica,id=id, telefone=telefone, senha=senha)
        db.session.add(novo_medico)
        db.session.commit()
        if id == novo_medico.id:
            return alert ("CRM ja cadastrado")
        else:
            return redirect(url_for('login_medico'))

@app.route('/cadastrarPaciente', methods=['GET', 'POST']) #ROTA PARA O CADASTRO DO PACIENTE NO SISTEMA
def cadastrarPaciente():
    if request.method == 'GET':
        return render_template('cadastra_Paciente.html')
    elif request.method == 'POST':
        nome = request.form['nome_paciente']
        id = request.form['cadastro_pessoa']
        telefone = request.form['tel_paciente']
        data = request.form['data_nasc_paciente']
        email = request.form['email_paciente']
        novo_paciente = Paciente(nome=nome, id=id, telefone=telefone, idade=data, senha=email)
        db.session.add(novo_paciente)
        db.session.commit()
        return render_template('cadastra_paciente.html')
    
if __name__ == '__main__':
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)  