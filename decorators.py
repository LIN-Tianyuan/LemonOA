from functools import wraps
from flask import g, redirect, url_for


def login_required(func):
    # Retaining information about func
    @wraps(func)
    # func(a,b,c)
    # func(1,2,c=3)
    def inner(*args, **kwargs):
        if g.user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("auth.login"))
    return inner

"""
@login_required
def public_question(question_id)
    pass
    
=>

login_required(public_question)(question_id)
"""

