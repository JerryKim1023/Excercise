from flask import Flask, Response, redirect, render_template,request,jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# push_up page로 이동
@app.route('/push_up', methods=['GET'])
def push_up():
    if request.method == 'GET':
        return render_template('push_up.html', result="success")
    else:
        return redirect('/')

# burpee page로 이동
@app.route('/burpee', methods=['GET'])
def burpee():
    if request.method == 'GET':
        print("1")
        return render_template('burpee.html', result="success", msg="전신운동 조지자!")
    else:
        print("2")
        return redirect('/')

# deck_of_pain_rep page로 이동
@app.route('/deck_of_pain_rep', methods=['GET'])
def deck_of_pain_rep():
    if request.method == 'GET':
        print("1")
        return render_template('deck_of_pain_rep.html', result="success", msg="하체운동 조지자!")
    else:
        print("2")
        return redirect('/')

# --------------------------------  상체  --------------------------------

@app.route('/push_up/set_play', methods=['GET'])
def push_up_set():
    print(request)
    max_num_receive = request.args.get('max_num_give')
    min_num_receive = request.args.get('min_num_give')
    print(max_num_receive)
    print(min_num_receive)
    max_num = int(max_num_receive)
    min_num = int(min_num_receive)

    exercise_list = []

    while max_num-min_num >= 1:
        exercise_list.append(max_num)
        max_num -= 1

        exercise_list.append(min_num)
        min_num += 1

# 리스트를 클라이언트로 넘겨줘서 엔터마다 하나씩 읽게 만들면 됨. continue?로 엔터처럼 사용자가 원하는 타이밍에 넘기는 게 가능?
    print("상체 운동이 끝났습니다!!")
    

    return render_template('push_up.html', result="You've done all of push ups")


# --------------------------------  전신  --------------------------------

@app.route('/burpee/set_play', methods=['GET'])
def burpee_set():
    if request.method == 'GET':
        print("1")
        return render_template('burpee.html', result="success", msg="전신운동 조지자!")
    else:
        print("2")
        return redirect('/')



# --------------------------------  하체  --------------------------------

@app.route('/deck_of_pain_rep/set_play', methods=['GET'])
def deck_of_pain_rep_set():
    if request.method == 'GET':
        print("1")
        return render_template('deck_of_pain_rep.html', result="success", msg="전신운동 조지자!")
    else:
        print("2")
        return redirect('/')



@app.route('/test', methods=['GET'])
def test_get():
   #  title_give로 가져온 값을 가져와 그게 title_receive야
   title_receive = request.args.get('title_give')
   print(title_receive)
   # 이쪽을 response로 보내줄게
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
   #  title_give으로 받아온 값 가져와봐
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})





if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)



