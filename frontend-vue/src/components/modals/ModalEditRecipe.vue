<script setup>
import { Button, Dialog, InputText, Textarea, FloatLabel } from 'primevue';
import { onMounted, ref } from "vue";
import { useToast } from 'primevue';
import { updateRecipe } from '../../api/recipes';

const toast = useToast();
const visible = ref(false);
const title = ref("")
const steps = ref("")

const emit = defineEmits(['update_recipe'])

const props = defineProps({
    recipe: Object
})

const handleUpdateRecipe = async () => {
    try {
        if (!title.value || !steps.value) {
            toast.add({ severity: 'error', summary: 'Error', detail: 'All fields are required', life: 5000 });
            return;
        }

        const data = {
            title: title.value,
            steps: steps.value,
            image: props.recipe.image
        };

        const response = await updateRecipe(props.recipe.id_user, props.recipe.id_recipe, data);

        if (response?.message) {
            toast.add({ severity: 'success', summary: 'Update Recipe', detail: 'Recipe updated successfully!', life: 5000 });
            title.value = "";
            steps.value = "";
            visible.value = false;
            emit('update_recipe')
        } else {
            toast.add({ severity: 'error', summary: 'Update Recipe', detail: 'Recipe not edited', life: 5000 });
            visible.value = false;
        }
    } catch (error) {
        console.log(error)
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to update recipe', life: 5000 });
    }
};
onMounted(() => {
    title.value = props.recipe.title
    steps.value = props.recipe.steps
})
</script>

<template>
    <Button v-tooltip.top="{ value: 'Update', showDelay: 100 }" icon="pi pi-pencil" severity="warn" label="Update"
        @click="visible = true" />
    <Dialog v-model:visible="visible" modal header="Edit new recipe" :style="{ width: '25rem' }">
        <span class="text-surface-500 dark:text-surface-400 block mb-8">Edit recipe details.</span>

        <div class="mb-4">
            <FloatLabel variant="in">
                <InputText id="title" v-model="title" variant="filled" class="w-full" />
                <label for="title">Title</label>
            </FloatLabel>
        </div>

        <div class="mb-8">
            <FloatLabel variant="in">
                <Textarea class="w-full resize-none" id="steps" v-model="steps" variant="filled" rows="6" cols="30" />
                <label for="steps">Steps</label>
            </FloatLabel>
        </div>

        <div class="flex justify-end gap-2">
            <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
            <Button type="button" label="Save" severity="warn" @click="handleUpdateRecipe"></Button>
        </div>
    </Dialog>
</template>
