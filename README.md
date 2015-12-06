# fynd
A tool which will help you to find a flat in a region of common interest.

##Auth backend apis

###Login
POST http://10.1.6.24:8000/auth/login_api
params: (x-www-form-urlencoded)
 username: rohit.laddha@housing.com
 password: housing

###Logout
GET http://10.1.6.24:8000/auth/logout

###sample url check
GET http://10.1.6.24:8000/auth/sample_view

##Auth frontend api
GET http://10.1.6.24:8000/auth/login

##Matching Apis
login required    
http://10.1.6.24:8000/match/get_intersection?size=1&lat1=19.107554&lon1=72.896517&range1=10&range_type1=time


