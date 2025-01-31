from flask import Flask, request, jsonify, Blueprint

app = Flask(__name__)

learners = Blueprint("learners", __name__)

learners_list = []

@learners.route("/", methods=["GET"])
def get_learners():
    return jsonify(learners_list)

@learners.route("/", methods=["POST"])
def create_learner():
    learner = {
        "id": len(learners_list) + 1,
        "name": request.json.get("name"),
        "major": request.json.get("major"),
    }
    learners_list.append(learner)
    return jsonify(learners_list), 201

@learners.route("/<int:id>", methods=["PUT"])
def update_learner(id):
    learner = next((t for t in learners_list if t.get("id") == id), None)
    if learner is None:
        return jsonify({"error": "Learner not found"}), 404
    learner["name"] = request.json.get("name", learner["name"])
    learner["major"] = request.json.get("major", learner["major"])
    return jsonify(learner)

@learners.route("/<int:id>", methods=["DELETE"])
def delete_learner(id):
    global learners_list
    learner = next((t for t in learners_list if t.get("id") == id), None)
    if learner is None:
        return jsonify({"error": "Learner not found"}), 404
        
    learners_list = [t for t in learners_list if t.get("id") != id]
    return '', 204

@learners.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    learner = next((c for c in learners_list if c.get("id") == id), None)
    if learner:
        return jsonify(learner)
    return jsonify({"error": "Learner not found"}), 404

app.register_blueprint(learners, url_prefix="/learners")

if __name__ == "__main__":
    app.run(debug=True)
