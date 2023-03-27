<template>
    <div>
      <h1>{{ carPart.title }}</h1>
      <p>Brand: {{ carPart.brand }}</p>
      <p>Model: {{ carPart.model }}</p>
      <p>Year: {{ carPart.year_from }}</p>
      <p>Price: {{ carPart.price }}</p>
      <p>Description: {{ carPart.description }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: {
      id: {
        type: Number,
        required: true
      }
    },
    data() {
      return {
        carPart: {}
      }
    },
    mounted() {
      axios.get(`/api/car_parts/${this.id}/`)
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