

@todos.route("/",methods=["POST"])
def create_todo():
    list = {
        "id": len(listt)+1,
        "model" : request.json.get("model"),
        "available" : request.json.get("available",False),
    }