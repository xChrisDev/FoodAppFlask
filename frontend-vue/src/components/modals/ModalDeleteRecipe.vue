<script setup>
import { Button, Dialog } from 'primevue';
import { ref } from "vue";
import { useToast } from 'primevue';
import { useRouter } from 'vue-router'; // Importa useRouter
import { deleteRecipe } from '../../api/recipes';

const props = defineProps({
    recipe: Object
});

const toast = useToast();
const router = useRouter(); // Obtiene la instancia del router
const visible = ref(false);
const emit = defineEmits(['delete_recipe']);

const handleDeleteRecipe = async () => {
    try {
        const response = await deleteRecipe(props.recipe.id_user, props.recipe.id_recipe);

        if (response?.message) {
            toast.add({ severity: 'success', summary: 'Delete Recipe', detail: 'Recipe deleted successfully!', life: 5000 });
            visible.value = false;
            emit('delete_recipe');

            // Redireccionar a la página de recetas del usuario
            router.push(`/${props.recipe.id_user}/recipes`);
        } else {
            toast.add({ severity: 'error', summary: 'Delete Recipe', detail: 'Recipe not deleted', life: 5000 });
            visible.value = false;
        }
    } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to delete recipe', life: 5000 });
    }
};
</script>

<template>
    <Button v-tooltip.top="{ value: 'Delete', showDelay: 100 }" icon="pi pi-trash" severity="danger" label="Delete"
        @click="visible = true" />
    <Dialog v-model:visible="visible" modal header="Delete Recipe" :style="{ width: '25rem' }">
        <div class="mb-8">
            <h2>Are you sure you want to proceed?</h2>
        </div>
        <div class="flex justify-end gap-2">
            <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
            <Button type="button" label="Delete" severity="danger" @click="handleDeleteRecipe"></Button>
        </div>
    </Dialog>
</template>
