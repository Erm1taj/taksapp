db_link='postgres://admin:oocooSh7@postgres.host:5432/my_db'
db_link1='sqlite:///C:/Users/admin/site_db.sqlite3'

def parse_db_url(db_link):
	a=db_link.split(":")
	engine=a[0]
	if engine=="postgres":
		a=db_link.replace("//",'').replace("@",":").replace("/",":").split(":")
		return {"ENGINE":engine,"USER":a[1],"PASSWORD":a[2],"HOST":a[3],"PORT":a[4],"NAME":a[5]}
	if engine=="sqlite":
		a=db_link.replace(":///",'?').split("?")
		return {"ENGINE":engine,"NAME":a[1]}
	else:
		return ValueError
	
print(parse_db_url(db_link))
print(parse_db_url(db_link1))