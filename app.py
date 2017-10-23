from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import soundcloud
def get_comments(url_in):
    client = soundcloud.Client(client_id='406ab22163491158a886303b41395b21',
                           client_secret='7a6a23159d92fbba7d66cc6b57c9dc47',
                           redirect_uri='google.com')
    #redirect user to authorize URL
    client.authorize_url()
    results = []
    try:
        track = client.get('/resolve', url=url_in)
        comments = client.get('/tracks/%d/comments' % track.id)
        for comment in comments:
        x = comment.body
        if " - " in x:
            if "@" in x:
                try:
                    x = x.split(": ")[1]
                except:
                    pass
            results.append(x)
            print (x)
    except:
        results = ['No Result... sorry']
    return results

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
      block_start_string='{%',
      block_end_string='%}',
      variable_start_string='((',
      variable_end_string='))',
      comment_start_string='{#',
      comment_end_string='#}',
    ))


app = CustomFlask(__name__)
app.config.from_pyfile('db.cfg')
db = SQLAlchemy(app)




@app.route("/", methods=['POST', 'GET'])
def index():
    message = "Hello Flask!"
    if request.method == 'POST':
        return render_template('index.html', message = request.form['fooput'], results = get_comments(request.form['fooput']))
#result=request.form['fooput']results = get_comments(request.form['fooput']
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/example')
def example():
    message = "Hello Flask!"
    return render_template('example.html', message=message)


@app.route('/more')
def more():
    return render_template('more.html')


def initialize_database():
    app.logger.info('Database is not created, exec create_all() here.')
    db.create_all()
    data1 = Todo('todo1')
    data2 = Todo('todo2')
    db.session.add(data1)
    db.session.add(data2)
    db.session.commit()


@app.route('/sqlalchemy')
def sqlalchemy():
    todos = []
    try:
        todos = Todo.query.order_by(Todo.pub_date.desc()).all()
    except:
        initialize_database()
    return render_template('sqlalchemy.html', todos=todos)


@app.route('/sqlalchemy/get', methods=['GET'])
def sqlalchemy_get():
    todos = Todo.query.order_by(Todo.pub_date.desc()).all()
    return jsonify(todos=[todo.get_dict() for todo in todos])


@app.route('/sqlalchemy/new', methods=['POST'])
def sqlalchemy_new():
    if request.json:
        db.session.add(Todo(request.json['title']))
        db.session.commit()
    return jsonify(status='ok') # Oops: always ok...


@app.route('/sqlalchemy/update', methods=['POST'])
def sqlalchemy_update():
    if request.json:
        todo = Todo.query.get(request.json['id'])
        todo.done = request.json['done']
        todo.title = request.json['title']
        db.session.commit()
    return jsonify(status='ok') # Oops: always ok...


@app.route('/router')
def router():
    return render_template('router.html')


@app.route('/sfc')
def sfc():
    return render_template('sfc.html')

wurst = 'Wurstig'

@app.route('/typescript')
def typescript():
    return render_template('typescript.html')


@app.route('/vuex')
def vuex():
    return render_template('vuex.html')


@app.route('/v0.10.3')
def v0_10_3():
    return render_template('vue.js_v0.10.3.html')


if __name__ == '__main__':
    app.run(debug=True)
