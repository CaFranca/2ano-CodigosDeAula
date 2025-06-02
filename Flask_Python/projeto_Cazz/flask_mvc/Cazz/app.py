from flask import Flask
from controllers import tarefa_controller as task

app = Flask(__name__)
app.register_blueprint(task)

if __name__ =='__main__':
    app.run(debug=True)
        