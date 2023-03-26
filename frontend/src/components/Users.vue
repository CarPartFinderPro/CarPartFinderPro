<template>
  <div>
    <ul>
      <li v-for="user in users" :key="user.id">{{ user.first_name }} {{ user.last_name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      users: [],
    };
  },
  mounted() {
    axios.get('http://localhost:8000/api/users/')
      .then(response => {
        this.users = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  },
};
</script>