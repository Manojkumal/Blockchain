import pycurl
from io import BytesIO
import json

class RPC_Curl(object):
    def __init__(self, rpc_port):
        self.rpc_port = str(rpc_port)

    def retrive_file(self, ref_hash):
        response = {}
        data_buffer = BytesIO()
        crl = pycurl.Curl()

        crl.setopt(crl.URL, 'http://127.0.0.1:'+self.rpc_port+'/api/v0/cat?arg='+ref_hash)
        crl.setopt(crl.WRITEDATA, data_buffer)
        crl.setopt(crl.POST, 1)

        crl.perform()
        response['status'] = crl.getinfo(pycurl.HTTP_CODE)
        crl.close()

        response['results'] = data_buffer.getvalue()
        return response

    def save_file(self, file_name):
        response = {}
        body_buffer = BytesIO()
        crl = pycurl.Curl()

        crl.setopt(crl.URL, 'http://127.0.0.1:'+self.rpc_port+'/api/v0/add')
        crl.setopt(crl.POST, 1)
        crl.setopt(crl.HTTPPOST, [('data', (crl.FORM_FILE, file_name))])
        crl.setopt(crl.WRITEDATA, body_buffer)

        crl.perform()
        response['status'] = crl.getinfo(pycurl.HTTP_CODE)
        crl.close()

        # ✅ Fixed line: normal space
        response['results'] = body_buffer.getvalue().decode('utf8')
        return response


def test():
    rpc_curl = RPC_Curl(5001)

    file_name = 'Gossip_protocol.jpg'
    post_ret = rpc_curl.save_file(file_name)
    print(json.loads(post_ret['results']))

    receipt = json.loads(post_ret['results'])
    ref_hash = receipt['Hash']
    download_file = "dl_"+receipt['Name']

    file_content = rpc_curl.retrive_file(ref_hash)['results']

    with open(download_file, "wb") as f:
        f.write(file_content)


if __name__ == "__main__":
    test()

