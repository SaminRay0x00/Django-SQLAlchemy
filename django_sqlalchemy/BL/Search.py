from sqlalchemy import create_engine

e = create_engine("mysql://root:@localhost/test?charset=utf8")

# e.execute("create table if not exists raminoooooooooo (name varchar(20))")
# e.execute("insert into raminoooooooooo (name) values (%s)", [u'رامین'])

query = u"""select * from raminoooooooooo where name like N'{}%%'""".format(u'رامین')
result = e.execute(query).fetchall()
for v in result:
    for column, value in v.items():
        print "%s" % value.encode("utf-8")
