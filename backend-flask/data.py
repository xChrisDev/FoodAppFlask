users = [
    {
        "id_user": 1,
        "name": "Kane",
        "surname": "Johnson",
        "type": "Head Chef",
        "profile_photo": "https://randomuser.me/api/portraits/men/43.jpg",
    },
    {
        "id_user": 2,
        "name": "Arthur",
        "surname": "Hendricks",
        "type": "Sous Chef",
        "profile_photo": "https://randomuser.me/api/portraits/men/85.jpg",
    },
    {
        "id_user": 3,
        "name": "Sam",
        "surname": "Altman",
        "type": "Pastry Chef",
        "profile_photo": "https://randomuser.me/api/portraits/men/76.jpg",
    },
    {
        "id_user": 4,
        "name": "Jeremy",
        "surname": "Stuart",
        "type": "Line Cook",
        "profile_photo": "https://randomuser.me/api/portraits/men/51.jpg",
    },
    {
        "id_user": 5,
        "name": "Jared",
        "surname": "Thompson",
        "type": "Commis Chef",
        "profile_photo": "https://randomuser.me/api/portraits/men/78.jpg",
    },
]

recipes = [
    {
        "id_recipe": 1,
        "id_user": 1,
        "title": "Classic Beef Wellington",
        "steps": "To prepare the Classic Beef Wellington, start by seasoning a beef fillet with salt and pepper. Sear it in a hot pan with oil until it’s beautifully browned on all sides. Once seared, brush the beef with mustard and let it cool. Next, lay out plastic wrap and arrange slices of prosciutto on it, slightly overlapping. Spread a layer of mushroom duxelles over the prosciutto, then place the beef in the center. Wrap it tightly using the plastic wrap and chill in the fridge for about 15 minutes. Roll out puff pastry, wrap the beef tightly, and seal the edges. Brush the pastry with egg wash and bake at 400°F (200°C) for 20-25 minutes until golden brown. Let it rest before slicing and serving.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Beef_Wellington_2019.jpg/640px-Beef_Wellington_2019.jpg",
    },
    {
        "id_recipe": 2,
        "id_user": 1,
        "title": "Signature Homemade Sauce",
        "steps": "For the Signature Homemade Sauce, heat olive oil in a saucepan over medium heat. Add finely chopped onions and garlic, sautéing until they turn translucent. Stir in tomato paste and let it cook for a couple of minutes. Next, add crushed tomatoes, salt, pepper, and a pinch of sugar to balance the acidity. Let the sauce simmer for 20-30 minutes, stirring occasionally. Finish by adding fresh basil leaves and adjusting the seasoning to taste. You can blend the sauce for a smooth texture or leave it chunky, depending on your preference.",
        "image": "https://www.budgetbytes.com/wp-content/uploads/2017/06/Thick-Rich-Pizza-Sauce-finished-1200-500x500.jpg",
    },
    {
        "id_recipe": 3,
        "id_user": 2,
        "title": "Creamy Italian Risotto",
        "steps": "To make Creamy Italian Risotto, start by heating chicken or vegetable broth in a pot and keeping it warm. In a separate pan, sauté finely chopped onions in butter until they’re soft and fragrant. Add Arborio rice and toast it for a few minutes to enhance its nutty flavor. Pour in a splash of white wine and stir until it’s absorbed. Gradually add warm broth, one ladle at a time, stirring constantly until the liquid is absorbed before adding more. Continue this process until the rice is creamy and cooked al dente. Finish by stirring in grated Parmesan cheese and a bit of butter for richness. Season with salt and pepper, and garnish with fresh herbs before serving.",
        "image": "https://hips.hearstapps.com/hmg-prod/images/del089923-risotto-web-001-ab-index-64e7a1083b54e.jpg?crop=0.8888888888888888xw:1xh;center,top&resize=1200:*",
    },
    {
        "id_recipe": 4,
        "id_user": 2,
        "title": "Grilled Salmon Perfection",
        "steps": "For Grilled Salmon Perfection, preheat your grill to medium-high heat. Season the salmon fillets with salt, pepper, and a drizzle of olive oil. Place the salmon skin-side down on the grill and cook for about 4-5 minutes. Carefully flip the fillets and grill for another 3-4 minutes until the salmon is cooked through and flakes easily with a fork. Serve with a squeeze of fresh lemon juice and a sprinkle of fresh dill for a bright, flavorful finish.",
        "image": "https://mowi-salmon.es/wp-content/uploads/sites/4/2022/05/natural-line-C.jpg",
    },
    {
        "id_recipe": 5,
        "id_user": 2,
        "title": "Authentic Seafood Paella",
        "steps": "To prepare Authentic Seafood Paella, heat olive oil in a large paella pan. Sauté chopped onions, garlic, and bell peppers until they’re soft and aromatic. Add diced tomatoes and cook until the mixture reduces slightly. Stir in short-grain rice and toast it for a couple of minutes to enhance its flavor. Add saffron, smoked paprika, and hot broth, then arrange shrimp, mussels, and clams on top. Let the paella simmer without stirring until the rice is cooked and the seafood is perfectly done. Garnish with lemon wedges and fresh parsley before serving.",
        "image": "https://assets.surlatable.com/m/3d3d33b2b4ace4a/72_dpi_webp-slt_REC-266406_1606888_15U_0914.jpg",
    },
    {
        "id_recipe": 6,
        "id_user": 3,
        "title": "Decadent Chocolate Cake",
        "steps": "For the Decadent Chocolate Cake, preheat your oven to 350°F (175°C) and grease a cake pan. In a bowl, mix together flour, sugar, cocoa powder, baking powder, and salt. Add eggs, milk, oil, and vanilla extract, and mix until the batter is smooth. Stir in boiling water to thin the batter slightly, then pour it into the prepared pan. Bake for 30-35 minutes until a toothpick inserted into the center comes out clean. Let the cake cool completely before frosting it with a rich chocolate ganache.",
        "image": "https://grandcafecapecod.com/wp-content/uploads/2024/01/best-chocolate-cake-recipe-from-scratch-8-500x500-1.jpg",
    },
    {
        "id_recipe": 7,
        "id_user": 3,
        "title": "Flaky French Croissants",
        "steps": "To make Flaky French Croissants, start by mixing flour, sugar, salt, yeast, and milk to form a dough. Knead the dough until it’s smooth and let it rise for about an hour. Roll out the dough and place a layer of butter in the center. Fold the dough into thirds and chill it for 30 minutes. Repeat the rolling and folding process 3-4 times to create layers. Roll out the dough, cut it into triangles, and roll each triangle into a croissant shape. Let the croissants rise for 1-2 hours, then brush them with egg wash and bake at 375°F (190°C) for 15-20 minutes until golden and flaky.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/2018_01_Croissant_IMG_0685.JPG/640px-2018_01_Croissant_IMG_0685.JPG",
    },
    {
        "id_recipe": 8,
        "id_user": 3,
        "title": "Classic Vanilla Soufflé",
        "steps": "For the Classic Vanilla Soufflé, preheat your oven to 375°F (190°C) and butter your ramekins. Make a roux by melting butter and whisking in flour, then gradually add warm milk to create a smooth base. Stir in sugar, vanilla extract, and egg yolks. In a separate bowl, beat egg whites until stiff peaks form, then gently fold them into the yolk mixture. Pour the batter into the prepared ramekins, smooth the tops, and bake for 15-18 minutes until the soufflés are puffed and golden. Serve immediately for the best results.",
        "image": "https://www.allysongofton.co.nz/content/recipes/1959.jpg?width=320&height=479&fit=bounds",
    },
    {
        "id_recipe": 9,
        "id_user": 4,
        "title": "Sautéed Mixed Vegetables",
        "steps": "To prepare Sautéed Mixed Vegetables, heat olive oil in a large skillet. Add chopped carrots, zucchini, bell peppers, and broccoli, and sauté them for 5-7 minutes until they’re tender but still crisp. Season with salt, pepper, and a bit of garlic powder for extra flavor. For a finishing touch, add a splash of soy sauce or lemon juice and toss in some fresh herbs before serving.",
        "image": "https://www.recipevibes.com/wp-content/uploads/2020/04/sauteed-vegetables.jpeg",
    },
    {
        "id_recipe": 10,
        "id_user": 4,
        "title": "Juicy Grilled Chicken Breast",
        "steps": "For Juicy Grilled Chicken Breast, preheat your grill to medium-high heat. Season the chicken breasts with salt, pepper, and your favorite spices, then drizzle them with olive oil. Place the chicken on the grill and cook for about 6-7 minutes per side, or until the internal temperature reaches 165°F (74°C). Let the chicken rest for 5 minutes before slicing to ensure it stays juicy and flavorful.",
        "image": "https://images.immediate.co.uk/production/volatile/sites/30/2013/05/Garlic_chicken-3f62fd9.jpg?quality=90&resize=556,505",
    },
    {
        "id_recipe": 11,
        "id_user": 4,
        "title": "Creamy Mashed Potatoes",
        "steps": "To make Creamy Mashed Potatoes, start by peeling and chopping potatoes into even pieces. Boil them in salted water until they’re tender, then drain and return them to the pot. Add butter, milk, salt, and pepper, and mash everything together until the potatoes are smooth and creamy. Adjust the seasoning to taste and serve warm for a comforting side dish.",
        "image": "https://www.spendwithpennies.com/wp-content/uploads/2021/09/The-Best-Mashed-Potatoes-SpendWithPennies-6.jpg",
    },
    {
        "id_recipe": 12,
        "id_user": 4,
        "title": "Traditional French Ratatouille",
        "steps": "For Traditional French Ratatouille, heat olive oil in a large pot and sauté chopped onions and garlic until they’re soft and fragrant. Add diced eggplant, zucchini, bell peppers, and tomatoes, and season with salt, pepper, and herbs de Provence. Let the mixture simmer for 30-40 minutes until the vegetables are tender and the flavors have melded together. Serve warm or at room temperature for a delicious and hearty dish.",
        "image": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjzKtZ8V2SOlAKIKUbOpXVa_8fPdgMGrMXJViWZxKraj-rte2Rb8L2uUSrnQqJE3pn89aay4Z6bwghIPqpMc7Jkla76sLVexbel8Rdwd7oEpaJ0GLSg41XM42-tohf9uqZLUgWkCvOVkw/s1600/000767db.JPG",
    },
    {
        "id_recipe": 13,
        "id_user": 4,
        "title": "Homemade Caesar Dressing",
        "steps": "To make Homemade Caesar Dressing, combine garlic, anchovies, Dijon mustard, and egg yolks in a blender and blend until smooth. Slowly drizzle in olive oil while blending to create a creamy emulsion. Add lemon juice, Worcestershire sauce, and grated Parmesan cheese, then season with salt and pepper. Store the dressing in the fridge until you’re ready to use it, and give it a good shake before serving.",
        "image": "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/perfect-caesar-salad-b18f1cb.jpg",
    },
    {
        "id_recipe": 14,
        "id_user": 5,
        "title": "Basic Tomato Sauce",
        "steps": "For Basic Tomato Sauce, heat olive oil in a saucepan and sauté chopped onions and garlic until they’re soft and translucent. Add crushed tomatoes, salt, pepper, and a pinch of sugar to balance the acidity. Let the sauce simmer for 20-30 minutes, stirring occasionally. Finish by stirring in fresh basil and adjusting the seasoning to taste. Use the sauce immediately or store it for later use.",
        "image": "https://www.budgetbytes.com/wp-content/uploads/2017/06/Thick-Rich-Pizza-Sauce-finished-1200-500x500.jpg",
    },
    {
        "id_recipe": 15,
        "id_user": 5,
        "title": "Fluffy Scrambled Eggs",
        "steps": "To make Fluffy Scrambled Eggs, whisk eggs in a bowl with a splash of milk, salt, and pepper. Heat butter in a non-stick pan over medium-low heat and pour in the eggs. Let them sit for a few seconds, then gently stir with a spatula until soft curds form. Remove the eggs from the heat while they’re still slightly runny, as they’ll continue to cook from residual heat. Serve immediately for the best texture.",
        "image": "https://www.southernliving.com/thmb/9BsC4qqnQEuKi8iqKTf7w85Xwgs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-1367022810-29ae41d562df4161bc2039b8bf2d2eff.jpg",
    },
    {
        "id_recipe": 16,
        "id_user": 5,
        "title": "Perfect Al Dente Pasta",
        "steps": "For Perfect Al Dente Pasta, bring a large pot of salted water to a boil. Add the pasta and stir occasionally to prevent sticking. Cook according to the package instructions until the pasta is al dente. Reserve a cup of the pasta water, then drain the pasta. Toss it with your favorite sauce, adding a splash of pasta water if needed to create a silky texture. Serve immediately for the best flavor and texture.",
        "image": "https://escueladegastronomíaae.com/wp-content/uploads/2024/09/3-27.png",
    },
    {
        "id_recipe": 17,
        "id_user": 5,
        "title": "Simple Homemade Vinaigrette",
        "steps": "To make Simple Homemade Vinaigrette, combine olive oil, vinegar, Dijon mustard, and honey in a jar. Add salt, pepper, and minced garlic, then shake the jar vigorously until the mixture is well emulsified. Taste and adjust the seasoning as needed. Store the vinaigrette in the fridge and give it a good shake before using it to dress your favorite salads.",
        "image": "https://images.squarespace-cdn.com/content/v1/64eff5bff72bae08d5a67103/70dbe399-fe29-4786-9154-b9a634ee445b/_MG_4681.jpg",
    },
]


def get_last_user_id():
    return users[-1]["id_user"] + 1

def get_last_recipe_id():
    return recipes[-1]["id_recipe"] + 1
