<script setup>
import { Button, Dialog, InputText, FloatLabel } from 'primevue';
import { ref } from "vue";
import { createUser } from '../../api/users';
import { useToast } from 'primevue/usetoast';

const visible = ref(false);
const name = ref("")
const surname = ref("")
const type = ref("")

const toast = useToast();
const emit = defineEmits(['add_user']);

const handlePostUser = async () => {
    try {
        if (!name.value || !surname.value || !type.value) {
            toast.add({ severity: 'error', summary: 'Error', detail: 'All fields are required', life: 5000 });
            return;
        }

        const data = {
            name: name.value,
            surname: surname.value,
            type: type.value,
            profile_photo: 'https://s3.amazonaws.com/37assets/svn/765-default-avatar.png'
        };

        const response = await createUser(data);

        if (response?.message) {
            toast.add({ severity: 'success', summary: 'Add User', detail: 'User added successfully!', life: 5000 });
            name.value = "";
            surname.value = "";
            type.value = "";
            visible.value = false;
            emit('add_user')
        } else {
            toast.add({ severity: 'error', summary: 'Add User', detail: 'User not added', life: 5000 });
            visible.value = false;
        }
    } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to add user', life: 5000 });
    }
};


</script>

<template>
    <Button v-tooltip.left="{ value: 'Add new user', showDelay: 100 }" label="New" icon="pi pi-plus" severity="success"
        @click="visible = true" />
    <Dialog v-model:visible="visible" modal header="Add User" :style="{ width: '25rem' }">
        <span class="text-surface-500 dark:text-surface-400 block mb-8">Set your information.</span>

        <div class="mb-4">
            <FloatLabel variant="in">
                <InputText id="name" v-model="name" variant="filled" class="w-full" />
                <label for="name">Name</label>
            </FloatLabel>
        </div>

        <div class="mb-4">
            <FloatLabel variant="in">
                <InputText id="surname" v-model="surname" variant="filled" class="w-full" />
                <label for="surname">Surname</label>
            </FloatLabel>
        </div>

        <div class="mb-8">
            <FloatLabel variant="in">
                <InputText id="type" v-model="type" variant="filled" class="w-full" />
                <label for="type">Type</label>
            </FloatLabel>
        </div>

        <div class="flex justify-end gap-2">
            <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
            <Button type="button" label="Save" @click="handlePostUser"></Button>
        </div>
    </Dialog>
</template>
