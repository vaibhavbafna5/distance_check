import cv2
import sys

# distance from camera to face (inches)
known_distance = 24

# known width of face (going with average face width)
known_width = 6.5

GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

fonts = cv2.FONT_HERSHEY_COMPLEX

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def find_focal_length(measured_distance, real_width, ref_image_width):
    return (ref_image_width * measured_distance) / real_width

def calculate_distance(focal_length, real_face_width, frame_face_width):
    return (real_face_width * focal_length) / frame_face_width

def calculate_face_width_from_image(image):
    face_width = 0
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_image, 1.3, 5)

    print("faces: ", faces)

    for (x, y, h, w) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), GREEN, 2)
        face_width = w

    return face_width

if __name__ == "__main__":

    file_name = sys.argv[1]
    reference_img = cv2.imread(file_name)
    reference_image_face_width = calculate_face_width_from_image(reference_img)

    focal_length = find_focal_length(known_distance, known_width, reference_image_face_width)
    print("image_width: ", reference_image_face_width)
    print("focal_length: ", focal_length)

    # cap = cv2.VideoCapture(0)
    # while True:

    #     _, frame = cap.read()

    #     face_width_in_frame = calculate_face_width_from_image(frame)
    #     if face_width_in_frame:

    #         distance = calculate_distance(
    #             focal_length,
    #             known_width,
    #             face_width_in_frame
    #         )

    #         # draw line as background of text
    #         cv2.line(frame, (30, 30), (230, 30), RED, 32)
    #         cv2.line(frame, (30, 30), (230, 30), BLACK, 28)
    
    #         # Drawing Text on the screen
    #         cv2.putText(
    #             frame, 
    #             f"Distance: {round(distance/12,2)} FT.", 
    #             (30, 35), 
    #             fonts, 0.6, GREEN, 2
    #         )

    #     cv2.imshow("frame", frame)

    #     if cv2.waitKey(1) == ord("q"):
    #         break

    # cap.release()
    # cv2.destroyAllWindows()
