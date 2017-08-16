def handle_uploaded_file(f): 
	with open('media/image_upload/', 'wb+') as destination: 
		for chunk in f.chunks(): destination.write(chunk)
