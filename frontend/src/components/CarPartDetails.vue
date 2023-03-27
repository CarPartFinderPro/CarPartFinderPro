<template>
    <div>
      <h2>{{ carPart.title }}</h2>
      <div class="car-part-details">
        <p>Brand: {{ carPart.brand }}</p>
        <p>Model: {{ carPart.model }}</p>
        <p>Year: {{ carPart.year_from }}</p>
        <p>Price: {{ carPart.price }}</p>
        <p>Description: {{ carPart.description }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        carPart: {}
      }
    },
    mounted() {
      axios.get(`/api/car_parts/${this.$route.params.id}`)
        .then(response => {
          this.carPart = response.data;
        })
        .catch(error => {
          console.log(error);
        })
    }
  }
  </script>
  
  <style>
  .car-part-details {
    margin-top: 10px;
    font-size: 14px;
    color: #666;
  }
  </style>