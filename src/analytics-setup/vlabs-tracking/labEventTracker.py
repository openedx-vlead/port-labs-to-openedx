import os
import json
from flask import Flask
from flask import send_from_directory
from flask import request
from elasticsearch import Elasticsearch

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/<analytics>',methods= ['GET'])
def fetch_analytics(analytics):
    	data = request.data
    	fetch_data = name
    	data_list = fetch_data.split(",") 
    	data_dict = {}

    	data_dict["STUDENT_LONG_ID"] = data_list[0]
    	data_dict["COURSE_ID"] = data_list[1]
    	data_dict["DATE_OF_EXPERIMENT"] = data_list[2]	   
    	data_dict["TIME_OF_EXPERIMENT"] = data_list[3]
	data_dict["EXPERIMENT_NAME"] = data_list[4]
	data_dict["LAB_NAME"] = data_list[5]
	data_dict["IP_ADDRESS"] = request.environ.get('HTTP_X_REAL_IP',request.remote_addr)

    	#json_data = json.dumps(data_dict)
	try:
		es = Elasticsearch([{'host':'elk-stack.vlabs.ac.in', 'port':9200}])
		es.index(index="vlabs", doc_type="usage", body=data_dict)
	except Exception as e:
		print e
	
	#try:
  	#	fp = open("/home/ubuntu/vlabs-tracking/filename.json","a")
        # 	fp.write(json_data)
    	# 	fp.write("\n")
	#	fp.close()
    	#except Exception as e:
	#	return e

	return "Hello {}!".format(analytics) 

if __name__ == '__main__':
    app.run()


