import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired
from models import UserModel, EmailCaptchaModel
from exts import db


# Form: is mainly used to verify whether the data submitted by the front-end meets the requirements
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Wrong email format!")])
    captcha = wtforms.StringField(validators=[Length(min=4, max=4, message="Wrong format of captcha!")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="Wrong format of username!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Wrong format of password!")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    # Custom Validation
    # Is the mailbox already registered?
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="This email address has already been registered!")

    # Is the verification code correct?
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="Wrong email or verification code!")
        # todo: You can delete the captcha_model(done)
        else:
            db.session.delete(captcha_model)
            db.session.commit()


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Wrong email format!")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="Wrong format of password!")])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="The title is incorrectly formatted!")])
    content = wtforms.StringField(validators=[Length(min=3, message="The content is incorrectly formatted!")])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="The content is incorrectly formatted!")])
    question_id = wtforms.IntegerField(validators=[InputRequired(message="The issue id must be passed in!")])