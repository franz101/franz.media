from flask import Flask, render_template, request
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




@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return render_template('index.html', message = request.form['fooput'], results = get_comments(request.form['fooput']))
#result=request.form['fooput']results = get_comments(request.form['fooput']
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
