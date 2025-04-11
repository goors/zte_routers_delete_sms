import requests
import json
import base64

# URL to fetch SMS data
url = 'http://192.168.0.1/goform/goform_get_cmd_process?isTest=false&cmd=sms_data_total&page=0&data_per_page=500&mem_store=1&tags=10&order_by=order+by+id+desc'

# Initialize session
s = requests.Session()
s.headers.update({'Host': '192.168.0.1'})
s.headers.update({'Referer': 'http://192.168.0.1/index.html'})

# Get SMS data
r = s.get(url)
t = r.text
t = t.replace('""31321""','"31321"')  # Clean the response
j = json.loads(t)

# Print the list of SMS messages
for m in j['messages']:
    print(m['id'] + " (" + m['number'] + "):")
    try:
        print(base64.b16decode(m['content']).decode('iso-8859-1').encode('utf-8'))
    except Exception as e:
        print("Error decoding content:", e)
    print("\n")

# Get user input for deleting a message
id = input("Delete SMS id: ")
if id != '':
    id = input("Again: delete SMS id: ")

# If an ID is provided, send the delete request
if id != '':
    url = 'http://192.168.0.1/goform/goform_set_cmd_process'
    payload = {'isTest': 'false', 'goformId': 'DELETE_SMS', 'msg_id': id, 'notCallback': 'true'}
    s.post(url, data=payload)
    print(f"Message with ID {id} deleted.")
  
