from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return ('<h1>This test app</h1>')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
 app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
