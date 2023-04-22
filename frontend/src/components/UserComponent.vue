<template>
    <div>
      <table class="user-details">
        <tbody>
          <tr>
            <td>Username:</td>
            <td>{{ user.username }}</td>
          </tr>
          <tr>
            <td>Password:</td>
            <td>
              <span v-if="!showPassword">{{ maskedPassword }}</span>
              <span v-show="showPassword">{{ user.password }}</span>
              <button @click="showPassword = !showPassword">{{ showPassword ? 'Hide' : 'Show' }}</button>
            </td>
          </tr>
          <tr>
            <td>Active:</td>
            <td>{{ user.active }}</td>
          </tr>
          <tr>
            <td>Email:</td>
            <td>{{ user.email }}</td>
          </tr>
          <tr>
            <td>Registration Date:</td>
            <td>{{ user.registration_date }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      user: {},
      showPassword: false
    }
  },
  mounted () {
    axios.get('/api/users/2/')
      .then(response => {
        this.user = response.data
      })
      .catch(error => {
        console.log(error)
      })
  },
  computed: {
    maskedPassword () {
      return this.user.password ? '*'.repeat(this.user.password.length) : ''
    }
  }
}
</script>

  <style>
  .user-details {
    height: 500px;
    width: 1200px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f1f1f1;
    border: 1px solid #ccc;
    border-radius: 5px;
    border-collapse: collapse;
  }
  .user-details h3 {
    margin: 0;
    font-size: 20px;
  }
  .user-details td {
    padding: 10px;
    font-size: 14px;
    color: #666;
    border: 1px solid #ccc;
  }
  .user-details p {
    margin: 0;
    font-size: 14px;
    color: #666;
  }
  .user-details td:first-child {
    font-weight: bold;
    background-color: #ddd;
  }
  </style>
