<script setup>
import { Card, Button } from 'primevue';

const props = defineProps({
    recipe: {
        type: Object
    }
})
</script>

<template>
    <div class="flex justify-center items-center">
        <Card class="w-92 shadow-lg">
            <template #header>
                <img :src="props.recipe.image" class="w-full h-48 object-cover rounded-t-lg" />
            </template>
            <template #title>
                <h2 class="text-xl font-bold text-gray-800">{{ props.recipe.title }}</h2>
            </template>
            <template #content>
                <p class="text-gray-600">{{ props.recipe.steps }}</p>
            </template>
            <template #footer>
                <RouterLink :to="`/${props.recipe.id_user}/recipes/${props.recipe.id_recipe}`">
                    <Button label="More details" icon="pi pi-external-link" severity="info" size="small"
                        class="w-full mt-4" />
                </RouterLink>
            </template>
        </Card>
    </div>
</template>