import tempfile
import os
from flask import Flask, request, redirect, send_file, render_template
from skimage import io
from skimage.transform import resize
import base64
import glob
import numpy as np

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        img_data = request.form.get('myImage').replace("data:image/png;base64,", "")
        aleatorio = request.form.get('numero')
        folder_id = '1bjhGYXx9opwIgZj4FO95we5TpBep92S7'  # Reemplaza con la ID de tu carpeta en Google Drive
        file_name = aleatorio + '_image.png'
        with tempfile.NamedTemporaryFile(delete = False, mode = "w+b", suffix='.png', dir=str(aleatorio)) as fh:
            fh.write(base64.b64decode(img_data))
        print(f"Image uploaded {file_name}")
    except Exception as err:
        print("Error occurred")
        print(err)

    return redirect("/", code=302)
    
@app.route('/prepare', methods=['GET'])
def prepare_dataset():
    d = ["Niebla","Roca","Hojas","Arena","Nubes"]
    for digit in d:
        images = []
        filelist = glob.glob('{}/*.png'.format(digit))
        images_read = io.concatenate_images(io.imread_collection(filelist))
        images_read = images_read[:, :, :, 3]
        images.append(images_read)
        images = np.vstack(images)
        np.save('{}.npy'.format(digit), images)
    return "Data set procesado exitosamente"

@app.route('/Niebla.npy', methods=['GET'])
def download_Niebla():
    return send_file('./Niebla.npy')

@app.route('/Roca.npy', methods=['GET'])
def download_Roca():
    return send_file('./Roca.npy')

@app.route('/Hojas.npy', methods=['GET'])
def download_Hojas():
    return send_file('./Hojas.npy')

@app.route('/Arena.npy', methods=['GET'])
def download_Arena():
    return send_file('./Arena.npy')

@app.route('/Nubes.npy', methods=['GET'])
def download_Nubes():
    return send_file('./Nubes.npy')

@app.route('/Niebla.npy', methods=['GET'])
def download_Niebla():
    return send_file('./Niebla.npy')

@app.route('/Roca.npy', methods=['GET'])
def download_Roca():
    return send_file('./Roca.npy')

@app.route('/Hojas.npy', methods=['GET'])
def download_Hojas():
    return send_file('./Hojas.npy')

@app.route('/Arena.npy', methods=['GET'])
def download_Arena():
    return send_file('./Arena.npy')

@app.route('/Nubes.npy', methods=['GET'])
def download_Nubes():
    return send_file('./Nubes.npy')
    
if __name__ == "__main__":
    
    digits = ["Niebla","Roca","Hojas","Arena","Nubes"]
    for d in digits:
        if not os.path.exists(str(d)):
            os.mkdir(str(d))
    app.run()
