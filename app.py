from flask import Flask,Response 
import codecs
app = Flask (__name__)

@app.route("/")
def index():
	rows = []
	def generate():
		with codecs.open('sample.csv','r','utf-8') as f:
			for row in f:
				rows.append(row)
	generate()
	return Response(stream_template('index.html',rows=rows))

def stream_template(template_name,**context):
	app.update_template_context(context)
	t = app.jinja_env.get_template(template_name)
	rv = t.stream(context)
	rv.enable_buffering(5)
	return rv

if __name__ == "__main__":
	app.run(debug=True,threaded=True,host='0.0.0.0')
