<template>
    <div>
      <h2>Lista użytkowników</h2>
      <button @click="loadUsers">Pobierz użytkowników</button>
      <ul v-if="users.length">
        <li v-for="user in users" :key="user.id">
          {{ user.username }} - {{ user.email }}
        </li>
      </ul>
      <p v-else>Nie znaleziono użytkowników</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        users: []
      }
    },
    methods: {
      loadUsers() {
        axios.get('/api/users/')
          .then(response => {
            this.users = response.data;
          })
          .catch(error => {
            console.log(error);
          });
      }
    }
  }
  </script>