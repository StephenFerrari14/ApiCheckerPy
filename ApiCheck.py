import requests
import json
requests.packages.urllib3.disable_warnings()

with open('urls.txt') as f:
    content = f.read().splitlines()

open('out.txt', 'w').close()

#parse if its a post or get
didFail = False

x = 0;
while (x < len(content)):
#while (False):  
	#print (content[x])
	if "{" and "}" not in content[x]:
		#Not post
		print ("GET")
		response = requests.get(content[x])

		if(response.status_code != 200):
			didFail = True
		print('Response from ' + response.url)
		print('Status Code: ' + str(response.status_code))

		output = open('out.txt', 'a')
		output.write('Response from ' + response.url + '\n')
		output.write('Status Code: ' + str(response.status_code) + '\n')
		output.close();

	else:
		print ("POST")
		#post processing
		dataString = content[x]
		length = len(dataString)
		dataIndex = dataString.find("{")
		postUrl = dataString[0:dataIndex - 1]
		#print (postUrl)
		dataString = dataString[dataIndex:length]

		json_acceptable_string = dataString.replace("'", "\"") #Might not need this
		data = json.loads(json_acceptable_string)
		#print (dataString)
		response = requests.post(postUrl, data=data)

		if(response.status_code != 200):
			didFail = True

		print('Response from ' + response.url)
		print('Status Code: ' + str(response.status_code))

		output = open('out.txt', 'a')
		output.write('Response from ' + response.url + '\n')
		output.write('Status Code: ' + str(response.status_code) + '\n')
		output.close()


	#request comes with built in response code lookup
	#requests.codes.ok
	#Also this thing raise_for_status()
	#response.headers
	#response.cookies
	x = x + 1

if (didFail):
	print("One or more requests did not return a 200")
	output = open('out.txt', 'a')
	output.write('One or more requests did not return a 200\n')
	output.close()

