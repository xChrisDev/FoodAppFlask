<script setup>
import Button from 'primevue/button';

const props = defineProps({
    user: { type: Object }
})

</script>

<template>
    <div class="rounded-3xl shadow-xl bg-white w-96 p-6">
        <div class="flex items-center gap-4">
            <img :src="props.user.profile_photo" class="w-20 h-20 rounded-2xl shadow-md" />
            <div class="flex-1">
                <div class="flex justify-between items-center">
                    <h2 class="font-semibold text-lg text-gray-900">{{ props.user.name }} {{ props.user.surname }}</h2>
                    <div class="flex gap-1">
                        <Button v-tooltip.top="{ value: 'Update', showDelay: 100 }" icon="pi pi-pen-to-square"
                            size="small" severity="warn" rounded />
                        <Button v-tooltip.top="{ value: 'Delete', showDelay: 100 }" icon="pi pi-times" size="small"
                            severity="danger" rounded />
                    </div>
                </div>
                <p class="text-gray-600 text-sm mt-1">{{ props.user.type }}</p>
            </div>
        </div>
        <RouterLink :to="`/${props.user.id_user}/recipes`">
            <Button label="View Recipes" icon="pi pi-external-link" severity="info" size="small" class="w-full mt-4" />
        </RouterLink>
    </div>
</template>
