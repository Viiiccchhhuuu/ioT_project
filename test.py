import requests

BASE="http://127.0.0.1:5000/"

print("vichu is the best")
data=[{"likes":100, "name":"Vishakhavel's GNR covers","views":10000},
     {"likes":200, "name":"Slash's GNR covers","views":200000},
     {"likes":300, "name":"Vichu's GNR covers","views":200000000}]

#for i in range(len(data)):
 #   response=requests.put(BASE+"video/"+str(i), data[i])
    #print(response.json())

#after stall\\response=requests.put(BASE+"video/1", {"name" :"Sarkar", "views":1000,"likes"  :10})
#response=requests.delete(BASE+"video/1")           # NOTE THAT THE PROGRAM CRASHES IF THE VIDEO_ID IS NOT FOUND IN THE VIDEOS DICTIONARY.
#print(response)
#TO AVOID THIS , WE HAVE DEFINED A FUCNTION IN THE MAIN.PY TO ABORT IF VIDEO ID IS NOT FOUND.
#print(response.json())

#response=requests.delete(BASE+"video/1")
#print(response.json())


#response=requests.put(BASE+"video/3",data[2])
#print(response.json())

for i in range (0,3):
    response = requests.get(BASE + "video/"+str(i))
    print(response.json())






