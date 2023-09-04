
from wsgiref.simple_server import WSGIServer
import gevent.pywsgi

import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['GET'])
def upload_file():

    url = "https://ivr-calling-data-dev.s3.amazonaws.com/1a7fb06a-4813-11ee-a810-e68c095a7d26/Aetna_bulk.xlsx?AWSAccessKeyId=ASIA4JPVH5SVJBOQ2PMD&Signature=BbYXNn20rvdTHuYuvSLPh%2B5nalE%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBAaCXVzLWVhc3QtMSJIMEYCIQCa%2FUuU0Txv%2Fk7bSBeG3KgQmPchuFoG4QSWmFtKLpKyqQIhAMbc9nc48GmMUfe935l58g1oL3TYSWfhJh0tszubTerBKp4DCNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMODQ1MDEyMjY2MTU0IgxAbIXMtJiysv5WxC0q8gLiu8fHyvuDa0Gz1L6G2lro4Q6xhpWcQypS10Ix%2FRNbtYYxerlNLU%2BW29LG8rEVjNqA6iSYCb%2F%2FIEjhzx62t3YDMVo%2BQf5%2FHPkOTl31Wco%2FV4jSNB%2FzmTN5zh%2FgdSCM62gluDqWK4F9zWRDKOYiDVVl%2BQRi%2BTEbM6GcPmb8BMSAEb0TlVny0fKXSfwiEYxu9Y5eCeh2RmT9mAnAGwWwfCvCO5g5w0LIYnaplE4CBJESHKyWkFslNVhfzg6yFCvfJgEGXoUNHEtWuHJcgT%2FR%2BSzhbZQqwguq9SadLLM5HWdBJq4MNKtV69JxicIKUL9EnHo1%2FpJUNjxZ%2BbmX7MfaHrdODwc8jM%2BhMvqtvPyoupVlye1eWMtOQ8mR7OIGqVP0VvYSWcwwDYzJ6uoG1jsUvcpfiQ%2BaXrVG3H%2BGY8MmhfVXQUTcUdIau%2Bm06iEpKcSJeEabWiL0wVI0eSCNOS6c09L14DY9vETAjxQvqhMlUhPf%2F%2B%2BzMLXjwqcGOpwBPQMEX9zlcOef7XexuEyWuDHmZ54mCmLnN4Jb3YZCL9oEiBVgyZp0XrmHKaaAWYFQcc3MORhnQY3lygB2cQkSmy8NNGwvWHI9fLv9yTkYYs9kg6NPypPB5BC2M0IxE6bZOiduhKwHnm4NzH58%2BS%2FcFD0lkVfmOAdB9C35TMumwx7wSBpiFVg7ikDrtcbt4tGhBkxmibuHhM3z1wNa&Expires=1693496638"
    # headers = {
    #     'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    # }

    url_param = request.args.get('Presign')
    file_param = request.args.get('file_param')

    if not url_param:
        return "URL parameter is missing", 400

    if not file_param:
        return "File parameter is missing", 400

    print("URL Parameter2:", url_param)
    print("File Parameter2:", file_param)

    # url_params = requests.get(url_param)
    file_path = f'/Users/K Adarsh Kumar/Documents/{file_param}'
    with open(file_path, 'rb') as file:
      print(file_path,'file path')
      print(file,"file")
      if file:
          print("URL Parameter2:", url_param)
          response = requests.put(url_param, data=file)
          print("URL Parameter2:", url_param)
          print(response.text,"res text")
          if response.status_code == 200:
            return "File upload successful"
          else:
                return f"File upload failed with status code: {response.status_code}"

      else:
        return "No file received"


    return "Parameters received and processed successfully"

if __name__ == '__main__':
    # from waitress import serve
    # serve(app,host='192.168.100.21', port=8080)
    # http_server = gevent.pywsgi.WSGIServer(("192.168.100.21", 8080), app)
    # http_server.serve_forever()
    app.run()



