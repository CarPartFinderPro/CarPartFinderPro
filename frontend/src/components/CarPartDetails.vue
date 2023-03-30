<template>
  <div class="car-part-details">
    <h1>{{ carPart.title }}</h1>
    <div class="main-info">
      <div class="info-row">
        <div class="info-cell">Brand: {{ carPart.brand }}</div>
        <div class="info-cell">Model: {{ carPart.model }}</div>
      </div>
      <div class="info-row">
        <div class="info-cell">Year: {{ carPart.year_from }}</div>
        <div class="info-cell">Price: {{ carPart.price }} PLN</div>
      </div>
    </div>
    <div class="details-container">
      <div class="part-details">
        <h1>Additional informations about part</h1>
        <div class="details-info">
          <div class="details-row">
            <div class="details-cell">Part_number: {{ carPart.part_number }}</div>
            <div class="details-cell">Color_model: {{ carPart.color_model }}</div>
          </div>
          <div class="details-row">
            <div class="details-cell">Condition: {{ carPart.condition }}</div>
            <div class="details-cell">Seller: {{ user.username }}</div>
          </div>
        </div>
        <h1>Description</h1>
        <p>{{ carPart.description }}</p>
      </div>
      <div class="seller-info">
        <h3>Informations about seller:</h3>
        <p>Username: {{ user.username }}</p>
        <p>Email: {{ user.email }}</p>
      </div>
    </div>
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
      carPart: {},
      user: {} // Dodane
    }
  },
  mounted() {
    axios.get(`/api/car_parts/${this.id}/`)
      .then(response => {
        this.carPart = response.data;
        // Dodane: Pobierz dane użytkownika po otrzymaniu carPart
        return axios.get(`/api/users/${this.carPart.seller}/`);
      })
      .then(response => {
        // Dodane: Zaktualizuj dane użytkownika
        this.user = response.data;
      })
      .catch(error => {
        console.log(error);
      });
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
  font-size: 20px;
  color: black;
  width: 95%; /* Dodane */
  margin-left: auto;
  margin-right: auto;
  /* background-color: #f0e1c1; */
}

.car-part-details h1 {
  font-size: 32px;
  margin-bottom: 10px;
}

.main-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 15px;
  background-color: #2432c7;
  padding: 15px;
  border-radius: 5px;
  width: 100%;
  color:white
}

.info-row {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.info-cell {
  width: 50%;
  text-align: center;
}

.details-container {
  display: flex;
  flex-direction: column; /* Zaktualizowane */
  width: 100%; /* Zaktualizowane */
}

.part-details {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 15px;
  border-radius: 5px;
  width: 100%;
  margin-left: auto;
  margin-right: auto;
}
.part-details h1 {
  font-size: 30px;
  margin-bottom: 10px;
}
.part-details p {
  /* font-size: 30px; */
  text-align: center;
  margin-bottom: 5px;
}

.details-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  background-color: #2432c7;
  color: white;
  padding: 15px;
  margin-bottom: 20px;
}

.details-row {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.details-cell {
  width: 50%;
  text-align: center;
}

.seller-info {
  text-align: center; /* Zaktualizowane */
  padding: 15px;
  border-radius: 5px;
  width: 100%; /* Dodane */
  margin-top: 20px; /* Dodane */
  
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