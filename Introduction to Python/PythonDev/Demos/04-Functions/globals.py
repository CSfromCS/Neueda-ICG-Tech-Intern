__DBNAME = None

def initDB(name):
  global __DBNAME  
  if __DBNAME is None: 
    __DBNAME = name
  else:
    raise RuntimeError("Database name has already been set.")

def queryDB():
  print("TODO, add code to query %s" % __DBNAME)

def updateDB():
  print("TODO, add code to update %s" % __DBNAME)


# Usage (i.e. client code)
initDB("Server=.;Database=Northwind")
queryDB()
updateDB()