# import requests
# url = "https://ivr-calling-data-dev.s3.amazonaws.com/02c3e934-48c0-11ee-86ed-0e39fb4a71d8/Aetna_bulk.xlsx?AWSAccessKeyId=ASIA4JPVH5SVIW2B7DGI&Signature=Ox1vl8y4P1OAUwkWesKznjz4f%2B4%3D&x-amz-security-token=IQoJb3JpZ2luX2VjECQaCXVzLWVhc3QtMSJHMEUCIQDGMoMrhxASVy1wDn%2BvP4P1esBsn6%2BjN6AmLV8ZbWP9VAIgUfIpua4wY7NuOvpMXCiKMedm0mvbtajFqWzeDvFxA%2B8qngMI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw4NDUwMTIyNjYxNTQiDEqIgc12vfZ4TiQEzCryAvZTYtMxdQm1bidZK555jru2XWfBHQaTUJWv7i%2FYcbXwcbV%2FgaT52uEi7AEQcsMpEl3%2B0nBYuqVnxWyrVcb05H2I3tREuXDi0U%2FBbI9MW851EX%2Fys4PGucaPa7VNN5fyPwiQ95MUKLfz4JmFjmqnrvYk%2FbAeLamdRuFkDsADx03XMelLFKtWntExH3TBO4OMh5mJDbINC4z2dv5%2B6fo2Zlt4rjasS4iQjuH26RJZ4kDdZoD7k72WBUYK%2BSn5JV%2FfeRJkCloOTkUdH3aM0p5TKyIfRUov0BY6M4mfGNSnG%2B9iUbFm8XnLa%2FO77fIhSTgfondRqoaWOhLgZphfvgpIK47JVLzRspFIlkEGkoEyP5lnO2xfS285PKdcMc1CE19QTI6jluroGCxFDBbOMxvp%2Fp7aCDjb1xUoCS%2FQtNNmjd4XK3B%2Fhx1EHp0ciuCFamj3DdvBF65kIxA7nzXb3fg%2BlkvfOuLgAsB3ykgCuUAsPP9fHbcw0qHHpwY6nQFSBJkI1QAuaS5JadODijX3%2FdHDVPMYobOT1LcwyFzwvU4R2J4bBUBqri98VIdZqafr0JY9eEcHlCDdDwQ1yaJAUkOAzfBwMAE5qOeLQtudzodeptzO8bDbWXt%2BEqhFVa1%2FBaHrHEiZprMmDjLmTxSPfKayL%2B6CitAet3%2F2%2BpSDDMaf8PaSjGacwMWJxfKXgxpu%2FBhzQsIE1ApAK2Rb&Expires=1693570901"
# # url = "https://ivr-calling-data-dev.s3.amazonaws.com/10c90408-4805-11ee-a72d-46b429718f73/Aetna_bulk.xlsx?AWSAccessKeyId=ASIA4JPVH5SVFQWSSO6U&Signature=WdOKyZbdbnEVQPrMBfPGa4tbJPk%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEA4aCXVzLWVhc3QtMSJGMEQCIG4bTc2LCcrlWyTwyb8K2K7zScOFC4LZQ2eN9697EnLJAiAQE3Zv3jV%2FrQM5YVd9OL8olKIG7Nf5M08D%2ByzDneVxGCqeAwjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDg0NTAxMjI2NjE1NCIMiAtqBnsm5OYwz93sKvICVbUWEIavrk7QDeKFDXoomniolPlxJ%2FPW45WPCg4fWwsnAANYntiXomMpgHC1ojzaUOTg5VEL83bipnGTtjsdr%2B6rsNAjBwsEij6JRSzgakA%2FD8wo%2FIDbiUDtyMRRwShFbMukVNEk4Cg28egW76Etkp%2F61d1fncc9OMWSgdnSkiR1lEFZz737qXChGLe%2Bx%2F4FNS%2FUYf6H3B2weO3QpH89KQ55nwDsREuKkAPStx%2BZZ%2BTBpcJk9GyR5gdUasXgjYCMpQV4wunk7%2Bou%2Bp%2FOthjnesDrgCfXKCfmHuJzon92YO6w692YmuRIcNUpefS2QSXVEKzml9IXp0CqsBGaASXv%2BjotBDlQ80qiUQGwY1foa6CAamd1k1SuTL8sc19Jbw7rE%2BbrtpzAc%2FHYbQp5%2Ft5WSVMYknC%2BSGv5auVI26iY5pcdK8z15z4rZbTsXWLUmQFjDLQ10roSKN9LGQo8VFsingbKGi2h%2BBfdXlrBrpRXeLyJpzCotMKnBjqeAQw%2F7SfDCIpidnRPvjskkKDgwseVRObt1U1qKydvq9UFNQx8QDnC0Ua2nt%2FdjR0q8cztZs1%2BE%2BuKDXh6Y5wBSebvwZiMFUDtVDPA2YEpP0Q7so4Zyvy75E2I1DtNpuF8lSP4m4ocRs3UL3FgT8n%2BNWryY2HWBY740uxWHiCE4A2%2FPaYGwmzjnWFyhoEnqqgrQl6uYDnL%2BMuJhLREz64W&Expires=1693490609"
# print("start")
#
# with open('/Users/K Adarsh Kumar/Documents/Aetna_bulk.xlsx', 'rb') as f:
#     r = requests.put(url, data=f)
#
#     print(f)
#     print("Done")