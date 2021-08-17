from model.Connection import Connection
 
connect =  Connection()
# connect.writedata("vuletable")
val = input("Nhap version ban muon luu:")
print(val)
connect._createVersion(val)