<template>
    <div>
      <div class="car-part-list">
        <ul>
            <!-- Use a v-for directive to loop through the carParts array and display each item in a list -->
            <li v-for="carPart in carParts" :key="carPart.id">
                <!-- Display the title, brand, model, year_from, and price of each car part -->
                <h3>Title: {{ carPart.title }}</h3>
                <p>Brand: {{ carPart.brand }}</p>
                <p>Model: {{ carPart.model }}</p>
                <p>Year: {{ carPart.year_from }}</p>
                <p>Price: {{ carPart.price }}</p>
            </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        // Define an empty array to store the car parts data
        carParts: []
      }
    },
    mounted() {
    // Use Axios to make a GET request to the API endpoint for car parts
      axios.get('/api/car_parts/')
        .then(response => {
        // When the response is received, set the carParts array to the data returned by the API
          this.carParts = response.data;
        })
        .catch(error => {
         // If there is an error, log it to the console
          console.log(error);
        })
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

.car-part-list ul {
  list-style: none;
  padding: 0;
}

.car-part-list li {
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.car-part-list li:last-child {
  border-bottom: none;
}
</style>