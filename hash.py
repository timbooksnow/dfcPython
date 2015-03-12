import hashlib, zlib, csv, os, sys

hashFileName = str(sys.argv[1])
directoryToHash = str(sys.argv[2])

def filename_hasher(subdir, file_name):
	full_path = subdir + '/' + file_name
	temp_list = []
	temp_list.append(file_name)
	temp_list.append(os.path.abspath(full_path))
	temp_list.append(hash_file(full_path, hashlib.md5()))
	temp_list.append(hash_file(full_path, hashlib.sha1()))
	temp_list.append(hash_file(full_path, hashlib.sha224()))
	temp_list.append(hash_file(full_path, hashlib.sha256()))
	temp_list.append(hash_file(full_path, hashlib.sha384()))
	temp_list.append(hash_file(full_path, hashlib.sha512()))
	return temp_list


def hash_file(file_name, _type):
	BUFFER_SIZE = 64 * 1024 #Read 64k at a time to save memory
	hash_type = _type
	with open(file_name, 'rb') as f:
		buffer_s = f.read(BUFFER_SIZE)
		while len(buffer_s) > 0:
			hash_type.update(buffer_s)
			buffer_s = f.read(BUFFER_SIZE)

	hash_in_hex = hash_type.hexdigest()
	
	return hash_in_hex
	
print os.getcwd() #show current dir
temp_list = []

rootdir = '/Users/MikeO/Desktop/Hasher/' # Dir path
lindir = '/home/beast/hash' # Linux dir 
windir = 'C:\\Users\\timbooks\\Desktop\\HasherTestArea' # Dir path on a windows machine

#toHashDirectory = windir

for subdir, dirs, files in os.walk(directoryToHash):
    for file in files:
        temp_list.append(filename_hasher(subdir, file))
      

column_header = ['Filename','Path','MD5','SHA1','SHA224','SHA256','SHA384','SHA512']

#with open('hashes'+ '.csv', 'wb') as csvfile:
with open(hashFileName+ '.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([column_header])
    writer.writerows(temp_list)
