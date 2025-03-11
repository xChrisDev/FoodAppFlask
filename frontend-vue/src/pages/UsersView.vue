<script setup>
import UserCard from '../components/UserCard.vue'
import NavBar from '../components/NavBar.vue';
import { getAllUsers } from '../api/users';
import { onMounted, ref } from 'vue';

const users = ref([])

const fetchUsers = async () => {
    users.value = await getAllUsers();
    console.log(users.value)
}

onMounted(fetchUsers)

</script>

<template>
    <header>
        <NavBar />
    </header>
    <div class=" flex flex-wrap justify-center gap-2 mt-4">
        <UserCard v-for="user in users" :user="user" />
    </div>
</template>