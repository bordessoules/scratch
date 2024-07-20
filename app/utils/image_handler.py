import uuid
import os
from flask import current_app

def save_image(image):
    filename = str(uuid.uuid4()) + os.path.splitext(image.filename)[1]
    image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
    return filename