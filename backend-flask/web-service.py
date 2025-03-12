from flask import Flask, request, jsonify
from flask_cors import CORS
from data import users, recipes, get_last_recipe_id, get_last_user_id

app = Flask(__name__)
CORS(app)


# ENDPOINTS - USERS
@app.get("/api/users")
def get_all_users():
    return jsonify(users)


@app.get("/api/users/<int:id_user>")
def get_single_user(id_user: int):
    user_found = [user for user in users if user["id_user"] == id_user]
    if user_found:
        return jsonify(user_found), 200
    return jsonify({"error": "User not found!"}), 404


@app.post("/api/users")
def post_user():
    if request.is_json:
        response = request.get_json()
        if (
            "name" not in response
            or "surname" not in response
            or "type" not in response
            or "profile_photo" not in response
        ):
            return jsonify({"error": "Missing fields!"}), 400
        response["id_user"] = get_last_user_id()
        users.append(response)
        return jsonify({"message": "User created successfully", "user": response}), 201
    return jsonify({"error": "Request must be JSON"}), 400


@app.put("/api/users/<int:id_user>")
def put_user(id_user: int):
    if request.is_json:
        user_found = [user for user in users if user["id_user"] == id_user]
        if user_found:
            user_found[0]["name"] = request.json.get("name") or user_found[0]["name"]
            user_found[0]["surname"] = request.json.get("surname") or user_found[0]["surname"]
            user_found[0]["type"] = request.json.get("type") or user_found[0]["type"]
            user_found[0]["profile_photo"] = request.json.get("profile_photo") or user_found[0]["profile_photo"]
            return jsonify({"message": "User updated successfully", "user": user_found[0]}), 200
        else:
            return jsonify({"error": "User not found!"}), 404
    return jsonify({"error": "Request must be JSON"}), 400


@app.delete("/api/users/<int:id_user>")
def delete_user(id_user: int):
    user_found = [user for user in users if user["id_user"] == id_user]
    if user_found:
        users.remove(user_found[0])
        return jsonify({"message": "User deleted successfully", "user": user_found[0]}), 200
    return jsonify({"error": "User not found!"}), 404


# ENDPOINTS - RECIPES
@app.get("/api/users/<int:id_user>/recipes")
def get_all_recipes_by_user(id_user: int):
    recipes_found = [recipe for recipe in recipes if recipe["id_user"] == id_user]
    if recipes_found:
        return jsonify(recipes_found), 200
    return jsonify({"error": "This user doesnt have recipes!"}), 404


@app.get("/api/users/<int:id_user>/recipes/<int:id_recipe>")
def get_single_recipe_by_user(id_user: int, id_recipe: int):
    recipe_found = [recipe for recipe in recipes if recipe["id_user"] == id_user and recipe["id_recipe"] == id_recipe]
    if recipe_found:
        return jsonify(recipe_found[0]), 200
    return jsonify({"error": "Recipe not found!"}), 404


@app.post("/api/users/<int:id_user>/recipes")
def post_recipe(id_user: int):
    if request.is_json:
        response = request.get_json()
        if "name" not in response or "ingredients" not in response or "instructions" not in response:
            return jsonify({"error": "Missing fields!"}), 400
        response["id_recipe"] = get_last_recipe_id()
        response["id_user"] = id_user
        recipes.append(response)
        return jsonify({"message": "Recipe created successfully", "recipe": response}), 201
    return jsonify({"error": "Request must be JSON"}), 400



@app.put("/api/users/<int:id_user>/recipes/<int:id_recipe>")
def put_recipe(id_user: int, id_recipe: int):
    if request.is_json:
        recipe_found = [recipe for recipe in recipes if recipe["id_user"] == id_user and recipe["id_recipe"] == id_recipe]
        if recipe_found:
            recipe = recipe_found[0]
            recipe["name"] = request.json.get("name") or recipe["name"]
            recipe["ingredients"] = request.json.get("ingredients") or recipe["ingredients"]
            recipe["instructions"] = request.json.get("instructions") or recipe["instructions"]
            return jsonify({"message": "Recipe updated successfully", "recipe": recipe}), 200
        else:
            return jsonify({"error": "Recipe not found!"}), 404
    return jsonify({"error": "Request must be JSON"}), 400



@app.delete("/api/users/<int:id_user>/recipes/<int:id_recipe>")
def delete_recipe(id_user: int, id_recipe: int):
    recipe_found = [
        recipe
        for recipe in recipes
        if recipe["id_user"] == id_user and recipe["id_recipe"] == id_recipe
    ]
    if recipe_found:
        recipes.remove(recipe_found[0])
        return jsonify({"message": "Recipe deleted successfully", "recipe": recipe_found[0]}), 200
    return jsonify({"error": "Recipe not found!"}), 404


if __name__ == "__main__":
    app.run(debug=True)