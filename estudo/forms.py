from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from estudo.models import Contato, User, Post, PostComentarios
from estudo import db, bcrypt

class UserForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha =  PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirme sua Senha', validators=[DataRequired(), EqualTo('senha')])
    btnSubmit = SubmitField('Cadastrar')

        
    def validade_email(self, email):
        if User.query.filter(email=email).first():
            return ValidationError('Usuário já cadastrado')

    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        user = User(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha=senha
        )
        
        db.session.add(user)
        db.session.commit()
        return user

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha =  PasswordField('Senha', validators=[DataRequired()])
    btnSubmit = SubmitField('Login')
    
    def login(self):
        # RECUPERAR O USUÁRIO E O E-MAIL
        user = User.query.filter_by(email=self.email.data).first()
        # VERIFICA SE A SENHA É VÁLIDA
        if user:
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                # RETORNA O USUÁRIO
                return user
            else:
                raise Exception('Senha Incorreta!!!')
        else:
            # SE O USUÁRIO NAO EXISTIR IRA DAR ERRO
            raise Exception('Usuário não encontrado!!')
        
class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    assunto = StringField('Assunto', validators=[DataRequired()])
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        contato = Contato(
            nome=self.nome.data,
            email=self.email.data,
            assunto=self.assunto.data,
            mensagem=self.mensagem.data
        )
        db.session.add(contato)
        db.session.commit()

class PostForm(FlaskForm):
    mensagem = StringField('Mensagem', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self, user_id):
        post = Post(
            mensagem=self.mensagem.data,
            user_id = user_id
        )
        
        db.session.add(post)
        db.session.commit()

class CommentForm(FlaskForm):
    comentario = StringField('Comentario', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self, user_id, post_id):
        post = PostComentarios(
            comentario=self.comentario.data,
            user_id = user_id,
            post_id = post_id
        )
        
        db.session.add(post)
        db.session.commit()