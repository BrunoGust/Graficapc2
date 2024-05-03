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
    images = []
    digits = []
    y = []
    d = [0,1,2,3,4]
    for digit in d:
      filelist = glob.glob('{}/*.png'.format(digit))
      images_read = io.concatenate_images(io.imread_collection(filelist))
      images_read = images_read[:, :, :, 3]
      digits_read = np.array([digit] * images_read.shape[0])
      images.append(images_read)
      digits.append(digits_read)
    images = np.vstack(images)
    digits = np.concatenate(digits)
    np.save('X.npy', images)
    np.save('y.npy', digits)
    return "OK!"

@app.route('/X.npy', methods=['GET'])
def download_X():
    return send_file('./X.npy')
@app.route('/y.npy', methods=['GET'])
def download_y():
    return send_file('./y.npy')
    
if __name__ == "__main__":
    
    digits = [0,1,2,3,4]
    for d in digits:
        if not os.path.exists(str(d)):
            os.mkdir(str(d))
    app.run()
