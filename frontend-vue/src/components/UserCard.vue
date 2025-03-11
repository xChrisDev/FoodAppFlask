<script setup>
import Button from 'primevue/button';
</script>

<template>
    <div class="rounded-3xl shadow-lg bg-white w-96 p-6 relative">
        <div class="flex justify-end gap-1">
            <Button icon="pi pi-times" size="small" severity="danger" rounded />
            <Button icon="pi pi-pen-to-square" size="small" severity="warn" rounded />
        </div>
        <div class="flex items-center gap-4 mt-2">
            <div
                class="w-24 h-24 bg-cyan-500 rounded-2xl flex justify-center items-center text-white text-2xl font-bold">
                IMG</div>
            <div>
                <h2 class="font-semibold text-xl text-gray-900">Helen Joe</h2>
                <p class="text-gray-500 text-xs">@helenjoe</p>
                <p class="text-gray-600 text-sm pt-3">Chef</p>
            </div>
        </div>

        <div class="flex justify-between items-center mt-6 text-gray-700">
            <div class="text-center">
                <p class="text-sm">Recipes</p>
                <p class="font-bold text-lg">41</p>
            </div>
            <div class="text-center">

            </div>
            <!-- Botón -->
            <Button label="View recipes" severity="info" size="small" />
        </div>
    </div>
</template>
