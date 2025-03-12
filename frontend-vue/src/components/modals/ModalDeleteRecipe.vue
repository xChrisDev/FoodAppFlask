<script setup>
import { Button, Dialog } from 'primevue';
import { ref } from "vue";

const visible = ref(false);

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
            <Button type="button" label="Delete" severity="danger" @click="visible = false"></Button>
        </div>
    </Dialog>
</template>
