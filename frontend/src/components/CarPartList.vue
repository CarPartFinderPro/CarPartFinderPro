<template>
  <div>
    <div class="car-part-list">
      <div v-for="carPart in carParts" :key="carPart.id" class="car-part-item" @click="viewCarPart(carPart.id)">
        <h3 class="car-part-title">{{ carPart.title }}</h3>
        <div class="car-part-details">
          <p>Brand: {{ carPart.brand }}</p>
          <p>Model: {{ carPart.model }}</p>
          <p>Year: {{ carPart.year_from }}</p>
          <p>Price: {{ carPart.price }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      carParts: []
    }
  },
  mounted() {
    axios.get('/api/car_parts/')
      .then(response => {
        this.carParts = response.data;
      })
      .catch(error => {
        console.log(error);
      })
  },
  methods: {
    viewCarPart(carPartId) {
      this.$router.push(`/car_part/${carPartId}`);
    }
  }
}
</script>

<style>
.car-part-list {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f1f1f1;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.car-part-item {
  margin-bottom: 10px;
  padding: 10px;
  border-bottom: 1px solid #ccc;
  cursor: pointer;
}

.car-part-title {
  margin: 0;
  font-size: 20px;
}

.car-part-details {
  margin-top: 10px;
  font-size: 14px;
  color: #666;
}
</style>