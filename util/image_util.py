import cv2
import uuid
from datetime import datetime
from config.config import CERTIFICATE_FOLDER

class ImageUtil:

    def __init__(self):
        self.location_name = (1039, 2033)
        self.location_date = (1080, 3033)
        self.fontScale = 9
        self.color = (255, 0, 0)
        self.thickness = 2
        self.font = cv2.FONT_HERSHEY_SIMPLEX


    def write(self, text = "Candra"):
        img = cv2.imread('./certificates/cert01.jpeg')
        add_space = ''
        for i in range(round((17-len(text))/2)):
            add_space += ' '
        text = add_space + text + add_space



        # textsize = cv2.getTextSize(text, font, 1, 2)[0]
        # textX = (img.shape[1] - textsize[0]) / 2
        # textY = (img.shape[0] + textsize[1]) / 2
        # textX = round(( (img.shape[1] - textsize[0]) - (2500)) / 2)
        # textY = round((img.shape[0] + textsize[1]) / 2) + 300
        cv2.putText(img, text, self.location_name, self.font, self.fontScale, self.color, self.thickness, cv2.LINE_AA)
        cv2.putText(img, datetime.now().strftime("%d-%m-%Y"), self.location_date, self.font, 3, self.color, self.thickness, cv2.LINE_AA)
        new_file = 'certificate_' + str(uuid.uuid4()) + '.jpeg'
        cv2.imwrite(CERTIFICATE_FOLDER + new_file, img)
        return new_file

