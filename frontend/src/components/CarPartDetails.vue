<template>
  <div class="car-part-details">
    <h1>{{ carPart.title }}</h1>
    <p>Brand: {{ carPart.brand }}</p>
    <p>Model: {{ carPart.model }}</p>
    <p>Year: {{ carPart.year_from }}</p>
    <p>Price: {{ carPart.price }}</p>
    <p>Part_number: {{ carPart.part_number }}</p>
    <p>Color_model: {{ carPart.color_model }}</p>
    <p>Condition: {{ carPart.condition }}</p>
    <p>Description: {{ carPart.description }}</p>
    <button @click="goToHomePage">Back to homepage</button>
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
  },
  methods: {
    goToHomePage() {
      this.$router.push('/');
    }
  }  
}
</script>

<style>
.car-part-details {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: 20px;
  font-size: 16px;
  color: white;
  background-color: #333;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0px 0px 10px #333;
}

.car-part-details h1 {
  font-size: 24px;
  margin-bottom: 10px;
}

.car-part-details p {
  margin: 5px;
}
 
.car-part-details button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
  background-color: #fff;
  color: #333;
  border-radius: 5px;
  cursor: pointer;
}
</style>