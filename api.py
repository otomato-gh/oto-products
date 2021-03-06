from eve import Eve
from eve_swagger import swagger, add_documentation

app = Eve()
app.register_blueprint(swagger)

# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': 'Otomato Products API',
    'version': '1.0',
    'description': 'store and retrieve products',
    'termsOfService': 'my terms of service',
    'contact': {
        'name': 'ant.weiss@gmail.com',
        'url': 'http://otomato.link'
    },
    'license': {
        'name': 'GPL',
        'url': 'https://github.com/antweiss/oto-products/blob/master/LICENSE',
    }
}

@app.route('/metrics')
def metrics():
  global count
  count+=1
  metrics = "random " + str(random.randint(1, 10))
  metrics += "\nhttp_requests_total " + str(count)
  metrics += "\noto_products_errors " + str(random.randint(1, 10))
  return Response(metrics, mimetype='text/plain')


if __name__ == '__main__':
	app.run(host='0.0.0.0')
