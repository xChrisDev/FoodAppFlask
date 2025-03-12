<script setup>
import { Button, Dialog, InputText, Textarea, FloatLabel } from 'primevue';
import { ref } from "vue";

const visible = ref(false);
const title = ref("")
const steps = ref("")

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
            <Button type="button" label="Save" @click="visible = false"></Button>
        </div>
    </Dialog>
</template>
