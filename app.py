from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'website_secret_key'


def main():
    pass


@app.route('/')
def main_page():
    """основная страница"""
    pass


@app.route('/information')
def info():
    """страница с информацией о сайте"""


if __name__ == '__main__':
    main()
