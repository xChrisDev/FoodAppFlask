<script setup>
import ModalAddRecipe from '../components/modals/ModalAddRecipe.vue';
import RecipeCard from '../components/RecipeCard.vue';
import { onMounted, ref } from 'vue';
import { getAllRecipesByUser } from '../api/recipes';
import { useRoute, useRouter } from 'vue-router';
import { getUserById } from '../api/users';
import { Button } from 'primevue';

const router = useRouter();
const route = useRoute();
const id_user = route.params.id_user;

const user = ref(null);
const recipes = ref([]);
const loading = ref(true);
const errorMessage = ref("");

const fetchUserAndRecipes = async () => {
    try {
        user.value = await getUserById(id_user);
        const response = await getAllRecipesByUser(id_user);
        errorMessage.value = "";

        if (response.error) {
            errorMessage.value = response.error;
        } else {
            recipes.value = response;
        }
    } catch (error) {
        errorMessage.value = "This user doesn't have recipes!";
    } finally {
        loading.value = false;
    }
};

const redirectHome = () => {
    router.push('/')
}

onMounted(() => {
    fetchUserAndRecipes();
});

</script>

<template>
    <div class="min-h-screen py-10 flex flex-col items-center">
        <div v-if="loading" class="text-center">
            <p>Loading...</p>
        </div>

        <div v-else>
            <div class="text-center mb-4">
                <img :src="user[0].profile_photo" alt="Foto de perfil"
                    class="w-24 h-24 shadow-xl rounded-full mx-auto object-cover mb-4" />

                <h2 class="text-2xl pb-1 font-bold">{{ user[0].name }} {{ user[0].surname }}</h2>
                <p class="text-md font-medium">{{ user[0].type }}</p>
            </div>

            <div class="w-full flex justify-between px-6 my-4">
                <Button icon="pi pi-home" severity="contrast" label="Home" @click="redirectHome"/>
                <ModalAddRecipe :id_user="parseInt(id_user)" @add_recipe="fetchUserAndRecipes" />
            </div>

            <div v-if="errorMessage" class="w-[500px] max-w-6xl px-6 text-center mt-10">
                <p class="text-2xl font-semibold text-red-500">{{ errorMessage }}</p>
            </div>

            <div v-else class="w-full max-w-6xl px-6">
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                    <RecipeCard v-for="recipe in recipes" :key="recipe.id" :recipe="recipe" />
                </div>
            </div>
        </div>
    </div>
</template>
