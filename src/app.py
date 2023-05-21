from flask import Flask, render_template, request
from camera import Camera
from object import Object
from change_state import *
import numpy as np

app = Flask(__name__)

CAM = initial_camera()
OBJ = Object('old_wolf3.stl')

@app.route("/",methods=['GET','POST','PATCH'])
def home():
    global CAM,OBJ
    if request.method == 'POST':
        print(request.form)
        if request.form['action'] == "Generate":  
            print(request.form)
            print(CAM.cam)
            CAM = modify_state(CAM, OBJ, request.form['transla'], '', request.form['radios'])
            print(CAM.cam)
            
        if request.form['action'] == "Reset":
            CAM = initial_camera()

        gerar_imagens(CAM,OBJ)
        return render_template("screen.html")
    elif request.method == 'GET':

        print(request.form)

        print(CAM)
        gerar_imagens(CAM,OBJ)
        print(CAM)

        return render_template("screen.html")
    else:
        return 'invalid http method'
    
if __name__ == "__main__":
    app.run(debug=True)