from run import creatApp

app = creatApp()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.errorhandler(404)
def not_found(error):
    return '404'

if __name__ == '__main__':
    app.run()
