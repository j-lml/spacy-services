from displacy_service.server import APP, get_model

# Pre-load English model only, to save memory
model='es_core_news_md'
print("model:" + str(model))
print("loading....")

# get_model('en_core_web_sm')
# get_model('de')
get_model(model)
print("[ok]")


if __name__ == '__main__':
    from wsgiref import simple_server
    ip='0.0.0.0'
    port=7999
    httpd = simple_server.make_server(ip, port, APP)
    print("ip:" + ip)
    print("port:" + str(port))
    httpd.serve_forever()
