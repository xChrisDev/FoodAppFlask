<script setup>
import { onMounted, ref } from 'vue';
import RecipeCard from '../components/RecipeCard.vue';
import { getAllRecipesByUser } from '../api/recipes';
import { useRoute } from 'vue-router';
import { getUserById } from '../api/users';

const route = useRoute();
const id_user = route.params.id_user;

const user = ref(null);
const recipes = ref([]);
const loading = ref(true);

const fetchUserAndRecipes = async () => {
    try {
        user.value = await getUserById(id_user);
        recipes.value = await getAllRecipesByUser(id_user);
    } catch (error) {
        console.error('Error fetching data:', error);
    } finally {
        loading.value = false; 
    }
}

onMounted(fetchUserAndRecipes);
</script>

<template>
    <div class="min-h-screen py-10 flex flex-col items-center">
        <div v-if="loading" class="text-center">
            <p>Loading...</p>
        </div>

        <div v-else>
            <div class="text-center mb-12 ">
                <img :src="user.profile_photo" alt="Foto de perfil"
                    class="w-32 h-32 shadow-xl rounded-full mx-auto object-cover mb-4" />

                <h2 class="text-4xl pb-1 font-bold">{{ user.name }} {{ user.surname }}</h2>
                <p class="text-xl font-medium">{{ user.type }}</p>
            </div>

            <div class="w-full max-w-6xl px-6">
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
                    <RecipeCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" />
                </div>
            </div>
        </div>
    </div>
</template>
