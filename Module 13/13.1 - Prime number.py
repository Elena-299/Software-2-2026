from flask import Flask

app = Flask(__name__)

def prime_number(num):
    num = int(num)
    i = 2
    while i != num:
        if num % i == 0:
            give = "false"
            break
        elif i == num-1:
            give = "true"
        i = i+1
    return give

@app.route('/prime_number/<num>')
def check(num):
    result = {
        "Number": num,
        "isPrime": prime_number(num)
    }
    return result

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)