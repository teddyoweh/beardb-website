import requests
class BeardbConfig:
    
    def __init__(self):
        self.email ='teddy@teddyoweh.net' 
        self.baseurl = 'http://127.0.0.1:5000/'
        self.secret ='b867dd6ef191065c8725f8b69e6f54a6d83eb07dac538b3bd35482fdbf1d6b04'
        self.data = self.return_me()
        self.project = self.data['projects']
        self.buckets = self.data['buckets']
        self.createdat = self.data['created']
        self.fullnamme= self.data['fullname']
        self.secretKey = self.data['secretKey']
        self.email = self.data['email']
        self.id = self.data['id']
          
    def return_me(self):
        url = self.baseurl + '/me'
        data = {'email':self.email,'secret':self.secret} 
        r = requests.post(url,data)
        return r.json()['data']
        
    def new_project(self,project):
        url= self.baseurl+'/newproject'
        data ={
            'secret':self.secret,
            'email':self.email,
            'project':project}
        response = requests.post(url,data=data)
        return response.json()
    def new_database(self,project,database):
        url = self.baseurl+'/newdatabase'
        data ={
            'secret':self.secret,
            'email':self.email,
            'project':project,
            'database':database}
        response = requests.post(url,data=data)
    def new_bucket(self,project,database,bucket):
        url = self.baseurl+'/newbucket'
        data ={
            'secret':self.secret,
            'email':self.email,
            'project':project,
            'database':database,
            }
        response = requests.post(url,data=data)
        return response.json()
    def insert_data(self,project,database,bucket,data):
        url = self.baseurl+'/insertdata'
        data ={
            'secret':self.secret,
            'email':self.email,
            'project':project,
            'database':database,
            'data':data
            }
        response = requests.post(url,data=data)
        return response.json()
    def update_data(self,project,database,bucket,data,query):
        url = self.baseurl+'/updatedata'
        data ={
            'secret':self.secret,
            'email':self.email,
            'project':project,
            'database':database,
            'data':data,
            'query':query
            }
        response = requests.post(url,data=data)
        return response.json()
    def updatedatabyid(self,project,database,bucket,data,id):
        url = self.baseurl+'/updatedatabyid'
        data ={
            'secret':self.secret,
            'email':self.email,
            'project':project,
            'database':database,
            'data':data,
            'id':id
            }
        response = requests.post(url,data=data)
        return response.json()
    def fetchdata(self,project,database,bucket,query={}):
        url = self.baseurl+'/fetchdata'
        data ={
            'secret':self.secret,
            'email':self.email,
            'project':project,
            'database':database,
            'bucket':bucket,
            'data':query
            
            }
        response = requests.post(url,data=data)
        return response.json()
    def return_projects(self):
        return self.data['projects']
        
    
        
        

config = BeardbConfig()
print(config.return_me())
# print(config.fetchdata('website','users','users'))