# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import cv2
import imutils

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QRadioButton, QPushButton, QLineEdit
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

class Widget(QWidget):

    def detect(self, frame):
        cv2.imshow('output', frame)

        bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)

        person = 1
        for x,y,w,h in bounding_box_cordinates:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
            person += 1

        cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
        cv2.putText(frame, f'Total Persons : {person-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
        cv2.imshow('output', frame)

        return frame

    def humanDetector(self, args):
        # print(args)
        image_path = args["image"]
        video_path = args['video']
        if str(args["camera"]) == 'true' : camera = True
        else : camera = False

        writer = None
        if args['output'] is not None:
            writer = cv2.VideoWriter(args['output'],cv2.VideoWriter_fourcc(*'MJPG'), 10, (600,600))

        if camera:
            print('[INFO] Opening Web Cam.')
            self.detectByCamera(writer)
        elif video_path is not None:
            print('[INFO] Opening Video from path.')
            self.detectByPathVideo(video_path, writer)
        elif image_path is not None:
            print('[INFO] Opening Image from path.')
            # self.detectByPathImage(image_path, args['output'])

    def detectByPathVideo(self, path, writer):

        video = cv2.VideoCapture(path)
        check, frame = video.read()
        if check == False:
            print('Video Not Found. Please Enter a Valid Path (Full path of Video Should be Provided).')
            return

        print('Detecting people...')
        while video.isOpened():
            #check is True if reading was successful
            check, frame =  video.read()

            if check:
                frame = imutils.resize(frame , width=min(800,frame.shape[1]))
                frame = self.detect(frame)

                if writer is not None:
                    writer.write(frame)

                key = cv2.waitKey(1)
                if key== ord('q'):
                    break
            else:
                break
        video.release()
        cv2.destroyAllWindows()

    def detectByCamera(self, writer):
        video = cv2.VideoCapture(0)
        print('Detecting people...')

        while True:
            check, frame = video.read()

            frame = self.detect(frame)
            if writer is not None:
                writer.write(frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                    break

        video.release()
        cv2.destroyAllWindows()

    def start(self):
        args = {
        'image': None,
        'video': "C:\\Users\\harsh.bagadia\\Downloads\\vid.mp4",
        'camera': "true",
        'output' : 'C:\\Users\\harsh.bagadia\\Downloads\\vid-output.mp4'
        }
        self.humanDetector(args)

    def openFileBrowse(self):
        self.inputFilePath = str(QFileDialog.getOpenFileName(self,
        "Open Image", "C:\\", "Image Files (*.png *.jpg *.bmp);; All files (*.*)"))
        self.inputFileLocationText.setText(self.inputFilePath.split(",")[0].replace("(", "").replace("'", "").strip())


    def __init__(self, parent=None):
        self.inputFilePath = None

        super().__init__(parent)
        self.loadUi();
        self.setWindowTitle("My App")

        self.imageRadioButton = self.findChild(QRadioButton, "imageRadioButton")
        self.videoRadioButton = self.findChild(QRadioButton, "videoRadioButton")
        self.cameraRadioButton = self.findChild(QRadioButton, "cameraRadioButton")
        self.inputBrowseButton = self.findChild(QPushButton, "inputBrowseButton")
        self.startButton = self.findChild(QPushButton, "startButton")
        self.inputFileLocationText = self.findChild(QLineEdit, "inputFileLocationText")

        self.startButton.setEnabled(True)
        self.startButton.clicked.connect(self.start)

        self.inputBrowseButton.clicked.connect(self.openFileBrowse)
        self.inputFileLocationText.setText(self.inputFilePath)

    def loadUi(self):
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "form.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
