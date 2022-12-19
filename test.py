from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    print(request.method)
    print(request.args)

    count = int(request.cookies.get('visit',0))
    count = count+1
    message = 'you visit {} times.'.format(count)
    response = make_response(message)
    response.set_cookie('visit',str(count))
    return response
    #return "hello world!"

if __name__ == '__main__':
    app.run(debug=True)