

from flask import Flask, jsonify, send_file, redirect, request

app = Flask(__name__)

@app.route('/text')
def text():
    return '文本接口返回'

@app.route('/json')
def return_json():
    data = {"msg":"This is a json Res"}
    return jsonify(data)

@app.route('/image')
def return_img():
    imgpath = r"E:\test.jpg"
    return send_file(imgpath,mimetype='image/jpeg')

@app.route('/hi/<name>')
def he(name):
    return f"hi {name}"

@app.route('/hi/<int:num>')
def number(num):
    return f"hi {num + ' ' + num }"

@app.route('/test/<num>/')
def add(num):
    return f"test {num + num }"

@app.route('/baidu')
def baidu():
    return redirect('https://www.baidu.com')

@app.route('/test/fird',methods=["POST"])

def fidr_json():
    try:
        my_json = request.get_json()
        print(my_json)
        get_name = my_json.get('name')
        get_age = my_json.get('age')
        print(get_age)

        if not all([get_age, get_name]):
            return '检查参数是否正确'

        get_age += 10
        return jsonify(name=get_name, get=get_age)

    except Exception as e:
        print(e)
        return '错误访问，请检查'



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)