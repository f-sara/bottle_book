
# フォーム関係の画面遷移

from bottle import Bottle, jinja2_template as template, request, redirect
from bottle import response
import routes
from models import connection, Books
from utils.util import Utils
from utils.auth import Auth

app = routes.app
auth = Auth()

# 登録フォームを処理する
@app.route('/add', method=['GET', 'POST'])
def add():
    # 認証確認
    auth.check_login()
    registId = ""
    form = {}
    kind = "登録"

    if request.method == 'GET':
        # id指定された場合
        # 編集画面
        if request.query.get('id') is not None:
            book = connection.query(Books).filter\
                (Books.id_ == request.query.get('id')).first()
            form['name'] = book.name
            form['volume'] = book.volume
            form['author'] = book.author
            form['publisher'] = book.publisher
            form['memo'] = book.memo
            registId = book.id_
            
            kind = "編集"
        # フォーム画面表示処理
        return template('add.html'
                        , form=form
                        , kind=kind
                        , registId=registId)
    # POSTされた場合
    elif request.method == 'POST':
        # POST値の取得
        form['name'] = request.forms.decode().get('name')
        form['volume'] = request.forms.decode().get('volume')
        form['author'] = request.forms.decode().get('author')
        form['publisher'] = request.forms.decode().get('publisher')
        form['memo'] = request.forms.decode().get('memo')
        registId = ""
        # idが指定されている場合
        if request.forms.decode().get('id') is not None:
            registId = request.forms.decode().get('id')
 
        # バリデーション処理
        errorMsg = Utils.validate(data=form)

        # コンソールに表示処理
        print(errorMsg)
        if request.forms.get("next") == "back":
            return template("add.html"
                            , form=form
                            , kind=kind
                            , registId=registId)
        
        if  errorMsg == []:
            # 入力エラーがないと確認画面を表示
            headers = ['著書名', '卷数', '著作者', '出版社', 'メモ']
            return template('confirm.html'
                            , form=form
                            , headers=headers
                            , registId=registId)
        else:
            #n油力エラーがあると再度入力画面を表示
            return template('add.html'
                            , error=errorMsg
                            , kind=kind
                            , form=form
                            , registId=registId)

# 確認画面から登録処理にpostされる
@app.route('/regist', method='POST')
def regist():
    # 認証確認
    auth.check_login()
    # データ受け取り
    name = request.forms.decode().get('name')
    volume = request.forms.decode().get('volume')
    author = request.forms.decode().get('author')
    publisher = request.forms.decode().get('publisher')
    memo = request.forms.decode().get('memo')
    registId = request.forms.decode().get('id')

    if request.forms.get('next') == 'back':
        # 確認画面から戻るボタンを押す
        # 登録フォームに戻る
        response.status = 307
        response.set_header("Location", '/add')
        return response
    else:
        if registId is not None:
            # 更新処理
            book = connection.query(Books).filter\
                (Books.id_ == registId).first()
            book.name = name
            book.volume = volume
            book.author = author
            book.publisher = publisher
            book.memo = memo
            connection.commit()
            connection.close()
        else:
            # 登録処理
            book = Books(
                name = name,
                volume = volume,
                author = author,
                publisher = publisher,
                memo = memo,
                delFlg = False)
            connection.add(book)
            connection.commit()
            connection.close()
        redirect('/list') # 一覧画面に遷移

# リスト画面から削除ボタンが押される
@app.route('/delete/<dataId>')
def delete(dataId):
    # 認証確認
    auth.check_login()
    # 論理削除を実行
    book = connection.query(Books).filter\
        (Books.id_ == dataId).first()
    book.delFlg = True
    connection.commit()
    connection.close()
    redirect('/list')