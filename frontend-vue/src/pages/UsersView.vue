<script setup>
import UserCard from '../components/UserCard.vue';
import ModalAddUser from '../components/modals/ModalAddUser.vue';
import { Button, Toolbar, IconField, InputText, InputIcon, Skeleton } from 'primevue';
import { getAllUsers, getUserById } from '../api/users';
import { onMounted, ref } from 'vue';

const users = ref([]);
const id_user = ref(null);
const noResults = ref(false);
const loading = ref(true);

const fetchUsers = async () => {
    loading.value = true;
    noResults.value = false;
    users.value = [];

    const id = id_user.value?.trim() || "";
    try {
        if (id.length == 0) {
            users.value = await getAllUsers();
        } else {
            users.value = await getUserById(id);
        }
        noResults.value = users.value.length === 0;
    } catch (error) {
        noResults.value = true;
    } finally {
        setTimeout(() => {
            loading.value = false;
        }, 300);
    }
};

onMounted(() => {
    fetchUsers();
});
</script>

<template>
    <header>
        <Toolbar>
            <template #start>
                <div class="flex gap-2">
                    <IconField>
                        <InputIcon>
                            <i class="pi pi-search" />
                        </InputIcon>
                        <InputText placeholder="Search by ID..." v-model="id_user" />
                    </IconField>
                    <Button v-tooltip.right="{ value: 'Search', showDelay: 100 }" icon="pi pi-search" severity="info"
                        outlined @click="fetchUsers" @keydown.enter="fetchUsers" tabindex="0" />
                </div>
            </template>
            <template #end>
                <ModalAddUser @add_user="fetchUsers" />
            </template>
        </Toolbar>
    </header>

    <p v-if="noResults" class="text-center text-gray-500 mt-4">No users found with that ID.</p>

    <div v-else class="flex flex-wrap justify-center gap-2 mt-4">
        <template v-if="loading">
            <Skeleton v-for="n in 3" :key="n" width="390px" height="180px" class="rounded-lg" />
        </template>
        <template v-else>
            <UserCard v-for="user in users" :key="user.id" :user="user" @edit="fetchUsers" @delete="fetchUsers" />
        </template>
    </div>
</template>
