from flask import Flask, render_template, request
from camera import Camera
from object import Object
from change_state import *
import numpy as np

app = Flask(__name__)

CAM = initial_camera()
OBJ = Object('old_wolf3.stl')

@app.route("/",methods=['GET','POST'])
def home():
    global CAM,OBJ
    if request.method == 'POST':
        print(request.form)
        if request.form['action'] == "Generate":  
            CAM = modify_state(CAM, OBJ, request.form['transla'], (request.form['rota'],request.form['radios-eixo']), request.form['radios'])
            
        if request.form['action'] == "Reset":
            CAM = initial_camera()

        if request.form['action'] == "Camera":
            #print(request.form)
            CAM = Camera(motion_matrix=CAM.cam,
            focal_distance= int(request.form['focal']),
            width_px = int(request.form['w_px']), 
            height_px = int(request.form['h_px']),
            width_mm = int(request.form['w_mm']),
            height_mm = int(request.form['h_mm']))

        gerar_imagens(CAM,OBJ)
        return render_template("screen.html",camera_focal = CAM.focal_distance, camera_w_px = CAM.width_px,camera_h_px = CAM.height_px,camera_w_mm = CAM.width_mm,camera_h_mm = CAM.height_mm)
    elif request.method == 'GET':

        print(request.form)

        print(CAM)
        gerar_imagens(CAM,OBJ)
        print(CAM)

        return render_template("screen.html",camera_focal = CAM.focal_distance, camera_w_px = CAM.width_px,camera_h_px = CAM.height_px,camera_w_mm = CAM.width_mm,camera_h_mm = CAM.height_mm)
    else:
        return 'invalid http method'
    
if __name__ == "__main__":
    app.run(debug=True)