import face_recognition

def run_recognition(file_name):
	yashin_image =  face_recognition.load_image_file("yashin2.jpg")
	unknown_image = face_recognition.load_image_file(file_name)
	try:
	    yashin_face_encoding = face_recognition.face_encodings(yashin_image)[0]
	    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
	except IndexError:
	    return ["No faces found!"]
	known_faces = [yashin_face_encoding]
	results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
	return results
