# 0x11. Python - Network #1

## Overview
For this project, I learnt two python packages for sending requests to servers on the internet:
- urllib
- requests #requestsiswaysimplerthanurllib;)

## Tasks
- Task 0 - What's my status? #0

	- Description: Write a Python script that fetches https://alx-intranet.hbtn.io/status

	- Usage: ./0-hbtn_status.py
	
	- File: [0-hbtn_status.py](https://github.com/m-aishah/alx-higher_level_programming/blob/master/0x11-python-network_1/0-hbtn_status.py)


- Task 1 - Response header value #0

	- Description: Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

	- Usage: ./1-hbtn_header.py <URL>

	- File: [1-hbtn_header.py](https://github.com/m-aishah/alx-higher_level_programming/blob/master/0x11-python-network_1/1-hbtn_header.py)


- Task 2 - POST an email #0
	
	- Description: Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

	- Usage: ./2-post_email.py <URL> <email>

	- File: [2-post_email.py](https://github.com/m-aishah/alx-higher_level_programming/blob/master/0x11-python-network_1/2-post_email.py)


- Task 3 - Error code #0

	- Description: Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).

	- Usage: ./3-error_code.py <URL>

	- File: [3-error_code.py](https://github.com/m-aishah/alx-higher_level_programming/blob/master/0x11-python-network_1/3-error_code.py)


- Task 4 - What's my status? #1

	- Description: Write a Python script that fetches https://alx-intranet.hbtn.io/status

	- Usage: ./4-hbtn_status.py

	- File: [4-hbtn_status.py](https://github.com/m-aishah/alx-higher_level_programming/blob/master/0x11-python-network_1/4-hbtn_status.py)


- Task 5 - Response header value #1

	- Description: Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header.

	- Usage: ./5-hbtn_header.py <URL>

	- File: [5-hbtn_header.py](https://github.com/m-aishah/alx-higher_level_programming/blob/master/0x11-python-network_1/5-hbtn_header.py)


- Task 6 - POST an email #1

	- Description: Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

	- Usage: ./6-post_email.py <URL> <email>

	- File: [6-post_email.py](https://github.com/m-aishah/alx-higher_level_programming/blob/master/0x11-python-network_1/6-post_email.py)


- Task 7 - Error code #1

	- Description: Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response

	- Usage: ./7-error_code.py <URL>

	- File: [7-error_code.py](https://github.com/m-aishah/alx-higher_level_programming/blob/master/0x11-python-network_1/7-error_code.py)


- Task 8 - Search API

	- Description: Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

	- Usage: ./8-json_api.py [<letter>]

	- File: [8-json_api.py](https://github.com/m-aishah/alx-higher_level_programming/blob/master/0x11-python-network_1/8-json_api.py)


- Task 9 - My GitHub!

	- Dscription: Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id

	- Usage: ./10-my_github.py <username> <password>

	- File: [10-my_github.py](https://github.com/m-aishah/alx-higher_level_programming/blob/master/0x11-python-network_1/10-my_github.py)


- Task 10 - Time for an interview!

	- Description: The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:

'''bash
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
'''

	- Usage: ./100-github_commits.py <repository_name> <owner>

	- File 100-github_commits.py
