<script setup>
import { Button, Dialog, InputText, Textarea, FloatLabel } from 'primevue';
import { ref } from "vue";
import { createRecipe } from '../../api/recipes';
import { useToast } from 'primevue';

const visible = ref(false);
const title = ref("")
const steps = ref("")
const toast = useToast();

const emit = defineEmits(['add_recipe'])

const props = defineProps({
    id_user: {
        type: Number
    }
})

const handleAddRecipe = async () => {
    try {
        if (!title.value || !steps.value) {
            toast.add({ severity: 'error', summary: 'Error', detail: 'All fields are required', life: 5000 });
            return;
        }

        const data = {
            id_user: props.id_user,
            title: title.value,
            steps: steps.value,
            image: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ8AxgZbnk93FKz8jDp91BzvvRwufyv7nrIA&s'
        };

        const response = await createRecipe(props.id_user, data);

        if (response?.message) {
            toast.add({ severity: 'success', summary: 'Add Recipe', detail: 'Recipe added successfully!', life: 5000 });
            title.value = "";
            steps.value = "";
            visible.value = false;
            emit('add_recipe')
        } else {
            toast.add({ severity: 'error', summary: 'Add Recipe', detail: 'Recipe not added', life: 5000 });
            visible.value = false;
        }
    } catch (error) {
        console.log(error)
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to add recipe', life: 5000 });
    }
};

</script>

<template>
    <Button v-tooltip.left="{ value: 'Add new recipe', showDelay: 100 }" label="New recipe" icon="pi pi-plus"
        severity="success" @click="visible = true" />
    <Dialog v-model:visible="visible" modal header="Add new recipe" :style="{ width: '25rem' }">
        <span class="text-surface-500 dark:text-surface-400 block mb-8">Set recipe details.</span>

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
            <Button type="button" label="Save" @click="handleAddRecipe"></Button>
        </div>
    </Dialog>
</template>
