import face_recognition
from PIL import Image, ImageDraw
import numpy as np
# 加载2张已知面孔的图片
known_student_1_image = face_recognition.load_image_file("students/1.jpg")
known_student_2_image = face_recognition.load_image_file("students/2.jpg")
known_student_3_image = face_recognition.load_image_file("students/3.jpg")
known_student_4_image = face_recognition.load_image_file("students/4.jpg")

# 计算图片对应的编码
student_face_1_encoding = face_recognition.face_encodings(known_student_1_image)[0]
student_face_2_encoding = face_recognition.face_encodings(known_student_2_image)[0]
student_face_3_encoding = face_recognition.face_encodings(known_student_3_image)[0]
student_face_4_encoding = face_recognition.face_encodings(known_student_4_image)[0]

known_face_encodings = [
    student_face_1_encoding,
    student_face_2_encoding,
    student_face_3_encoding,
    student_face_4_encoding
]
known_face_names = [
    "1",
    "2",
    "3",
    "4",
]

# 加载一张未知面孔的图片
unknown_image = face_recognition.load_image_file("class.jpg")
# 计算图片对应的编码
# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.4)
    print(matches)
    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    # if True in matches:
    #     first_match_index = matches.index(True)
    #     name = known_face_names[first_match_index]

    # Or instead, use the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    print(face_distances)
    best_match_index = np.argmin(face_distances)
    print(best_match_index)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
pil_image.show()