<script setup>
import { useRoute, useRouter } from 'vue-router';
import { getRecipeByUserAndId } from '../api/recipes';
import { ref, onMounted } from 'vue';
import { Button } from 'primevue';

const route = useRoute();
const router = useRouter();
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

            <div class="container mx-auto p-2">
                <div class="bg-white p-2 rounded-lg shadow-lg">
                    <img :src="recipe.image" :alt="recipe.title" class="w-full h-80 object-cover rounded-md mb-6" />

                    <div>
                        <h2 class="text-xl font-semibold text-gray-800">Preparation Steps</h2>
                        <p class="mt-4 text-gray-600">{{ recipe.steps }}</p>
                    </div>

                    <!-- Botones de Editar y Eliminar -->
                    <div class="mt-8 flex justify-end gap-1 items-center">
                        <Button v-tooltip.top="{ value: 'Update', showDelay: 100 }" icon="pi pi-pencil" severity="warn"
                            label="Update" />
                        <Button v-tooltip.top="{ value: 'Delete', showDelay: 100 }" icon="pi pi-trash" severity="danger"
                            label="Delete" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
