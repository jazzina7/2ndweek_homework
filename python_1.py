from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

articles = []
no = 1

## HTML을 주는 부분
@app.route('/')
def home():
    return 'This is Home!'


@app.route('/mypage')
def mypage():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
    global articles
    global no

    name_receive = request.form['name_give']
    amount_receive = request.form['amount_give']
    address_receive = request.form['address_give']
    phoneno_receive= request.form['phoneno_give']

    article={}
    article['name'] = name_receive
    article['amount']=amount_receive
    article['address'] = address_receive
    article['phoneno'] = phoneno_receive

    no = no + 1
    articles.append(article)


    return jsonify({'result': 'success'})


@app.route('/delete', methods=['POST'])
def delete_article():
   global articles

   no_receive = request.form['no_give']

   for article in articles:
    if article['no']==no_receive:
       articles.remove(article)

   del articles[no_receive]

   return jsonify({'result': 'success'})

@app.route('/test', methods=['GET'])
def test_get():
    return jsonify({'result': 'success', 'variables': articles})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)