import json
from cPickle import Unpickler
import requests
import pickle
import pandas as pd
import numpy as np
from flask import Flask
from flask import request
from jinja2 import Template 
from flask import session, g, redirect, url_for, abort, render_template, flash
import pdb
import pymongo

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world'

# @app.route('/predictquote' , methods=['POST'])
# def predictQuote():
#  	print "Predicting Quote Conversion"


# 	test_frame = pd.DataFrame([request.json])#pd.read_json(j)
# 	expected_features = ['body_length','channels','delivery_method','fb_published','gts','has_analytics','has_header','has_logo','num_order','num_payouts','org_facebook','org_twitter','sale_duration','show_map','uid','user_age','user_type']
# 	input_features = test_frame.columns
# 	selected_features = [ item for item in input_features if item in expected_features ]
# 	test_features = test_frame[selected_features]

# 	#test_features = test_frame[['body_length','channels','delivery_method','fb_published','gts','has_analytics','has_header','has_logo','num_order','num_payouts','org_facebook','org_twitter','sale_duration','show_map','uid','user_age','user_type']]
# 	test_num =  test_features.fillna(test_features.mean())
# 	test_final = np.array(test_num)

# 	data_proba_pred = model.predict_proba(test_final)

# 	# DB query to insert prediction
# 	# insert into transactions (uid, fraud_class) values (0123, 'review');

# 	cursor = conn.cursor()
# 	test_frame_columns = test_frame.columns
# 	#this_uid, this_fraud_class,this_org_name,this_ip,this_device_id,this_email_domain,this_country,this_currency,this_venue_name,this_name,this_noa,this_payout_type = ""

	


# 	#pdb.set_trace()
# 	# write to database


# 	cursor.execute("INSERT INTO customer_quotes (org_name, ip, device_id, email_domain, country, currency, venue_name, name, noa, payout_type,fraud_class) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)", (this_org_name,this_ip,this_device_id,this_email_domain,this_country,this_currency,this_venue_name,this_name,this_noa,this_payout_type,this_class))
# 	conn.commit()
# 	return


# @app.route('/dashboard', methods=['GET'])
# def dashboard():
#     # show the post with the given id, the id is an integer
#     # select uid,fraud_class from transactions
#     cursor = conn.cursor()
#     cursor.execute("SELECT customer_id,datetime from customer_quotes")
#     resultset = cursor.fetchall()
#     print resultset
#     print type(resultset)
#     #pdb.set_trace()
#     orglist = []
#     statuslist = []
#     for record in resultset:
#     	(org,status) = record
#     	orglist.append(org)
#     	statuslist.append(status)

#     #data = sorted(, key=lambda record: record[0][1], reverse=True)

#     #htmlcode = html.table(resultset)
#     #print htmlcode
    
#     #return render_template('data.html', data=resultset)
#     #return htmlcode

#     return 'account_status: %s' % statuslist


if __name__ == "__main__":
	# model = Unpickler('fraud_model') # unpickle the model
	#model = pickle.load( open( 'fraud_model2', 'rb') )
	# conn_string = "host='localhost' dbname='customer360'"
	# conn = psycopg2.connect(conn_string)
	# cursor = conn.cursor()

	app.debug = True
	app.run(host = '0.0.0.0')
