<script setup>
import { Button, Dialog, InputText, FloatLabel } from 'primevue';
import { watch, ref } from "vue";
import { useToast } from 'primevue';
import { updateUser } from '../../api/users';

const props = defineProps({
    user: { type: Object }
})

const visible = ref(false);
const name = ref("")
const surname = ref("")
const type = ref("")
const profile_photo = ref("")

const toast = useToast();
const emit = defineEmits(['edit_user']);

const loadUserData = () => {
    profile_photo.value = props.user.profile_photo
    name.value = props.user.name
    surname.value = props.user.surname
    type.value = props.user.type
}

const handlePutUser = async () => {
    try {
        if (!name.value || !surname.value || !type.value) {
            toast.add({ severity: 'error', summary: 'Error', detail: 'All fields are required', life: 5000 });
            return;
        }

        const data = {
            name: name.value,
            surname: surname.value,
            type: type.value,
            profile_photo: profile_photo.value
        };

        const response = await updateUser(props.user.id_user, data);

        if (response?.message) {
            toast.add({ severity: 'success', summary: 'Edit User', detail: 'User updated successfully!', life: 5000 });
            name.value = "";
            surname.value = "";
            type.value = "";
            profile_photo.value = "";
            visible.value = false;
            emit('edit_user')
        } else {
            toast.add({ severity: 'error', summary: 'Edit User', detail: 'User not edited', life: 5000 });
            visible.value = false;
        }
    } catch (error) {
        toast.add({ severity: 'error', summary: 'Error', detail: 'Failed to edit user', life: 5000 });
    }
};

watch(visible, (newVal) => {
    if (newVal) {
        loadUserData();
    }
});

</script>

<template>
    <Button v-tooltip.top="{ value: 'Update', showDelay: 100 }" icon="pi pi-pen-to-square" size="small" severity="warn"
        rounded @click="visible = true" />
    <Dialog v-model:visible="visible" modal header="Edit User" :style="{ width: '25rem' }">
        <span class="text-surface-500 dark:text-surface-400 block mb-8">Edit your information.</span>

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
            <Button type="button" label="Save" severity="warn" @click="handlePutUser"></Button>
        </div>
    </Dialog>
</template>
