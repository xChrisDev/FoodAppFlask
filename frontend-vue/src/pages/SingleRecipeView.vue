<script setup>
import ModalEditRecipe from '../components/modals/ModalEditRecipe.vue';
import ModalDeleteRecipe from '../components/modals/ModalDeleteRecipe.vue';
import { useRoute } from 'vue-router';
import { getRecipeByUserAndId } from '../api/recipes';
import { ref, onMounted } from 'vue';

const route = useRoute();
const id_user = route.params.id_user;
const id_recipe = route.params.id_recipe;

const recipe = ref(null);
const loading = ref(true);

const fetchRecipeByUser = async () => {
    try {
        recipe.value = await getRecipeByUserAndId(id_user, id_recipe)
    } catch (error) {
        console.error('Error fetching data:', error);
    } finally {
        loading.value = false;
    }
}

onMounted(fetchRecipeByUser);
</script>

<template>
    <div class="mt-2 flex flex-col items-center">
        <div v-if="loading" class="text-center">
            <p class="text-lg text-gray-700">Loading...</p>
        </div>

        <div v-else class="w-full max-w-4xl bg-white rounded-lg shadow-lg overflow-hidden">
            <div class="bg-gradient-to-r from-blue-600 to-blue-400 text-white p-3 flex items-center justify-between">
                <h1 class="text-2xl font-bold">{{ recipe.title }}</h1>
            </div>

            <div class="container mx-auto">
                <div class="bg-white p-4">
                    <div class="flex flex-col md:flex-row gap-6">
                        <div class="w-full md:w-1/2 h-64 md:h-64 rounded-md border border-gray-300 overflow-hidden">
                            <img :src="recipe.image" :alt="recipe.title" class="w-full h-full object-cover" />
                        </div>
                        <div class="w-full md:w-1/2">
                            <h2 class="text-xl font-semibold text-gray-800">Preparation Steps</h2>
                            <p class="mt-4 text-gray-600">{{ recipe.steps }}</p>
                            <div class="mt-4 flex justify-end gap-2 items-center">
                                <ModalEditRecipe :recipe="recipe" @update_recipe="fetchRecipeByUser" />
                                <ModalDeleteRecipe :recipe="recipe" @delete_recipe="fetchRecipeByUser" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>