import { createWebHistory, createRouter } from "vue-router";

import UsersView from "../pages/UsersView.vue";
import RecipesView from "../pages/RecipesView.vue";
import SingleRecipeView from "../pages/SingleRecipeView.vue";

const routes = [
  { path: "/", component: UsersView },
  { path: "/:id_user/recipes", component: RecipesView },
  { path: "/:id_user/recipes/:id_recipe", component: SingleRecipeView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
