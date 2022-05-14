from flask import *

from .ciphers import TranspositionCipher, CeaserCipher
from .forms import CipherForm

views = Blueprint('views', __name__)

@views.route('/')
def home():

    return render_template('index.html')

@views.route('/transposition/')
def transposition():

    form = CipherForm()

    return render_template('transposition_cipher.html', form=form)

@views.route('/ceaser/')
def ceaser():

    form = CipherForm()

    return render_template('ceaser_cipher.html', form=form)

@views.route('/transposition_encrypt/', methods=['POST', 'GET'])
def transposition_encrypt():

    data = None

    form = CipherForm()

    if form.validate_on_submit():

        text = form.text.data

        key = form.key.data

        plaintext = TranspositionCipher(text)

        ciphertext = plaintext.encrypt_message(key)

    return render_template('result.html', data = ciphertext)

@views.route('/transposition_decrypt/', methods=['POST', 'GET'])
def transposition_decrypt():

    data = None

    form = CipherForm()

    if form.validate_on_submit():

        text = form.text.data

        key = form.key.data

        ciphertext = TranspositionCipher(text)

        plaintext = ciphertext.decrypt_message(key)

    return render_template('result.html', data = plaintext)

@views.route('/ceaser_encrypt/', methods=['POST', 'GET'])
def ceaser_encrypt():

    data = None

    form = CipherForm()

    if form.validate_on_submit():

        text = form.text.data

        key = form.key.data

        plaintext = CeaserCipher(text)

        ciphertext = plaintext.encrypt_message(key)

    return render_template('result.html', data = ciphertext)

@views.route('/ceaser_decrypt/', methods=['POST', 'GET'])
def ceaser_decrypt():

    data = None

    form = CipherForm()

    if form.validate_on_submit():

        text = form.text.data

        key = form.key.data

        ciphertext = CeaserCipher(text)

        plaintext = ciphertext.decrypt_message(key)

    return render_template('result.html', data = plaintext)