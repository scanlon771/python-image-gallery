import psycopg2
import json
from secrets import get_secret_image_gallery

def get_secret():
    jsonString = get_secret_image_gallery()
    return json.loads(jsonString)

def main():
	print(get_secret())

if __name__ == '__main__':
	main()
