from flask_wtf import FlaskForm #PARA PODER FAZER UM FORMULARIO
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField #PARA FALAR QUAL É SENHA, TEXTO E CONFIRMAÇÃO
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError #PARA DETERMINAR AS REGRAS DE CADA LUGAR
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar.')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembre-me')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Excel Impresionador')
    curso_vba = BooleanField('VBA Impresionador')
    curso_powerbi = BooleanField('Power BI Impresionador')
    curso_python = BooleanField('Python Impresionador')
    curso_ppt = BooleanField('Apresentações Impresionador')
    curso_sql = BooleanField('SQL Impresionador')
    botao_submit_editarperfil = SubmitField('Confirmar Edição')


    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com esse e-mail. Cadastre outro e-mail.')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2, 140)])
    corpo = TextAreaField('Escreva seu Post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')
