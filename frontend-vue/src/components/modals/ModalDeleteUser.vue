<script setup>
import { Button, Dialog } from 'primevue';
import { ref } from "vue";
import { deleteUser } from '../../api/users';
import { useToast } from 'primevue';

const visible = ref(false);
const toast = useToast();
const emit = defineEmits(['delete_user']);

const props = defineProps({
    id_user: { type: Number }
})

const handleDeleteUser = async () => {
    try {

        const response = await deleteUser(props.id_user);

        if (response?.message) {
            toast.add({ severity: 'success', summary: 'Delete User', detail: 'User deleted successfully!', life: 5000 });
            visible.value = false;
            emit('delete_user')
        } else {
            toast.add({ severity: 'error', summary: 'Delete User', detail: 'User not deleted', life: 5000 });
            visible.value = false;
        }
    } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to delete user', life: 5000 });
    }
};
</script>

<template>
    <Button v-tooltip.top="{ value: 'Delete', showDelay: 100 }" icon="pi pi-times" size="small" severity="danger"
        rounded @click="visible = true" />
    <Dialog v-model:visible="visible" modal header="Delete User" :style="{ width: '25rem' }">
        <div class="mb-8">
            <h2>Are you sure you want to proceed?</h2>
        </div>
        <div class="flex justify-end gap-2">
            <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
            <Button type="button" label="Delete" severity="danger" @click="handleDeleteUser"></Button>
        </div>
    </Dialog>
</template>
