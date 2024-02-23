from base64 import b64encode,b64decode
import falcon

def encodedLinkTest(id,bigid,admission_account_id,school_id):
    return b64encode(f"{id}_{bigid}_{admission_account_id}_{school_id}".encode('ascii')).decode("ascii").replace('/','+')
    
def dencodedLinkTest(text):
    dataOnText= b64decode(text.replace('+','/').encode('ascii')).decode('ascii').split('_')
    return {
        'id':int(dataOnText[0]),
        'bigid':dataOnText[1],
        'admission_account_id':int(dataOnText[2]),
        'school_id':int(dataOnText[3])
    }



def basic_auth_test_id(func):
    def method_req(*args, **kwargs):
        data_user={}
        try:
            id_test = kwargs.get('test_id')
            if not id_test:
                raise Exception("id test invalid")
            data_user = dencodedLinkTest(id_test)
            kwargs.pop('test_id')
            if not 'id' in data_user or  not 'bigid' in data_user or not 'admission_account_id' in data_user or not 'school_id' in data_user:
                raise Exception("id test invalid")
        except Exception as e:
            print(e)
            raise falcon.HTTPUnauthorized(
                title='401 Unauthorized',
                description='Authorization Failed',
                challenges=None)
        kwargs.update({**kwargs,'data_user':data_user})
        func(*args, **kwargs)
        
    return method_req