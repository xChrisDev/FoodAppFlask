<script setup>
import { Button, Toolbar, IconField, InputText, InputIcon } from 'primevue';
</script>

<template>
    <Toolbar>
        <template #start>
            <div class="flex gap-2">
                <IconField>
                    <InputIcon>
                        <i class="pi pi-search" />
                    </InputIcon>
                    <InputText placeholder="Search" />
                </IconField>
                <Button v-tooltip.right="{ value: 'Search', showDelay: 100 }" icon="pi pi-search"
                    severity="info" outlined/>
            </div>
        </template>

        <template #end>
            <Button v-tooltip.left="{ value: 'Add new user', showDelay: 100 }" label="New" icon="pi pi-plus"
                severity="success" />
        </template>
    </Toolbar>

</template>